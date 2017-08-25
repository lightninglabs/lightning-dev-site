#!/bin/bash

# Fetch the latest installation docs
curl -o INSTALL.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/INSTALL.md
# cp ~/lightning/ln-lnd/src/github.com/lightningnetwork/lnd/docs/INSTALL.md .

# Fetch the latest Docker guide
curl -o DOCKER-README.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docker/README.md
# cp ~/lightning/ln-lnd/src/github.com/lightningnetwork/lnd/docker/README.md DOCKER-README.md

# Fetch the latest RPC docs
curl -o python.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/python.md
# cp ~/lightning/ln-lnd/src/github.com/lightningnetwork/lnd/docs/grpc/python.md .

curl -o javascript.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/javascript.md
# cp ~/lightning/ln-lnd/src/github.com/lightningnetwork/lnd/docs/grpc/javascript.md .

# Render docs
./render.py

# Clean up
rm INSTALL.md
rm python.md
rm javascript.md
rm DOCKER-README.md
