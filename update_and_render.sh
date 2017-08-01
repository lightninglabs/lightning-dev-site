#!/bin/bash

# Fetch the latest installation docs
curl -o INSTALL.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/INSTALL.md

# Fetch the latest RPC docs
curl -o python.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/python.md
curl -o javascript.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/javascript.md

# Render docs
python render.py

# Clean up
rm INSTALL.md
rm python.md
rm javascript.md
