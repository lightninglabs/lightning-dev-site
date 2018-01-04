---
layout: page
title: Stage 4 - Webapp Integration
---

In this stage, we will integrate Lightning micropayments into our server-side
web application.

### Starting Afresh

It's time to recreate the micropayments ourselves. Get the starter code:

```bash
# Clear any local changes first and checkout the start tag
git checkout -- .
git checkout start
```

The starter code has stripped out all micropayments code, and we just also just
reset our database state to the default.

### The models

First, let's examine `coindesk/models.py` to understand our web app a little
better.

`coindesk/models.py` (cleaned up a little bit):
{% raw %}
```python
class Profile(models.Model):
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    identity_pubkey = models.CharField(max_length=80, unique=True)
    # bitcoin_address = BitcoinAddressField()


class Article(models.Model):

    ARTICLE_STATUS_CHOICES = (
        ('visible', 'Visible'),
        ('deleted by admin', 'Deleted by admin'),
    )

    title = models.CharField(max_length=191)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='visible', choices=ARTICLE_STATUS_CHOICES)

    @property
    def views(self):
        return self.payments.filter(status='complete', purpose='view').count()


class Payment(models.Model):

    PAYMENT_STATUS_CHOICES = (
        ('pending_invoice', 'Pending Invoice'), # Should be atomic
        ('pending_payment', 'Pending Payment'),
        ('complete', 'Complete'),
        ('error', 'Error'),
    )

    PAYMENT_PURPOSE_CHOICES = (
        ('view', 'View'),
        ('upvote', 'Upvote')
    )

    user = models.ForeignKey(User)
    article = models.ForeignKey(Article, related_name='payments')
    purpose = models.CharField(max_length=10, choices=PAYMENT_PURPOSE_CHOICES)

    satoshi_amount = models.IntegerField()
    r_hash = models.CharField(max_length=64)
    payment_request = models.CharField(max_length=1000)

    status = models.CharField(max_length=50, default='pending_invoice', choices=PAYMENT_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def generate_invoice(self, user, article):
        """
        Generates a new invoice
        """
        pass

    def check_payment(self):
        """
        Checks if the Lightning payment has been received for this invoice
        """
        pass
```
{% endraw %}

Each `Profile` object is associated with one `User` object, and stores the
identity pubkey of that user.

The `Article` class has a title, text, a timestamp and some basic moderation
functionality. Notice that the number of views for an article as counted as the
number of completed payments associated with it.

The `Payment` class represents a Lightning micropayment, and is going to be
where we implement the bulk of our work. Each payment is associated with a particular user and a article.

We have the `satoshi_amount`, `r_hash` and `payment_request` fields - the basic technical information
required to conduct a Lightning payment.

Each `Payment` goes through the
following lifecycle, represented by the `status` field:

1. The payment is initially pending an invoice. Calling `generate_invoice` will
generate an invoice for a user and a particular article they want to view.
2. After the invoice is generated, it is now pending payment.
3. `check_payment` will check if a payment has indeed been received by Bob
node. Afterwards, this `Payment` counts as complete, and the user should be
able to view the article.

It will soon be up to us to implement the `generate_invoice` and
`check_payment` functions. But first, let's add in some security.


### The views

We also need to understand some of the wiring behind the app.

Open `coindesk/views.py`. For our purposes, the `article` view is the most
important since it is executed when we view an article and handles what to do
with the different payment states.

