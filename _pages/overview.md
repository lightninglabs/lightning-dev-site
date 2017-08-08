---
layout: page
title: Lightning Network Overview
permalink: /overview/
---

### Introduction

This page aims to provide *just* enough information about the Lightning Network
to enable readers to build applications. This page assumes basic knowledge of
Bitcoin mechanics. If terms like "UTXO" and "locktime" are unfamiliar to you,
you should refer to the [Bitcoin developer
guide](https://bitcoin.org/en/developer-guide), which serves a similar purpose.

### Lightning Network

The Lightning Network enables blockchains to scale by keeping most transactions
off-chain. It is an overlay network, leveraging the security of the underlying
blockchain as an arbitration layer.

The Lightning Network attains these properties in a fully trustless manner. This
is accomplished primarily through "payment-channels", which allows two parties
to commit funds and trustlessly update the balance redeemable by either party in the
channel. With Hash Time-Locked Contracs (HTLCs), payments can even be sent to
parties with whom there does not exist a direct payment channel, connecting the
entire Lightning Network into a single financial network.

By conducting the vast majority of payments off-chain, the cost of opening and
closing channels (in the form of on-chain transations fees) is ammortized,
enabling low-cost micropayments. Since payments are conducted off-chain, the
Lightning Network is constrained not by the transaction throughput of the
underlying blockchain but rather by modern data processing and latency limits.

Furthermore, because each payment is settled immediately upon receipt by the
recipient, the Lightning Network frees cryptocurrency users from having to wait
the typical 6 confirmations before rendering goods or services.  

In short, the Lightning Network enables scalable blockchains through a
high-volume of instant transactions not requiring custodial delegation.

### Payment Channels
