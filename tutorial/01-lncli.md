---
layout: page
title: Stage 1 - Setting up a local cluster
---

### Introduction

In this stage of the tutorial, we will learn how to set up a local cluster of
nodes `Alice`, `Bob`, and `Charlie`, have them talk to each other, set up
channels, and route payments between one another. We will also establish a
baseline understanding of the different components that must work together as
part of developing on `lnd`.

This tutorial assumes you have completed installation of Go, `btcd`, and `lnd`
on simnet. If not, please refer to the [installation
instructions](/guides/installation/).

The schema will be the following. Keep in mind that you can easily extend this
network to include additional nodes `David`, `Eve`, etc. by simply running more
local `lnd` instances.

[//]: # (TODO Max: Replace this with an actual image)
```
   (1)                        (1)                         (1)
+ ----- +                   + --- +                   + ------- +
| Alice | <--- channel ---> | Bob | <--- channel ---> | Charlie |
+ ----- +                   + --- +                   + ------- +
    |                          |                           |
    |                          |                           |
    + - - - -  - - - - - - - - + - - - - - - - - - - - - - +
                               |
                      + --------------- +
                      | BTC/LTC network | <--- (2)
                      + --------------- +
```

### Understanding the components

#### LND

`lnd` is the main component that we will interact with. `lnd` stands for
Lightning Network Daemon, and handles channel opening/closing, routing and
sending payments, and managing all the Lightning Network state that is separate
from the underlying Bitcoin network itself.

Running an `lnd` node means that it is listening for payments, watching the
blockchain, etc. By default it is awaiting user input.

`lncli` is the command line client used to interact with your `lnd` nodes.
Typically, each `lnd` node will be running in its own terminal window, so that
you can see its log outputs. `lncli` commands are thus run from a different
terminal window.

#### BTCD

`btcd` represents the gateway that `lnd` nodes will use to interact with the
Bitcoin / Litecoin network. `lnd` needs `btcd` for creating on-chain addresses
or transactions, watching the blockchain for updates, and opening/closing
channels. In our current schema, all three of the nodes are connected to the
same `btcd` instance. In a more realistic scenario, each of the `lnd` nodes
will be connected to their own instances of `btcd` or equivalent.

We will also be using `simnet` instead of `testnet`. Simnet is a
development/test network run locally that allows us to generate blocks at will,
so we can avoid the time-consuming process of waiting for blocks to arrive for
any on-chain functionality.

### Setting up our environment

Developing on `lnd` can be quite complex since there are many more moving
pieces, so to simplify that process, we will walk through a recommended
workflow.

#### Running btcd

Let's start by running btcd, if you don't have it up already. Open up a new
terminal window, ensure you have your `$GOPATH` set, and run:
```bash
btcd --txindex --simnet --rpcuser=kek --rpcpass=kek
```

Breaking down the components:
  * `--txindex` is required so that the `lnd` client is able to query
    historical transactions from `btcd`.
  * `--simnet` specifies that we are using the `simnet` network. This can be
    changed to `--testnet`, or omitted entirely to connect to the actual Bitcoin
    / Litecoin network.
  * `--rpcuser` and `rpcpass` sets a default password for authenticating to the
    `btcd` instance.

#### Running lnd

Now, let's set up the three `lnd` nodes. To keep things as clean and separate
as possible, open up a new terminal window, ensure you have `$GOPATH` set and
`$GOPATH/bin` in your `PATH`, and create a new directory under `$GOPATH` called
`dev` that will represent our development space. We will create separate
folders to store the state for alice, bob, and charlie, and run all of our
`lnd` nodes on different `localhost` ports instead of using
[Docker](/guides/docker/) to make our networking a bit easier.

```bash
# Create our development space
cd $GOPATH
mkdir dev
cd dev

# Create folders for each of our nodes
mkdir alice bob charlie
```

The directory structure should now look like this:
```bash
$ tree $GOPATH -L 2

├── bin
│   └── ...
├── dev
│   ├── alice
│   ├── bob
│   └── charlie
├── pkg
│   └── ...
├── rpc
│   └── ...
└── src
    └── ...
```

Start up the Alice node from within the `alice` directory:
```bash
cd $GOPATH/dev/alice
alice$ lnd --rpclisten=localhost:10001 --listen=localhost:10011 --restlisten=localhost:8001 --datadir=test_data --logdir=test_log --debuglevel=info --no-macaroons --bitcoin.simnet --bitcoin.active --bitcoin.node=btcd --btcd.rpcuser=kek --btcd.rpcpass=kek 
```
The Alice node should now be running and displaying output.

Breaking down the components:
  * `--rpclisten`: The host:port to listen for the RPC server. This is the primary way
    an application will communicate with `lnd`
  * `--listen`: The host:port to listen on for incoming P2P
    connections. This is at the networking level, and is distinct from the
    Lightning channel networks and Bitcoin/Litcoin network itself.
  * `--restlisten`: The host:port exposing a REST api for interacting with `lnd` over
    HTTP. For example, you can get Alice's channel balance by making a GET
    request to `localhost:8001/v1/channels`. This is not needed for this
    tutorial, but you can see some examples
    [here](https://gist.github.com/Roasbeef/624c02cd5a90a44ab06ea90e30a6f5f0).
  * `--datadir`: The directory that `lnd`'s data will be stored inside
  * `--logdir`: The directory to log output.
  * `--debuglevel`: The logging level for all subsystems. Can be set to
    `trace`, `debug`, `info`, `warn`, `error`, `critical`.
  * `--no-macaroons`: Disable macaroon authentication for tutorial purposes.
  * `--bitcoin.simnet`: Specifies whether to use `simnet` or `testnet`
  * `--bitcoin.active`: Specifies that bitcoin is active. Can also include
    `--litecoin.active` to activate Litecoin.
  * `--bitcoin.node=btcd`: Use the `btcd` full node to interface with the blockchain.
    Note that when using Litecoin, the option is `--litecoin.node=btcd`.
  * `--btcd.rpcuser` and `--btcd.rpcpass`: The username and password for
    the `btcd` instance. Note that when using Litecoin, the options are `--ltcd.rpcuser`
    and `--ltcd.rpcpass`.

### Running Bob and Charlie

Just as we did with Alice, start up the Bob node from within the `bob`
directory, and the Charlie node from within the `charlie` directory. Doing so
will configure the `datadir` and `logdir` to be in separate locations so that
there is never a conflict.

Keep in mind that for each additional terminal window you set, you will need to
set `$GOPATH` and include `$GOPATH/bin` in your `PATH`. Consider creating a
setup script that includes the following lines:
```bash
export GOPATH=~/gocode # if you exactly followed the install guide
export PATH=$PATH:$GOPATH/bin
```
and run it every time you start a new terminal window working on `lnd`.

Run Bob and Charlie:
```bash
# In a new terminal window
cd $GOPATH/dev/bob
bob$ lnd --rpclisten=localhost:10002 --listen=localhost:10012 --restlisten=localhost:8002 --datadir=test_data --logdir=test_log --debuglevel=info --no-macaroons --bitcoin.simnet --bitcoin.active --bitcoin.node=btcd --btcd.rpcuser=kek --btcd.rpcpass=kek 

# In another terminal window
cd $GOPATH/dev/charlie
charlie$ lnd --rpclisten=localhost:10003 --listen=localhost:10013 --restlisten=localhost:8003 --datadir=test_data --logdir=test_log --debuglevel=info --no-macaroons --bitcoin.simnet --bitcoin.active --bitcoin.node=btcd --btcd.rpcuser=kek --btcd.rpcpass=kek
```

### Configuring lnd.conf

To skip having to type out a bunch of flags on the command line every time, we
can instead modify our `lnd.conf`, and the arguments specified therein will be
loaded into `lnd` automatically. Any additional configuration added as a
command line argument will be applied *after* reading from `lnd.conf`, and will
overwrite the `lnd.conf` option if applicable.

- On MacOS, `lnd.conf` is located at: `/Users/[username]/Library/Application\ Support/Lnd/lnd.conf`
- On Linux: `~/.lnd/lnd.conf`

Here is an example `lnd.conf` that can save us from re-specifying a bunch of
command line options:
```bash
[Application Options]
datadir=test_data
logdir=test_log
debuglevel=info
debughtlc=true
no-macaroons=true

[Bitcoin]
bitcoin.simnet=1
bitcoin.active=1
bitcoin.node=btcd

[btcd]
btcd.rpcuser=kek
btcd.rpcpass=kek
```

Now, when we start nodes, we only have to type
```bash
alice$ lnd --rpclisten=localhost:10001 --listen=localhost:10011 --restlisten=localhost:8001
bob$ lnd --rpclisten=localhost:10002 --listen=localhost:10012 --restlisten=localhost:8002
charlie$ lnd --rpclisten=localhost:10003 --listen=localhost:10013 --restlisten=localhost:8003
```
etc.

### Working with lncli

Now that we have our `lnd` nodes up and running, let's interact with them! To
control `lnd` we will need to use `lncli`, the command line interface.

Open up a new terminal window, set `$GOPATH` and include `$GOPATH/bin` in your
`PATH` as usual.

Let's test that we can connect to Alice by first creating her wallet and then
requesting basic information:

```bash
cd $GOPATH/dev/alice
alice$ lncli --rpcserver=localhost:10001 --no-macaroons create
```

You'll be asked to input the wallet password twice. You can now start requesting
some basic information as follows:

```bash
alice$ lncli --rpcserver=localhost:10001 --no-macaroons getinfo
```

`lncli` just made an RPC call to the Alice `lnd` node. Notice that we had to
specify the `--rpcserver` here, which corresponds to `--rpcport=10001` that we
set when starting the Alice `lnd` node.

#### lncli options

To see all the commands available for `lncli`, simply type `lncli --help` or
`lncli -h`.

### Setting up Bitcoin addresses

Let's create a new Bitcoin address for Alice. This will be the address that
stores Alice's on-chain balance.

```bash
alice$ lncli --rpcserver=localhost:10001 --no-macaroons newaddress np2wkh
{
    "address": <ALICE_ADDRESS>
}
```

Open up new terminal windows and do the same for Bob and Charlie. `alice$` or
`bob$` denotes running the command from the Alice or Bob `lncli` window
respectively.

```bash
# In a new terminal window, setting $GOPATH, etc.
cd $GOPATH/dev/bob
bob$ lncli --rpcserver=localhost:10002 --no-macaroons create

bob$ lncli --rpcserver=localhost:10002 --no-macaroons newaddress np2wkh
{
    "address": <BOB_ADDRESS>
}

# In a new terminal window:
cd $GOPATH/dev/charlie
charlie$ lncli --rpcserver=localhost:10003 --no-macaroons create

charlie$ lncli --rpcserver=localhost:10003 --no-macaroons newaddress np2wkh
{
    "address": <CHARLIE_ADDRESS>
}
```

To avoid typing the `--rpcserver=localhost:1000X` flag every time, we can set
some aliases. Add the following to your `.bashrc`:
```bash
alias lncli-alice="lncli --rpcserver=localhost:10001 --no-macaroons"
alias lncli-bob="lncli --rpcserver=localhost:10002 --no-macaroons"
alias lncli-charlie="lncli --rpcserver=localhost:10003 --no-macaroons"
```

To make sure this was applied to all of your current terminal windows, rerun
your `.bashrc` file:
```bash
alice$ source ~/.bashrc
bob$ source ~/.bashrc
charlie$ source ~/.bashrc
```
For simplicity, the rest of the tutorial will assume that this step was
complete.

### Funding Alice

That's a lot of configuration! Recall that at this point, we've generated
onchain addresses for Alice, Bob, and Charlie. Now, we will get some practice
working with `btcd` and fund these addresses with some `simnet` Bitcoin.

Quit btcd and re-run it, setting Alice as the recipient of all mining rewards:
```bash
btcd --simnet --txindex --rpcuser=kek --rpcpass=kek --miningaddr=<ALICE_ADDRESS>
```

Generate 400 blocks, so that Alice gets the reward. We need at least 100 blocks
because coinbase funds can't be spent until after 100 confirmations, and we
need about 300 to activate segwit.
window with `$GOPATH` and `$PATH` set.

```bash
btcctl --simnet --rpcuser=kek --rpcpass=kek generate 400
```

Check that segwit is active:
```bash
btcctl --simnet --rpcuser=kek --rpcpass=kek getblockchaininfo | grep -A 1 segwit
```

Check Alice's wallet balance. `--witness_only=true` specifies that we only want
to consider witness outputs when calculating the wallet balance.

```bash
alice$ lncli-alice walletbalance --witness_only=true
```

It's no fun if only Alice any money. Let's give some to Charlie as well:

```bash
# Quit btcd
btcd --txindex --simnet --rpcuser=kek --rpcpass=kek --miningaddr=<CHARLIE_ADDRESS>

# Generate more blocks
btcctl --simnet --rpcuser=kek --rpcpass=kek generate 100

# Check Charlie's balance
charlie$ lncli-charlie walletbalance --witness_only=true
```

### Creating the P2P Network
Now that Alice and Charlie have some simnet Bitcoin, let's start connecting
them together.

Connect Alice to Bob:
```bash
# Get Bob's identity pubkey:
bob$ lncli-bob getinfo
{
    ----->"identity_pubkey": <BOB_PUBKEY>,
    "alias": "",
    "num_pending_channels": 0,
    "num_active_channels": 0,
    "num_peers": 0,
    "block_height": 450,
    "block_hash": "2a84b7a2c3be81536ef92cf382e37ab77f7cfbcf229f7d553bb2abff3e86231c",
    "synced_to_chain": true,
    "testnet": false,
    "chains": [
        "bitcoin"
    ]
}

# Connect Alice and Bob together
alice$ lncli-alice connect <BOB_PUBKEY>@localhost:10012
{
    "peer_id": 0
}
```
Notice that `localhost:10012` corresponds to the `--peerport=10012` flag we set
when starting the Bob `lnd` node.

Let's check that Alice and Bob are now aware of each other.
```bash
# Check that Alice has added Bob as a peer:
alice$ lncli-alice listpeers
{
    "peers": [
        {
            "pub_key": <BOB_PUBKEY>,
            "peer_id": 1,
            "address": "127.0.0.1:10012",
            "bytes_sent": "292",
            "bytes_recv": "292",
            "sat_sent": "0",
            "sat_recv": "0",
            "inbound": true,
            "ping_time": "0"
        }
    ]
}

# Check that Bob has added Alice as a peer:
bob$ lncli-bob listpeers
{
    "peers": [
        {
            "pub_key": <ALICE_PUBKEY>,
            "peer_id": 1,
            "address": "127.0.0.1:60104",
            "bytes_sent": "318",
            "bytes_recv": "318",
            "sat_sent": "0",
            "sat_recv": "0",
            "inbound": false,
            "ping_time": "5788"
        }
    ]
}
```

Finish up the P2P network by connecting Bob to Charlie:

```bash
charlie$ lncli-charlie connect <BOB_PUBKEY>@localhost:10012
```

and testing their connections:

```bash
# Check that Charlie has added Bob as a peer:
charlie$ lncli-charlie listpeers

# Check that Bob has added Charlie as a peer
bob$ lncli-bob listpeers
```

### Setting up Lightning Network

Before we can send payment, we will need to set up payment channels from Alice
to Bob, and Bob to Charlie.

First, let's open the Alice<-->Bob channel.

```bash
alice$ lncli-alice openchannel --node_key=<BOB_PUBKEY> --local_amt=1000000
```

- `--local_amt` specifies the amount of Satoshi that Alice will commit to the
  channel.  To see the full list of options, you can try `lncli openchannel
  --help`.

We now need to mine six blocks so that the channel is considered valid:
```bash
btcctl --simnet --rpcuser=kek --rpcpass=kek generate 6
```

Check that Alice<-->Bob channel was created:

```bash
alice$ lncli-alice listchannels
{
    "channels": [
        {
            "active": true,
            "remote_pubkey": <BOB_PUBKEY>,
            "channel_point": "2622b779a8acca471a738b0796cd62e4457b79b33265cbfa687aadccc329023a:0",
            "chan_id": "495879744192512",
            "capacity": "1000000",
            "local_balance": "991312",
            "remote_balance": "0",
            "commit_fee": "8688",
            "commit_weight": "600",
            "fee_per_kw": "12000",
            "unsettled_balance": "0",
            "total_satoshis_sent": "0",
            "total_satoshis_received": "0",
            "num_updates": "0"
        }
    ]
}
```

### Sending single hop payments

Finally, to the exciting part - sending payments! Let's send a payment from
Alice to Bob.

First, Bob will need to generate an invoice:

```bash
bob$ lncli-bob addinvoice --value=100000
{
        "r_hash": "<a_random_rhash_value>",
        "pay_req": "<encoded_invoice>",
}
```

Send the payment from Alice to Bob:

```bash
alice$ lncli-alice sendpayment --pay_req=<encoded_invoice>
{
	"payment_preimage": "baf6929fc95b3824fb774a4b75f6c8a1ad3aaef04efbf26cc064904729a21e28",
	"payment_route": {
		"total_time_lock": 1,
		"total_amt": 100000,
		"hops": [
			{
				"chan_id": 495879744192512,
				"chan_capacity": 1000000,
				"amt_to_forward": 100000
			}
		]
	}
}

# Check that Alice's channel balance was decremented accordingly:
alice$ lncli-alice listchannels

# Check that Bob's channel was credited with the payment amount:
bob$ lncli-bob listchannels
```

### Multi-hop payments

Now that we know how to send single-hop payments, sending multi hop payments is
not that much more difficult. Let's set up a channel from Bob<-->Charlie:

```bash
charlie$ lncli-charlie openchannel --node_key=<BOB_PUBKEY> --local_amt=800000 --push_amt=200000

# Mine the channel funding tx
btcctl --simnet --rpcuser=kek --rpcpass=kek generate 6
```

Note that this time, we supplied the `--push_amt` argument, which specifies the
amount of money we want to other party to have at the first channel state.

Let's make a payment from Alice to Charlie by routing through Bob:

```bash
charlie$ lncli-charlie addinvoice --value=10000
alice$ lncli-alice sendpayment --pay_req=<encoded_invoice>

# Check that Charlie's channel was credited with the payment amount (e.g. that
# the `remote_balance` has been decremented by 10000)
charlie$ lncli-charlie listchannels
```

### Closing channels

For practice, let's try closing a channel. We will reopen it in the next stage
of the tutorial.

```bash
alice$ lncli-alice listchannels
{
    "channels": [
        {
            "active": true,
            "remote_pubkey": "0343bc80b914aebf8e50eb0b8e445fc79b9e6e8e5e018fa8c5f85c7d429c117b38",
       ---->"channel_point": "3511ae8a52c97d957eaf65f828504e68d0991f0276adff94c6ba91c7f6cd4275:0",
            "chan_id": "1337006139441152",
            "capacity": "1005000",
            "local_balance": "990000",
            "remote_balance": "10000",
            "unsettled_balance": "0",
            "total_satoshis_sent": "10000",
            "total_satoshis_received": "0",
            "num_updates": "2"
        }
    ]
}
```

The Channel point consists of two numbers separated by a colon, which uniquely
identifies the channel. The first number is `funding_txid` and the second
number is `output_index`.

```bash
# Close the Alice<-->Bob channel from Alice's side.
alice$ lncli-alice closechannel --funding_txid=<funding_txid> --output_index=<output_index>

# Mine a block including the channel close transaction to close the channel:
btcctl --simnet --rpcuser=kek --rpcpass=kek generate 1

# Check that Bob's on-chain balance was credited by his settled amount in the
# channel. Recall that Bob previously had no on-chain Bitcoin:
alice$ lncli-bob walletbalance
{
    "balance": "110001"
}
```

At this point, you've learned how to work with `btcd`, `btcctl`, `lnd`, and
`lncli`. In [Stage 2](/tutorial/02-web-client), we will learn how to set up and
interact with `lnd` using a web GUI client.

_In the future, you can try running through this workflow on `testnet` instead
of `simnet`, where you can interact with and send payments through the testnet
Lightning Faucet node. For more information, see the "Connect to faucet
lightning node" section in the [Docker guide](/guides/docker/) or check out the
[Lightning Network faucet
repository](https://github.com/lightninglabs/lightning-faucet)._

[//]: # (TODO Max: Replace the link to Github LN Faucet to an internal guide for interacting with the Lightning Faucet)

#### Navigation
- [Proceed to Stage 2 - Web Client](/tutorial/02-web-client)
- [Return to main tutorial page](/tutorial/)

### Questions
- Join the #dev-help channel on our [Community
  Slack](https://lightningcommunity.slack.com/join/shared_invite/enQtMjk0OTYxNzI4NzExLTFhZDA5YTYxZDU2YWQyOTQzN2ZkMzk3ZGUwNGM0NjE2NzQyNjAyZTkwOTFkZjJmMmMyNzlmNmE5YTRmMGFhM2Q)
- Join IRC:
  [![Irc](https://img.shields.io/badge/chat-on%20freenode-brightgreen.svg)](https://webchat.freenode.net/?channels=lnd)