{% raw %}
```python
def article(request, pk):

    try:
        article = Article.objects.filter(status='visible').get(id=pk)
    except Article.DoesNotExist:
        raise Exception("Article with id {} does not exist or is not visible".format(pk))

    context = {'article': article}

    if not request.user.is_authenticated():
        return render(request,
            template_name='article.html',
            context=context)

    qs = article.payments.filter(user=request.user, purpose='view')

    if qs.count() == 0:
        # Generate a new payment
        payment, _ = Payment.objects.get_or_create(user=request.user,
                          article=article,
                          purpose='view',
                          satoshi_amount=settings.MIN_VIEW_AMOUNT,
                          status='pending_invoice')
        payment.save()
    elif qs.count() == 1:
        payment = qs.last()
    else:
        # This should not happen because there should never be more than one view payment per article per person
        raise Exception("Multiple payments detected")

    # User client requests that we check if the payment has been made
    if request.GET.get('check'):
        print "Checking for payment {}".format(payment.payment_request)
        if payment.check_payment():
            print "Payment succeeded!"
        else:
            print "Payment not received"

    if payment.status == 'pending_invoice':
        payment.generate_invoice(request.user, article)
    elif payment.status == 'pending_payment':
        # Do nothing; display the payment page to user
        pass
    elif payment.status == 'complete':
        # Do nothing; display the article to user
        pass
    elif payment.status == 'error':
        # TODO Optionally implement some kind of error resolution
        pass
        raise Exception("Payment error")
    else:
        context['payment_status'] = payment.status

    context['payment'] = payment

    return render(request,
        template_name='article.html',
        context=context)
```
{% endraw %}

A quick breakdown of what's going on:
1. First, we try to find the appropriate `Article` by its id. If successful, we
   populate the `context` variable so that the template can work with it.
2. If the user is not logged in, we can't check for a payment from them because
   we don't know who they are, so we just direct them to the article page.
3. We attempt to find a `Payment` for this particular `User` and `Article`. If
   a `Payment` was not found, we generate a new one. The satoshi amount is set
   by `settings.MIN_VIEW_AMOUNT`, which defaults to 1000 satoshis.  This newly
   created `Payment` has the initial state: `pending_invoice`.
4. If the user provides the `check` query parameter, we call the
   `check_payment` function, which will check if the payment was indeed
   complete and update the state if so.
5. If the payment is pending an invoice, we call the `generate_invoice`
   function, which will generate the invoice and update the Payment state.
6. If the payment is in any other state, we render `article.html` for the user
   or throw an error.

### Adding in a paywall

Right now, all the articles in the app are freely viewable. We all know no one
likes free stuff, so let's fix that.

We will begin by adding some conditionals in the html where we are currently
displaying the article content.

In `coindesk/templates/article.html`, notice the following code:
{% raw %}
```html
<div class="article-body">
  <div class="article-text">
    {{ article.text }}
  </div>
</div>
```
{% endraw %}

{% raw %}`{{ article.text }}`{% endraw %} is the Django template variable
representing the text of the website. We need to hide this for all
non-authenticated users. Let's show them the `pay.html` page instead. And of
course, users who have completed payments must be able to view the article
text.

Make the necessary edits: 
{% raw %}
```html
<div class="article-body">
  {% if not request.user.is_authenticated %}
    <h3>Make Payment</h3>
    <p>
      To view this article, please log in and return to this page to make
      a payment.
    </p>
    <a id="complete_button" href="/login">Log in</a>
  {% elif payment.status == "complete" %}
    <div class="article-text">
      {{ article.text }}
    </div>
  {% else %}
    <div>
      {% include "pay.html" %}
    </div>
  {% endif %}
</div>
```
{% endraw %}

As this is a Lightning tutorial, understanding the exact syntax is not
important, but a quick clarification may be helpful:
- The {% raw %}`{% if %}`{% endraw %} blocks are Django's way of adding
  conditionals in html templates. We are using this to determine if users are
  logged in or if the payment is complete.
- `payment` is a context variable the template needs populated in order to
  render correctly and access the relevant information. This was done in the
  `article` view.
- The {% raw %}`{% include %}`{% endraw %} tag adds in the template by the name
  of `pay.html`.

