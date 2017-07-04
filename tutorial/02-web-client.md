---
layout: page
title: Stage 2 - Web Client
---

In this section we will learn how to set up and interact with `lnd` using a
[web client](https://github.com/mably/lncli-web) built by [Francois
Mably](https://github.com/mably). Setup instructions are courtesy of the
creator himself.

### Setting up the LND web client

```bash
# Clone the repo and move into it:
git clone https://github.com/mably/lncli-web
cd lncli-web

# Install dependencies
npm install

# Fetch and install all the front end dependencies
"./node_modules/.bin/bower" install --allow-root

# Setup default configuration files
"./node_modules/.bin/gulp" install

# Start the server to point to our Alice node:
node server --lndhost=localhost:10001

# Check out the available command line arguments
node server --help
```

Open up `http://localhost:8280/` in your browser to see the web dashboard.

### Poking around

Now would be a good time to reopen that channel we had between Alice and Bob.
Except this time, we're going to do it through the web dashboard. Feel free to
try this on your own - the web dashboard is intuitive enough that we don't need
step by step instructions for it.

Note: The LND wallet is coming soon! Sign up for our newsletter at the bottom
of our [community page](https://lightning.community#mc-embedded-subscribe-form)

### Moving on to Step 3

By now, you should have gained familiarity with the web client.
In [Stage 3](/tutorial/03-rpc-client), we will learn how to set up an gRPC
client for programmatic access to our `lnd` nodes.

[Proceed to Stage 3 - Web Client](/tutorial/03-rpc-client)

### Questions
[![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lnd)
