---
layout: page
title: Lightning App Directory
permalink: /lapps/
---

### Introduction

This page lists wallets and Lightning apps ("lapps") built on LND, along with several
compatible apps built on Eclair and c-lightning.

### Wallets

* [Lightning App](https://github.com/lightninglabs/lightning-app) by Lightning Labs:
  a cross-platform wallet powered by `lnd`. See the announcement for
  [desktop](https://blog.lightning.engineering/announcement/2019/04/23mainnet-app.html)
  and [mobile](https://blog.lightning.engineering/announcement/2019/06/19/mobile-app.html)
  for more information. Checkout the [code](https://github.com/lightninglabs/lightning-app)
  and find the releases for
  [desktop](https://github.com/lightninglabs/lightning-app/releases),
  [Android](https://play.google.com/apps/testing/engineering.lightning.LightningMainnet)
  and [iOS](https://testflight.apple.com/join/xx23MrBp).  
<img src="/assets/lapps/lnd_desktop_app.png" alt="Screenshot of Lightning Desktop App" style="max-width: 80%;"/>

* [Zap](https://zap.jackmallers.com/) Wallet by Jack Mallers: a mobile and desktop app focused on ease of
  use and general user experience. Check out the [Zap website](https://zap.jackmallers.com/) or read the code on
  [GitHub](https://github.com/LN-Zap).  
<img src="/assets/lapps/zap.png" alt="Zap Wallet payment request view" style="max-width: 80%;"/>

* [HTLC.me](https://htlc.me/): Hosted wallet great for quickly trying out
  Lightning payments on the Bitcoin testnet.
* [ZeusLN](https://zeusln.app/):
  A mobile Bitcoin app for Lightning Network Daemon (lnd) node operators. Runs on Android and iOS.
* [Breez](https://breez.technology/): Breez is a Lightning Network mobile client and a hub.
  It provides a platform for simple, instantaneous bitcoin payments. Supports Android and iOS.

### Integrations

* [Bitrefill](https://en.bitrefill.com/): Recharge prepaid phone cards with
  Bitcoin and Litecoin
* [Y'alls](http://yalls.org/): Read and write articles, with Lightning Network
  micropayments  
<img src="/assets/lapps/yalls.png" alt="Screenshot of Yalls home view" style="max-width: 50%;"/>
* [LNCast](http://lncast.com/): Lightning Network Podcasts
* [Bard](https://www.bard.fun/): Simple paywall for watching a music visualizer
* [HodlHodl.com](https://hodlhodl.com/?set_asset=btcln): Peer-to-peer cryptocurrency
  exchange with Lightning integration
* [Zigzag.io](https://zigzag.io/#/): Cryptocurrency trading using Lightning
  (custodial)
* [lntxbot](https://telegram.me/lntxbot) Lightning integration to Telegram with
  tipping, send and receive and satellite API usage (custodial)
* [paywall.link](https://paywall.link/) Put any website behind a paywall and pay with Lightning

### Lightning network explorers

* [1ml.com](https://1ml.com/)
* [explore.casa](https://explore.casa/)
* [explorer.acinq.co](https://explorer.acinq.co/)
* [ln.alhur.es](https://ln.alhur.es/)

### Protocol Services

* [Lightning Faucet](https://faucet.lightning.community/): Receive free testnet
  Bitcoin
* [lnd.fun](http://lnd.fun/): Panel for webmasters to manage their full lightning node  
<img src="/assets/lapps/lnd.fun.png" alt="Screenshot of lnd.fun dashboard home view" style="max-width: 50%;"/>

### Developer Tools
* [ION](https://ion.radar.tech/): A comprehensive set of resources for users to join the Lightning Network.
* [WooCommerce
  Plugin](https://github.com/joaodealmeida/woocommerce-gateway-lightning):
  Gateway plugin to accept Lightning payments at WooCommerce stores
* [LND Explorer](https://demo1.lndexplorer.com/): demo for a web interface for
  LND. Code on [Github](https://github.com/altangent/lnd-explorer)
* [Light-weight LND Dashboard](https://github.com/mably/lncli-web): A
  lightweight web client for LND
* [LightningJ](http://www.lightningj.org/): A project intending to simplify the
  integration of Lightning implementations for Java developers, containing
  simple to use API implementations and converters between JSON and XML.

### Tipping
* [LightningTip](https://github.com/michael1011/lightningtip): Library to accept
  tips via the Lightning Network
* [Slack tipbot](https://github.com/CryptoFR/ln-tip-slack): Custodial Slack
  tipbot
* [LightningPay-PHP](https://github.com/robclark56/lightningPay-PHP): PHP plugin
  for eCommerce website to add _Pay by Lightning_ to accept order payments via the
  Lightning Network. 
* [Tippin.me](https://tippin.me/) LN tips integrated to Twitter (custodial)
* [Lightning Gifts](https://lightning.gifts/) Create fee-less Bitcoin gift
  vouchers to share with friends, family, and your haters. Powered by the Lightning Network ⚡

### Gaming
* [Lightning Gem](https://lightninggem.com/): Betting game using Lightning for
  payments
* [Kriptode.com](https://kriptode.com/) Lightning based games and more.
* [Satoshis.place](https://satoshis.place/) Internet graffiti paid with Lightning

### Physical applications
* [Ben Arc](https://twitter.com/BTCSocialist)'s various [projects](https://github.com/arcbtc/)
based on Arduino, ESP32 and the M5Stack.
  * [M5StackSats](https://github.com/arcbtc/M5StackSats):
    A bitcoin point of sale terminal using the ESP32 based M5Stack 
  * [Physically faucet](https://github.com/arcbtc/physically-faucet):
    A Lightning Network bitcoin faucet using the <http://lightning.gifts> api
  * [Flux capacitor](https://github.com/arcbtc/flux-capacitor):
    A dynamic Lightning Network point of sale device
  * [The Fossa](https://github.com/arcbtc/The-Fossa):
    The Free and Open Source Software (FOSS) ATM, dump that stinky loose fiat change for glorious sats!
* [LightningATM](https://github.com/21isenough/LightningATM):
  This ATM accepts coins and sends bitcoin over the Lightning Network

### Eclair Lapps

Eclair is a Scala implementation of the Lightning Network built by [ACINQ](https://acinq.co/)

* [Eclair](https://github.com/ACINQ/eclair) app: on
  [desktop](https://github.com/ACINQ/eclair/releases) and
  [Android](https://play.google.com/store/apps/details?id=fr.acinq.eclair.wallet.mainnet2)
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
  * [Nanopos](https://github.com/ElementsProject/nanopos): A simple
    point-of-sale system for fixed-price goods
  * [FileBazaar](https://github.com/ElementsProject/filebazaar): A system for
    selling files such as documents, images, and videos
  * [Lightning Publisher for
    WordPress](https://github.com/ElementsProject/wordpress-lightning-publisher):
    A patronage model for unlocking WordPress blog entries
  * [Paypercall](https://github.com/ElementsProject/paypercall): A programmer’s
    toolkit for Lightning that enables micropayments for individual API calls
  * [Ifpaytt](https://github.com/ElementsProject/ifpaytt): An extension of
    paypercall that allows web developers using IFTTT to request payments for
    service usage
  * [Lightning Jukebox](https://github.com/ElementsProject/lightning-jukebox):
    A fun demo that reimagines a classic technology for the Lightning Network
  * [Nanotip](https://github.com/ElementsProject/nanotip): The simple tip jar,
    rebuilt to issue Lightning Network invoices
* [Elaine Ou's projects](https://elaineou.com/shop/): 
  * [Lightning-powered vending machine](https://github.com/elaineo/Jellybean)
  * [Bitcoin-payable Twitter bot with Lightning Charge](https://github.com/elaineo/lightningbot)
  * [Twitter relay for Lightning JSON-RPC interface](https://github.com/elaineo/LightningBuddy)

### Requests

If you would like a Lightning app considered for this page, please send a
link and a one sentence description to <hello@lightning.engineering>.
If applicable, please specify which Lightning implementation it is built on.
