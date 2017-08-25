---
layout: page
title: Stage 2 - Web Client
---

In this section we will learn how to set up and interact with `lnd` using a
[web client](https://github.com/mably/lncli-web) built by [Francois
Mably](https://github.com/mably). Setup instructions are courtesy of the
creator himself. Before beginning this step make sure you have `node` and `npm`
installed.

### Setting up the LND web client

```bash
# Clone the repo and move into it:
git clone https://github.com/mably/lncli-web
cd lncli-web

# Install dependencies
npm install

# Setup default configuration files
"./node_modules/.bin/gulp" bundle

# Start the server to point to our Alice node:
node server --lndhost=localhost:10001

# Check out the available command line arguments
node server --help
```

Open up [`http://localhost:8280/`](http://localhost:8280/) in your browser to see the web dashboard.

### Poking around

Now would be a good time to reopen that channel we had between Alice and Bob.
Except this time, we're going to do it through the web dashboard. Feel free to
try this on your own - the web dashboard is intuitive enough that we don't need
step by step instructions for it.

Note: The LND wallet is coming soon! Sign up for our newsletter at the bottom
of our [community page](http://lightning.community#mc-embedded-subscribe-form)

### Moving on to Step 3

By now, you should have gained familiarity with the web client.
In [Stage 3](/tutorial/03-rpc-client), we will learn how to set up a gRPC
client for programmatic access to our `lnd` nodes.

#### Navigation
- [Proceed to Stage 3 - RPC Client](/tutorial/03-rpc-client)
- [Return to Stage 1 - Setting up a local cluster](/tutorial/01-lncli)
- [Return to main tutorial page](/tutorial/)

### Questions
- Join the #dev-help channel on our [Community
  Slack](https://join.slack.com/t/lightningcommunity/shared_invite/MjI4OTg3MzQ4MjI2LTE1MDMxNzM1NTMtNjlmOGYzOTI1Ng)
- Join IRC:
  [![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lnd)
