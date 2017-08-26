---
layout: page
title: Lightning Resources
permalink: /resources/
---

### Overview

This page is for those seeking to develop on LND or enhance their conceptual
understanding of the Lightning Network and associated technologies. It is not
comprehensive, but a careful study of the materials below should be sufficient
for anyone's needs.

If something important is missing, or you feel that additional resources or
links would be helpful, please email [Max
Fang](mailto:max@lightning.engineering) or message him on the Lightning
Community Slack.

### Lightning: Beginner

* [What is the Lightning Network and how can it help Bitcoin scale?](https://coincenter.org/entry/what-is-the-lightning-network)
  article by Elizabeth Stark
  * Accessible article explanation of the Lightning Network by Elizabeth Stark,
    the CEO of Lightning Labs.

* [The Blockchain and Us: Interview with Elizabeth Stark](https://www.youtube.com/watch?v=a3HulqfzyYE)
  * Quick 7 minute primer on the Lightning Network and its implications.

* [Joseph Poon discusses Lightning
  at Construct 2017](http://www.coindesk.com/events/construct-2017/videos/)
  (ctrl+f for "Lightning")
  * In-depth spoken explanation of the Lightning Network for the general
    audience. Note that this video requires providing CoinDesk an email address.

* ["Understanding the Lightning
  Network"](https://bitcoinmagazine.com/articles/understanding-the-lightning-network-part-building-a-bidirectional-payment-channel-1464710791/):
  Aaron van Wirdum's General Explainer Series
  * In-depth written explanation great for non-developers.
  * [Part 1](https://bitcoinmagazine.com/articles/understanding-the-lightning-network-part-building-a-bidirectional-payment-channel-1464710791/):
    Building a Bidirectional Bitcoin Payment Channel
  * [Part 2](https://bitcoinmagazine.com/articles/understanding-the-lightning-network-part-creating-the-network-1465326903/):
    Creating the Network
  * [Part 3](https://bitcoinmagazine.com/articles/understanding-the-lightning-network-part-completing-the-puzzle-and-closing-the-channel-1466178980/):
    Completing the Puzzle and Closing the Channel

### Lightning: Intermediate

* [Lightning Network Tech
  Talk](https://www.youtube.com/watch?v=wIhAmTqXhZQ) at Coinbase January
  2016
  * Spoken in-depth mechanics of bidirectional payment channels and multi-hop
    payments

* [Lightning Network](https://bitcoinmagazine.com/articles/understanding-the-lightning-network-part-building-a-bidirectional-payment-channel-1464710791/):
  Rusty Russell's Technical Explainer Series
  * In-depth explanation of Lightning, oriented towards developers.
  * [Part I](https://rusty.ozlabs.org/?p=450): Revocable Transactions
  * [Part II](https://rusty.ozlabs.org/?p=462): Hashed Timelock Contracts (HTLCs)
  * [Part III](https://rusty.ozlabs.org/?p=467): Channeling Contracts
  * [Part IV](https://rusty.ozlabs.org/?p=477): Summary

* [Lightning Network Paper](https://lightning.network/lightning-network-paper.pdf)
  published January 2016
  * The protocol has changed since this original paper, but covers the mid-level
    mechanics of the Lightning Network with an emphasis on the smart contracts
    that make it trustless
  * Combines the HTLC and channel update concepts together
  * Explains how the Lightning Network is represented in Bitcoin transaction
    based contracts, and how the Lightning Network works with the UTXO model.

* [Lightning Network Community Blog](http://lightning.community), managed by
  Lightning Labs.
  * Stay up to date with the latest about LND and the Lightning Network!

### Lightning: Advanced

* Read the code on Github: [`lnd`](https://github.com/lightningnetwork/lnd)

* [Basis Of Lightning
  Technology (BOLTs)](https://github.com/lightningnetwork/lightning-rfc/blob/master/00-introduction.md)
  * Full technical specification of the Lightning Network. BOLTs are the
    common standard enabling distinct, interoperable Lightning implementations.
  * [BOLT #0](https://github.com/lightningnetwork/lightning-rfc/blob/master/00-introduction.md):
    Introduction and Index
  * [BOLT #1](https://github.com/lightningnetwork/lightning-rfc/blob/master/01-messaging.md):
    Base Protocol
  * [BOLT #2](https://github.com/lightningnetwork/lightning-rfc/blob/master/02-peer-protocol.md):
    Peer Protocol for Channel Management
  * [BOLT #3](https://github.com/lightningnetwork/lightning-rfc/blob/master/03-transactions.md):
    Bitcoin Transaction and Script Formats
  * [BOLT #4](https://github.com/lightningnetwork/lightning-rfc/blob/master/04-onion-routing.md):
    Onion Routing Protocol
  * [BOLT #5](https://github.com/lightningnetwork/lightning-rfc/blob/master/05-onchain.md):
    Recommendations for On-chain Transaction Handling
  * [BOLT #6](https://github.com/lightningnetwork/lightning-rfc/blob/master/06-irc-announcements.md):
    Interim Node and Channel Discovery
  * [BOLT #7](https://github.com/lightningnetwork/lightning-rfc/blob/master/07-routing-gossip.md):
    P2P Node and Channel Discovery
  * [BOLT #8](https://github.com/lightningnetwork/lightning-rfc/blob/master/08-transport.md):
    Encrypted and Authenticated Transport
  * [BOLT #9](https://github.com/lightningnetwork/lightning-rfc/blob/master/09-features.md):
    Assigned Feature Flags
  * [BOLT #11](https://github.com/lightningnetwork/lightning-rfc/blob/master/11-payment-encoding.md):
    Invoice Protocol for Lightning Payments

* [Lightning Network Deep
  Dive](https://www.youtube.com/watch?v=b_szGaaPPFk) talk at SF Bitcoin Devs
  August 2016
  * Commitment scheme: Compact revocation derivation and storage
  * Revocation scheme: Pre-image derived revocation keys (homomorphic
    derivation)
  * Lightning Commitment Protocol: the fast link-layer protocol between two
    Lightning nodes
  * LND architecture

* [Lightning Network as a Directed Graph: Single-Funded Channel Network
  Topology](https://www.youtube.com/watch?v=-lgYYz3y_hY) talk at SF Bitcoin Devs
  April 2016 
  * Covers single funded channels and channel exhaustion
  * Covers how to construct sub-satoshi micropayments: "Pre-Image Length
    Probabilistic Payments"

* [Onion Routing in Lightning](https://youtu.be/Gzg_u9gHc5Q?t=2m47s) - Laolu
  Osuntokun at Scaling Bitcoin Milan 2016 (starts at 2:47)
  * A way to preserve privacy in the Lightning Network
  * [Video](https://youtu.be/Gzg_u9gHc5Q?t=2m47s),
    [transcript](https://scalingbitcoin.org/transcript/milan2016/onion-routing-in-lightning)

* [Outsourced Channel Monitoring](https://youtu.be/Gzg_u9gHc5Q?t=48m12s) - Tadge
  Dryja at Scaling Bitcoin Milan 2016 (starts at 48:12)
  * Outsourced channel monitoring: delegating the task of channel monitoring to
    a semi-trusted peer
  * [Video](https://youtu.be/Gzg_u9gHc5Q?t=48m12s), [slides](https://scalingbitcoin.org/milan2016/presentations/D1%20-%208%20-%20Tadge%20Dryja.pdf), [transcript](https://scalingbitcoin.org/transcript/milan2016/unlinkable-outsourced-channel-monitoring)

### LND Developer Tools

* [Developer Guides](/guides/)
  * Guides walking you through installation, docker setup, Python / Javascript
    gRPC, and more
* [API documentation](https://api.lightning.community)
  * API Reference documentation for the Lightning Network Daemon
* Lightning Faucet for [Bitcoin testnet](https://faucet.lightning.community/) or
  [Litecoin testnet](https://ltc.faucet.lightning.community/)
  * To read more, build from source, or deploy your own faucet see the [Github
    repository](https://github.com/lightninglabs/lightning-faucet)
* [LND Web Dashboard](https://github.com/mably/lncli-web)
  * A web client and dashboard made by Francis Mably. Useful as a more
    customizable client or as a starting point for a Lightning project
* [Lightning Apps and the Emerging Developer Ecosystem on LND](http://lightning.community/software/lnd/lightning/2017/07/05/emerging-lightning-developer-ecosystem/)
  * A survey of existing apps built on Lightning, as of July 2017. Potentially
    useful as inspiration or code examples
* Neutrino: A Bitcoin Light Client used in LND
  * [Compact Client Side Filtering for Light Clients](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-June/014474.html)
    on Bitcoin Dev Mailing List
  * [Neutrino BIP (Bitcoin Improvement Proposal)](https://github.com/Roasbeef/bips/blob/master/gcs_light_client.mediawiki)
  * [Github repository](https://github.com/lightninglabs/neutrino)

### LND Community

* LND Community Slack
  * Come here to meet the Lightning community, ask for help, and hang out!
  * [invite link](https://join.slack.com/t/lightningcommunity/shared_invite/MjI4OTg3MzQ4MjI2LTE1MDMxNzM1NTMtNjlmOGYzOTI1Ng)

* [#lnd](https://webchat.freenode.net/?channels=lnd) IRC
  * [![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lnd)

* [#lightning-dev](https://webchat.freenode.net/?channels=lightning-dev) IRC
  * [![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lightning-dev)
