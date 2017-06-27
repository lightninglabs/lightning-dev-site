---
layout: page
title: LND Installation
permalink: /installation/
---

# Preliminaries
  In order to build from source, the following build dependencies are 
  required:
  
  * **Go:** Installation instructions can be found [here](http://golang.org/doc/install). 
  
    It is recommended to add `$GOPATH/bin` to your `PATH` at this point.
    **Note:** If you are building with `Go 1.5`, then you'll need to 
    enable the vendor experiment by setting the `GO15VENDOREXPERIMENT` 
    environment variable to `1`. If you're using `Go 1.6` or later, then
    it is safe to skip this step.

  * **Glide:** This project uses `Glide` to manage dependencies as well 
    as to provide *reproducible builds*. To install `Glide`, execute the
    following command (assumes you already have Go properly installed):
    ```
    $ go get -u github.com/Masterminds/glide
    ```
  * **btcd:** This project currently requires `btcd` with segwit support,
    which is not yet merged into the master branch. Instead,
    [roasbeef](https://github.com/roasbeef/btcd) maintains a fork with his
    segwit implementation applied. To install, please see 
    [the installation instructions](docs/INSTALL.md).

# Installation

With the preliminary steps completed, to install `lnd`, `lncli`, and all
related dependencies run the following commands:
```
$ git clone https://github.com/lightningnetwork/lnd $GOPATH/src/github.com/lightningnetwork/lnd
$ cd $GOPATH/src/github.com/lightningnetwork/lnd
$ glide install
$ go install . ./cmd/...
```

# Updating
To update your version of `lnd` to the latest version run the following 
commands:
```
$ cd $GOPATH/src/github.com/lightningnetwork/lnd
$ git pull && glide install
$ go install . ./cmd/...
```

# Tests
To check that `lnd` was installed properly run the following command:
```
go install; go test -v -p 1 $(go list ./... | grep -v  '/vendor/')
```

[//]: # (TODO Max: Update these links to point to the dev site instead of Github)

## Further reading
* [Step-by-step send payment guide with docker](https://github.com/lightningnetwork/lnd/tree/master/docker)
* [Contribution guide](https://github.com/lightningnetwork/lnd/blob/master/docs/code_contribution_guidelines.md)
