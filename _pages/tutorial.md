---
layout: page
title: Tutorial
permalink: /tutorial/
---

# Overview

This tutorial will get you up to speed with all the skills necessary to work
with `lnd`. We will be building a Bitcoin micropayments paywell into a news
site!

This tutorial assumes you have completed installation of Go, `btcd`, and `lnd`
on simnet.  If not, you can find the installation instructions
[here](/installation/).

# Stages

Each of the different stages of this tutorial is oriented towards a specific
skill. Beginners should start at [stage 1](/tutorial/01-lncli). Otherwise, jump
wherever you want below!

- **[Stage 1 - Setting up a local cluster](/tutorial/01-lncli)**
    - How to set up a local environment with three nodes that can make payments
      with and through one another.
    - Gain experience interacting with `lnd` from the command line.
- **[Stage 2 - LND Web Client](/tutorial/02-web-client)**
    - How to run and use a `lnd` web GUI.
- **[Stage 3 - RPC Client](/tutorial/03-rpc-client)**
    - How to set up and interact with `lnd` from an RPC client, specifically
      `gRPC`.
- **[Stage 4 - Webapp Integration](/tutorial/04-rpc-client)**
    - Authenticating into a server using `lnd`
    - Exposure to `lnrpc` documentation
    - Adding a micropayments paywall.
    - Recommended next steps
