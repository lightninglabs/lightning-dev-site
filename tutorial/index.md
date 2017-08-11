---
layout: page
title: Tutorial
---

### Overview

This tutorial will get you up to speed with all the skills necessary to work
with [`lnd`](https://github.com/lightningnetwork/lnd). We will be building a
Bitcoin micropayments paywell into a news site!

Those seeking more conceptual familiarity with the Lightning Network can read
through the [LND Overview and Developer Guide](/overview/). It also contains a
more in-depth explanation of the components covered in this tutorial, and
includes best practices for integrating LND. It is not required knowledge for
completing this tutorial, but we recommend that you at least skim through the
guide before attempting to build your own app.

The tutorial assumes you have completed installation of Go, `btcd`, and `lnd`
on simnet. If not, the [installation instructions](/guides/installation/) will
guide you through the process.

### Stages

Each of the different stages of this tutorial is oriented towards a specific
skill. Beginners should start at [stage 1](/tutorial/01-lncli). Otherwise, jump
wherever you want below!

- **[Stage 1 - Setting up a local cluster](/tutorial/01-lncli)**
    - How to set up a local environment with three nodes that can make payments
      with and through one another.
    - Gain experience interacting with `lnd` from the command line.
- **[Stage 2 - Web Client](/tutorial/02-web-client)**
    - How to run and use a `lnd` web GUI.
- **[Stage 3 - RPC Client](/tutorial/03-rpc-client)**
    - How to set up and interact with `lnd` from an RPC client, specifically
      `gRPC`.
    - Exposure to `lnrpc` documentation
    - Set up web development workspace
- **[Stage 4 - Webapp Integration](/tutorial/04-webapp-integration)**
    - Adding a micropayments paywall
    - Recommended next steps
