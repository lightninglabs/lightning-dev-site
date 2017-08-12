---
layout: page
title: Stage 3 - RPC Client
---

In this section, we will run the finished tutorial app and set up a gRPC client
for programmatic access to our `lnd` nodes.

### Setting up our web development workspace

Let's set up our news site. Before beginning, ensure that you are running
Python 2.7 and that you have
[`pip`](https://pip.pypa.io/en/stable/installing/) and
[`virtualenv`](https://virtualenv.pypa.io/en/stable/installation/) installed.
```bash
# Create a new workspace which will hold both the repo and the virtualenv. We
# recommend running this in a new terminal window.
mkdir ln-coindesk
cd ln-coindesk

# Clone the repo
git clone https://github.com/MaxFangX/lightning-coindesk

# Create virtualenv and activate it. Make sure to activate this environment
# whenever you are working with the coindesk app.
virtualenv deskenv
source deskenv/bin/activate

# Install webapp Python requirements
cd lightning-coindesk
pip install -r requirements.txt
```

Now, let's set up Python gRPC so that we can run our website
```bash
# Install the dependencies required for gRPC
pip install grpcio grpcio-tools googleapis-common-protos

# Run our webserver
python manage.py runserver
```

Notice that in `coindesk/settings.py` we have set
`LND_RPCHOST = "localhost:10002"`. In other words, your server is connected to
the "Bob" `lnd` node, and making payments to it is equivalent to making
payments to Bob.

### Testing the app

If everything went smoothly, you should now have a web server exposed at port
8000. 
![lightning coindesk homepage](http://i.imgur.com/D2LgBUi.png)

Feel free to click around the site. You will soon find that you need to log in
and make a payment to view the articles.

![login page](http://i.imgur.com/zLTEYfk.png)

To prevent `lnd` users from having to go through the hassle of signing up with
an email address and password, we created an authentication scheme based on the
user's `lnd` identity pubkey and logging in by signing an arbitrary message. In
particular, we are signing the CSRF token sent along with the login POST
request. This scheme is secure against replay attacks because Django generates
a unique CSRF token for every login attempt, and never uses CSRF tokens.

Let's create a new account for Alice by logging in and supplying a username.
Copy down the generated message (in the screenshot, it is `VcccAuMC...`)

```bash
alice$ lncli-alice signmessage <GENERATED_MESSAGE>
{
    "signature": <SIGNATURE>
}
```

Paste `<SIGNATURE>` into the corresponding field and set `alice` as the desired
username. You should now be logged in as Alice.

![logged in homepage](http://imgur.com/BGSunzy.png)

Navigate to the sweet article and make a payment from the Alice node (you can
use either the command line or the web GUI. Clicking "Complete" will prompt the
webserver to check that the payment has been complete, and you can now enjoy
reading through this sweet article.

### Setting up gRPC

Let's practice running some commands on gRPC. Open up a new terminal window then proceed as follows:

```bash
# Enter the development environment
cd ln-coindesk

# Activate Python virtualenv
source deskenv/bin/activate

# Clone the Google API repository, which is required due to the use of
# google/api/annotations.proto
git clone https://github.com/googleapis/googleapis.git

# Download the lnd rpc.proto file
curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto

# Compile the proto file
python -m grpc_tools.protoc --proto_path=googleapis:. --python_out=. --grpc_python_out=. rpc.proto
```

We have now generated the two files `rpc_pb2.py` and `rpc_pb2_grpc.py`, which
you'll need to import into your Python code in order to use it with lnd. Let's move it into the coindesk folder for easy access
```bash
mv rpc* lightning-coindesk/coindesk
```

We will now try a few commands with the Python gRPC client from the command
line.
```bash
# Optionally install ipython for prettier command line output
pip install ipython

# Open the Django shell. This is a standard Python shell that also allows access to Django objects.
cd lightning-coindesk
python manage.py shell
```

```python
# Import rpc files and grpc
In [1]: from coindesk import rpc_pb2 as ln, rpc_pb2_grpc as lnrpc
In [2]: import grpc

# Establish a secure connection with our RPC server. We will first have to
# gather our cert. Lnd cert is at ~/.lnd/tls.cert on Linux and
# ~/Library/Application Support/Lnd/tls.cert on Mac
In [3]: cert = open('~/.lnd/tls.cert').read()
In [4]: creds = grpc.ssl_channel_credentials(cert)
In [5]: channel = grpc.secure_channel('localhost:10009', creds)
# Create a new 'stub' object that will allow us to interact with our "Bob" lnd node.
In [6]: stub = lnrpc.LightningStub(channel)

# Make a call to the ListChannels API.
In [7]: listchannels_resp = stub.ListChannels(ln.ListChannelsRequest())
Out[7]:
channels {
  active: true
  remote_pubkey: "02244b8eff01be9f7b4ec1d73ab10fc36da48b01a685ac90ed09a63fe94ec08d0a"
  channel_point: "2622b779a8acca471a738b0796cd62e4457b79b33265cbfa687aadccc329023a:0"
  chan_id: 495879744192512
  capacity: 1000000
  local_balance: 21001
  remote_balance: 970311
  commit_fee: 8688
  commit_weight: 724
  fee_per_kw: 12000
  total_satoshis_received: 21001
  num_updates: 8
}
channels {
  active: true
  remote_pubkey: "032eed260ef71110a02a5da44d82fef9628ffa51113a2d0b9524e7d3bff615a1cf"
  channel_point: "028088c354b26c33cfd5a5b2d4cca27c6e3a73b6752b5beff6f67ce779af5656:1"
  chan_id: 554153860464641
  capacity: 800000
  local_balance: 190000
  remote_balance: 601312
  commit_fee: 8688
  commit_weight: 724
  fee_per_kw: 12000
  total_satoshis_sent: 10000
  num_updates: 2
}
```
What happened here? We constructed the request object for the list channels
command with `ln.ListChannelsRequest()`, and passed it into the `ListChannels`
function exposed by our stub. 

The response was saved into a `listchannels_resp` variable that holds all the
information returned by the `listchannels` command. You can now access the
individual properties of this object; for example, you can access the `chan_id`
of Bob's first channel with `listchannels_resp.channels[0].chan_id`.

### Playing with gRPC

To get a hang of the RPC documentation, try running a slightly more complex
command like `GetChanInfo`, which requires passing in some parameters. The API
docs are not yet complete, but you can refer to the [RPC documentation in
lnd](https://github.com/lightningnetwork/lnd/blob/master/lnrpc/rpc.proto).

Hint: look at the `GetChanInfo` object and the associated requests and
responses.

### Moving on to Step 4

By now, you should have at least a basic understanding of how to work with lnd
from a gRPC client.  In [Stage 4](/tutorial/04-webapp-integration), we will
finally integrate `lnd` into our news site.

#### Navigation
- [Proceed to Stage 4 - Webapp Integration](/tutorial/04-webapp-integration)
- [Return to Stage 2 - Web Client](/tutorial/02-web-client)
- [Return to main tutorial page](/tutorial/)

### Questions
- Join the #dev-help channel on our [Community
  Slack](https://join.slack.com/t/lightningcommunity/shared_invite/MjE0NDkzNDM5NzQ3LTE1MDA0MjE0NzctODNlZDlmNWYzOA)
- Join IRC:
  [![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lnd)
