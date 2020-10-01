# Lightning Network Daemon Developer Site
Developer guides and resources for the Lightning Network Daemon

## Overview

This repository contains functionality for programmatically pulling guides from
the lnd repo, using a Python script and Jinja2 templates to output markdown
files, which are the corresponding pages in the fully rendered Jekyll static
site. 

Pay special attention to these files:
- `templates/base.md`: The Jinja2 template fed into the Python
  script, holding the Jeykll header to be prepended to the guide content pulled
  from Github. The `templates` dir also holds the templates for special cases
  where for example a dev site-specific footer needs to be appended
- `update_and_render.sh`: Update local guides to the latest version available
- `render.py`: The Python script that uses local guides and Jinja template to
  strip out redundant titles, add page headers/footers, and output Jekyll
  markdown
- `deploy.sh`: Build static site from Jekyll markdown and deploy to Google Cloud
  Platform

The rest of the files in this repo are the standard Jekyll site files.

## Running the site locally

### Prerequisites

You're going to need:

 - **Linux or OS X** — Windows may work, but is unsupported.
 - **Ruby, version 2.2.5 or newer**
 - **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.

### Running locally

```shell
git clone https://github.com/lightninglabs/lightning-dev-site
```
Install Jekyll:
```
$ gem install jekyll bundler
```
Run the site and watch for changes:
```
$ bundle exec jekyll serve
```
* If running remotely add: `--host=0.0.0.0`


## Regenerating documentation

```shell
# Install Jinja for python templating
pip install Jinja2
```

### Get the latest INSTALL.md
```shell
curl -o INSTALL.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/INSTALL.md
```

### Fetch the latest Docker guide
```shell
curl -o DOCKER-README.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docker/README.md
```

### Get the latest gRPC guides
```shell
curl -o python.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/python.md
curl -o javascript.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/javascript.md
```

Let's run the script to render the guides:
```shell
python render.py
```

Now that you're all set up, you can just run `./update_and_render.sh` to
automatically pull the latest markdown files and render the local Jekyll docs.

## Deployment

The Lightning API is deployed with Google Cloud Platform. Visit [this blog
post](https://little418.com/2015/07/jekyll-google-cloud-storage.html) for more
information.

### Steps
So we have the following steps-

1. Install Google Cloud SDK and authenticate into it:
```bash
brew cask install google-cloud-sdk
gcloud auth login
```

2. Build
```bash
bundle exec jekyll build
```

3. Push to Google Cloud Bucket
```bash
# -m use faster multithreaded uploads
# -d delete remote files that aren't in the source
# -r recurse into source subdirectories
gsutil -m rsync -d -r ./_site gs://dev.lightning.community
```

In the future, you can just run `./deploy.sh` to deploy automatically.
Thank you!