We should now see something like this when we click on an article:
![logged out article page](http://i.imgur.com/bVc4M06.png)

### Generating an invoice

Examine `coindesk/templates/pay.html`:
{% raw %}
```html
<div id="payment" class="ln-dialog">
  <div id="submit_box" class="animated fadeInDown delay">
    <h3>Make Payment</h3>
    <p>To view this article, please pay 1000 satoshis via the request below:</p>
    <p class="small">{{ payment.payment_request }}</p><br>
    <a id="complete_button" href="/articles/{{ article.id }}/?check=true">Complete</a>
  </div>
</div>
```
{% endraw %}

This template prompts the user to pay 1000 satoshis, and supplies a payment
request.

Log in as Alice. The page should look something like this:
![logged in article page with payment prompt missing payment
request](http://i.imgur.com/FpyjezK.png)

We are missing the payment request, so let's generate an invoice.

Navigate to `generate_invoice` in `coindesk/models.py`. Modify it to the
following:

{% raw %}
```python
def generate_invoice(self, user, article):
    """
    Generates a new invoice
    """
    assert self.status == 'pending_invoice', "Already generated invoice"
    channel = grpc.insecure_channel(settings.LND_RPCHOST)
    stub = lnrpc.LightningStub(channel)

    add_invoice_resp = stub.AddInvoice(ln.Invoice(value=settings.MIN_VIEW_AMOUNT, memo="User '{}' | ArticleId {}".format(user.username, article.id)))
    r_hash_base64 = codecs.encode(add_invoice_resp.r_hash, 'base64')
    self.r_hash = r_hash_base64.decode('utf-8')
    self.payment_request = add_invoice_resp.payment_request
    self.status = 'pending_payment'
    self.save()
```
{% endraw %}

Don't forget also to include the necessary imports at the top of the file:
```python
from coindesk import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
import grpc
```

Walking through the code:
- We first check that this `Payment` is indeed pending an invoice, and throw an
  error otherwise.
- Using gRPC, we add an invoice of the amount set by `MIN_VIEW_AMOUNT` in
  `settings.py`.
- We set the `r_hash` and `payment_request` attributes and update the state of
  this `Payment` to now be pending payment.


### Checking for payment receipt

The last piece needed for our fully functional Lightning Coindesk is to
implement the `check_payment` function of the `Payment` class. Recall from
`coindesk.views.` that `check_payment()` is called if the user passes along the
`check` query parameter. For your convenience, we have already implemented this
for you in the frontend:

In `coindesk/templates/pay.html`:
```html
<a id="complete_button" href="/articles/{{ article.id }}/?check=true">Complete</a>
```

Now, try to implement the `check_payment` function yourself. Here's some
starter code to help you with the annoying and unimportant parts:

```python
def check_payment(self):
    """
    Checks if the Lightning payment has been received for this invoice
    """
    if self.status == 'pending_invoice':
        return False

    # Prepare r_hash_bytes, which can be passed into the gRPC client
    r_hash_base64 = self.r_hash.encode('utf-8')
    r_hash_bytes = str(codecs.decode(r_hash_base64, 'base64'))

    # Implement this
    payment_settled = False

    if payment_settled:
        # Payment complete
        self.status = 'complete'
        self.save()
        return True
    else:
        # Payment not received
        return False
```

If you're absolutely stuck, you may refer to the [tutorial
repo](https://github.com/MaxFangX/lightning-coindesk) for the final solution.

### Conclusion

Congratulations! You have now built a working Lightning Coindesk app! If you
are looking to take this tutorial to the next level, consider trying one or
more of the following:

- Integrate error handling in the webapp; see the TODO in
  `coindesk.views.article`
- Add P2P payments through the app. Instead of paying the central server,
  distribute your micropayment equally between all the people who upvoted
  before you. The upvote functionality was intentionally left unimplemented for
  this purpose.
- Run this application in a more "production" environment, by using `testnet`
  and deploying your webapp online
- Allow the server to accept Litecoin in addition to Bitcoin.

At this point, you're ready to build with `lnd`. Go forth and bring
Bitcoin to the masses!

#### Next Steps

Read through the [LND Overview and Developer Guide](/overview/) to see best
practices and guidelines for implementing LND in your own webapp, or for a
conceptual brushup of the Lightning Network.

Check out the accessible dev manuals available on our [Guides page](/guides/).

#### Navigation
- [Return to Stage 3 - RPC Client](/tutorial/03-rpc-client)
- [Return to main tutorial page](/tutorial/)

### Questions
- Join the #dev-help channel on our [Community
  Slack](https://lightningcommunity.slack.com/join/shared_invite/enQtMjk0OTYxNzI4NzExLTFhZDA5YTYxZDU2YWQyOTQzN2ZkMzk3ZGUwNGM0NjE2NzQyNjAyZTkwOTFkZjJmMmMyNzlmNmE5YTRmMGFhM2Q)
- Join IRC:
  [![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lnd)
