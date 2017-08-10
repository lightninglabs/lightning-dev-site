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

The Lightning Network scales blockchains and enables trustless instant payments
by keeping most transactions off-chain and leveraging the security of the
underlying blockchain as an arbitration layer.

This is accomplished primarily through "payment-channels", wherein two parties
commit funds and pay each other by updating the balance redeemable by either
party in the channel. This process is instant and saves users from having to
wait for block confirmations before they can render goods or services.

Payment channels are trustless, since any attempt to defraud the current
agreed-upon balance in the channel results in the complete forfeiture of funds
by the liable party.

By moving payments off-chain, the cost of opening and closing channels (in the
form of on-chain transaction fees) is ammortized over the volume of payments in
that channel, enabling micropayments and small-value transactions for which the
on-chain transaction fees would otherwise be too expensive to justify.
Furthermore, the Lightning Network scales not with the transaction throughput of
the underlying blockchain, but with modern data processing and latency limits -
payments can be made nearly as quickly as packets can be sent.

Hash Time-Locked Contracts (HTLCs) allow transactions to be sent between parties
who do not have a direct channels by routing it through multiple hops, so anyone
connected to the Lightning Network is part of a single, interconnected global
financial system.

In short, the Lightning Network enables scalable blockchains through a
high-volume of instant transactions not requiring custodial delegation.

### Payment Channels

Payment channels are the main workhorse of the Lightning Network. They allow
multiple transactions to be aggregated into just a few on-chain transactions.

In the vast majority of cases, someone only needs to broadcast the first and
last transaction in the channel.
- The Funding Transaction creates the channel. During this stage, funds
  are sent into a multisig address controlled by both Alice and Bob, the
  counterparties to the channel. This address can be funded as a single-payer
  channel or by both Alice and Bob.
- The Closing Transaction closes the channel. When broadcast, the multisig
  address spends the funds back to Alice and Bob according to their agreed-upon
  channel amount.

In the case where either party attempts to defraud the other, a third
transaction, which punishes the attacker, will end up being broadcasted
on-chain. Let's investigate how this is possible by the way Lightning does
channel updates.

#### Channel Updates

In between the opening and closing transactions broadcast to the blockchain,
Alice and Bob can create a near infinite number of intermediate closing
transactions that gives different amounts to the two parties.

For example, if the initial state of the channel credits both Alice and Bob with
5BTC out of the 10BTC total contained in the multisig address, Alice can make a
1BTC payment to Bob by updating the closing transaction to pay 4BTC/6BTC, where
Alice is credited with 4BTC and Bob with 6BTC. Alice will give the signed
transaction to Bob, which is equivalent to payment, because Bob can broadcast it
at any time to claim his portion of the funds. Similarly, Alice is also able to
broadcast the closing transaction at any time to claim her funds.

To prevent an attack where Alice voids her payment by broadcasting the initial
state of 5BTC/5BTC, there needs to be a way to revoke prior closing
transactions. Payment revocation roughly works like the following.

When Alice broadcasts a closing transaction to the blockchain, she is attesting
to the current state of the chain. But since there may be millions of closing
transactions in a channel, all of which are valid, the blockchain itself can't
tell if what Alice attested to was indeed the correct state. Therefore, Alice
must wait 3 days after broadcasting the closing transaction before she can
redeem her funds. During this time, Bob is given a chance to reveal a secret
that will allow him to sweep Alice's funds immediately. Alice can thus revoke
her claim to the money in some state by giving Bob the secret to the closing
transaction. This allows Bob to take all of Alice's money, but only if Alice
attest to this old state by broadcasting the corresponding closing transaction
to the blockchain.

Channel updates are thus fully trustless. When making an update, both parties
exchange the secrets for the prior state, so that all prior states will have
been revoked except for the current state. Both parties will never broadcast an
old state, because they know the other party can take all their money if they
do so.

### Multihop payments

Single channels work well if you have a financial relationship with some entity
where you make payments frequently or in metered amounts. But most payments,
like purchasing an umbrella from a corner store because you lost it again, are
one-off. For Lightning to help Bitcoin scale in general use cases, there needs
to be a way for the whole network to forward payments through channels that
already exist. Furthermore, we want it such that this process retains the
trustless nature of individual channels, otherwise it becomes too hard to
identify dishonest actors amongst a large number of hops.

Once you don't have to trust the intermediaries, you no longer even care who
they are. This allows Lightning nodes to be fully anonymous, which is a huge win
for privacy.

Concretely, Suppose Alice has a channel with Bob, who has a channel with
Charlie, who has a channel with Dave: `A<->B<->C<->D`. How can
Alice pay Dave? 

Alice first notifies Dave that she wants to send him some money.

In order for Dave to accept this payment, he must generate a random number `R`.
He keeps `R` secret, but hashes it and gives the hash `H` to Alice.

Alice tells Bob: "I will pay you if you can produce the preimage of `H` within 3
days." In particular, she signs a transaction where for the first three days
after it is broadcast, only Bob can redeem it with knowledge of R, and
afterwards it is redeemable only by Alice. This transaction is called a Hash
Time-Locked Contract (HTLC) and allows Alice to make a conditional promise to
Bob while ensuring that her funds will not be accidentally burned if Bob never
learns what R is. She gives this signed transaction to Bob, but neither of them
broadcast it, because they are expecting to clear it out later.

Bob, knowing that he can pull funds from Alice if he knows R, now has no issue
telling Charlie: "I will pay you if you can produce the preimage of H within *2*
days."

Charlie does the same, making an HTLC that will pay Dave if Dave can produce R
within 1 day. However, Dave does in fact know R. Because Dave is able to pull
the desired amount from Charlie, Dave can consider the payment from Alice
completed. Now, he has no problem telling R to Charlie and Bob so that they are
able to collect their funds as well.

Now, everyone can clear out, because they have a guaranteed way to pull their
deserved funds by broadcasting these HTLCs off chain. They would prefer not to
do that though, since broadcasting on-chain is more expensive, and instead
settle each of these hops off chain. Alice knows that Bob can pull funds from
her since he has `R`, so she tells Bob: "I'll pay you, regardless of `R`, and in
doing so we'll terminate the HTLC so we can forget about R." Bob does the same
with Charlie, and Charlie with David.

Now, what if Dave is uncooperative and refuses to give `R` to Bob and Charlie?
Note that Dave must broadcast the transaction from Charlie within 1 day, and in
doing so must reveal R in order to redeem the funds. Bob and Charlie can simply
look at the blockchain to determine what R is and settle off-chain as well.

We have shown how to make a payment across the Lightning Network using only
off-chain transactions, without requiring direct channel links or trusting any
intermediaries. As long as there is a path from the payer to the payee, payments
can be routed, just like the Internet.
