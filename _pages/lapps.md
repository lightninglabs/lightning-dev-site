---
layout: page
title: Lightning App Directory
permalink: /lapps/
---

### Introduction

This page lists wallets and Lightning apps ("lapps") built on LND, along with several
compatible apps built on Eclair and c-lightning.

### Wallets

#### [Lightning Desktop App](https://github.com/lightninglabs/lightning-app) by Lightning Labs:

The Lightning Desktop App is a cross-platform wallet powered by `lnd`. This
application is temporarily down as we upgrade it to be compliant with the LND
beta release. See the [original
announcement](https://blog.lightning.engineering/announcement/2017/10/12/test-blitz.html)
for more information, or checkout the
[code](https://github.com/lightninglabs/lightning-app) or
[releases](https://github.com/lightninglabs/lightning-app/releases) <img
src="/assets/lapps/lnd_desktop_app.png" alt="Screenshot of Lightning Desktop App
Channel View" style="max-width: 80%;"/>

#### [Zap](https://zap.jackmallers.com/) Wallet by Jack Mallers
Currently in Beta, the Zap wallet is a mobile and desktop app focused on ease of
use and general user experience.
Check out the [Zap website](https://zap.jackmallers.com/) or read the code on
[Github](https://github.com/lightninglabs/lightning-app/releases) 

<img src="/assets/lapps/zap.png" alt="Zap Wallet payment request view" style="max-width: 80%;"/>

* [HTLC.me](https://htlc.me/): Hosted wallet great for quickly trying out
  Lightning payments on the Bitcoin testnet.

### Integrations

* [Bitrefill](https://en.bitrefill.com/): Recharge prepaid phone cards with
  Bitcoin and Litecoin
* [Y'alls](http://yalls.org/): Read and write articles, with Lightning Network
  micropayments
  <img src="/assets/lapps/yalls.png" alt="Screenshot of Yalls home view" style="max-width: 50%;"/>
* [LNCast](http://lncast.com/): Lightning Network Podcasts
* [Block & Jerry's](http://www.blockandjerrys.fun/): Virtual ice cream shop
* [adWatcher Microservice](http://adwatcher.hopto.org:7777/): Earn satoshis by
  watching ads or video content
* [Bard](https://www.bard.fun/): Simple paywall for watching a music visualizer
* [CoinMall](https://coinmall.com/): Buy & sell digital products with
  cryptocurrencies. 
* [Free DNS Demo](http://freedns.lightning-network.ro/): Purchase subdomains
  with off-chain payments.
* [Zigzag](http://zigzag.bitlum.io/): Cryptocurrency trading using Lightning
  (custodial)

### Protocol Services

* [Lightning Faucet](httos://faucet.lightning.community/): Receive free testnet
  Bitcoin (or [Litecoin](https://ltc.faucet.lightning.community/))
* [lnd.fun](http://lnd.fun/): Panel for webmasters to manage their full lightning node.
  <img src="/assets/lapps/lnd.fun.png" alt="Screenshot of lnd.fun dashboard home view" style="max-width: 50%;"/>
* [kibana](https://stats.preimage.net/): Visualization of the Lightning Network
* [1ML](https://1ml.com/): Lightning Network search and analysis engine

### Developer Tools
* [ION](https://ion.radar.tech/):ION provides a comprehensive set of resources for users to join the Lightning Network
* [WooCommerce
  Plugin](https://github.com/joaodealmeida/woocommerce-gateway-lightning):
  Gateway plugin to accept Lightning payments at WooCommerce stores, built on
  LND
* [LND Explorer](https://demo1.lndexplorer.com/): demo for a web interface for
  LND. Code on [Github](https://github.com/altangent/lnd-explorer)
* [Light-weight LND Dashboard](https://github.com/mably/lncli-web): A
  lightweight web client for LND.
* [LightningJ](http://www.lightningj.org/): A project intending to simplify the
  integration of Lightning implementations for Java developers, containing
  simple to use API implementations and converters between JSON and XML.

### Tipping
* [LightningTip](https://github.com/michael1011/lightningtip): Library to accept
  tips via the Lightning Network
* [Slack tipbot](https://github.com/CryptoFR/ln-tip-slack): Custodial Slack
  tipbot
* [CoinTippy](http://cointippy.com/): Custodial tip bot available on
  multiple platforms, including Reddit, Twitter, and Telegram.

### Gaming
* [Hammercoin](https://hammerco.in/): A role-playing game using Lightning for
  in-game payments
* [Sarutobi](https://play.google.com/store/apps/details?id=com.mandelduck.sarutobi):
  A game with Bitcoin and blockchain-based game items. [Release
  announcement](https://blog.indiesquare.me/sarutobi-android-release-and-cross-game-promotion-through-tokens-59a1c58cc7b1#.eaa1svobj)
* [Bitquest](http://bitquest.co/): The first Minecraft server denominated in
  cryptocurrency. [CoinJournal
  article](https://coinjournal.net/you-can-go-on-a-digital-treasure-hunt-for-bitcoin-in-minecraft/)
* [Lightning Gem](https://lightninggem.com/): Betting game using Lightning for
  payments
* [Thunderdice](http://thunderdice.ws/): Off-chain SatoshiDice

  <img src="/assets/lapps/thunderdice.png" alt="Screenshot of Thunder Dice Homepage" style="max-width: 50%;"/>

### Eclair Lapps

Eclair is a Scala implementation of the Lightning Network built by [ACINQ](https://acinq.co/)

* [Eclair](https://github.com/ACINQ/eclair) app: on
  [desktop](https://github.com/ACINQ/eclair/releases) and
  [Android](https://play.google.com/store/apps/details?id=fr.acinq.eclair.wallet)
* [Starblocks](https://starblocks.acinq.co/#/): Virtual coffee shop
* [Strike](https://strike.acinq.co/#/): Stripe-like Lightning payment aggregator
  API (custodial)
* [Lightning Conductor](http://lightningconductor.net/): A service for
  converting Lightning balances to BTC and back without having to close
  or open channels, currently on testnet.

### c-Lightning Lapps

c-lightning is a specification-compliant LN implementation in C, under the
[Elements Project](https://elementsproject.org/)

* [Blockstream store](https://store.blockstream.com/) (mainnet): Bitcoin
  paraphernalia that can only be purchased over LN.
* [Lightning Charge](https://github.com/ElementsProject/lightning-charge): A
  drop-in solution for accepting lightning payments
* [WooCommerce
  Plugin](https://github.com/ElementsProject/woocommerce-gateway-lightning):
  Original c-lightning version of the Gateway plugin to accept Lightning
  payments at WooCommerce stores, based on Lightning Charge.
* [Week of
  Lapps](https://blockstream.com/2018/03/29/blockstreams-week-of-lapps-ends.html)
   built on Lightning Charge by Nadav Idgi.
  * [Nanopos](https://github.com/ElementsProject/nanopos) — A simple
    point-of-sale system for fixed-price goods
  * [FileBazaar](https://github.com/ElementsProject/filebazaar) — A system for
    selling files such as documents, images, and videos
  * [Lightning Publisher for
    WordPress](https://github.com/ElementsProject/wordpress-lightning-publisher)
    — A patronage model for unlocking WordPress blog entries
  * [Paypercall](https://github.com/ElementsProject/paypercall) — A programmer’s
    toolkit for Lightning that enables micropayments for individual API calls
  * [Ifpaytt](https://github.com/ElementsProject/ifpaytt) — An extension of
    paypercall that allows web developers using IFTTT to request payments for
    service usage
  * [Lightning Jukebox](https://github.com/ElementsProject/lightning-jukebox) —
    A fun demo that reimagines a classic technology for the Lightning Network
  * [Nanotip](https://github.com/ElementsProject/nanotip) — The simple tip jar,
    rebuilt to issue Lightning Network invoices
* [BitcoinLightning.shop](https://bitcoinlightning.shop): Shop with Bitcoin
  Lightning, built on BTCPay and the c-lightning WooCommerce Plugin
* [Elaine Ou's Twitter bot](https://elaineou.com/shop/): Pay for likes,
  retweets, and follows

### Requests

If you would like your Lightning app considered for this page, please email a
link and one sentence description of your app to
[max@lightning.engineering](mailto:max@lightning.engineering). If applicable,
please specify which Lightning implementation it is built on.
