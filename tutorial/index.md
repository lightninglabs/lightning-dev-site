---
layout: page
title: Tutorial
---

# Overview

This tutorial will get you up to speed with all the skills necessary to work
with [`lnd`](https://github.com/lightningnetwork/lnd). We will be building a
Bitcoin micropayments paywell into a news site!

This tutorial assumes you have completed installation of Go, `btcd`, and `lnd`
on simnet.  If not, please see the [installation instructions](/guides/installation/).

# Stages

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
