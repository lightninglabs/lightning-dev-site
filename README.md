# Lightning Network Daemon Developer Site
Developer guides and resources for the Lightning Network Daemon

## Running the site locally

Install Jekyll:
```
$ gem install jekyll bundler
```
Run the site and watch for changes:
```
$ bundle exec jekyll serve
```

### Regenerating documentation

```shell
# Install Jinja for python templating
pip install Jinja2
```

# Get the latest INSTALL.md
curl -o INSTALL.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/INSTALL.md

# Get the latest gRPC guides
curl -o python.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/python.md
curl -o javascript.md -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/docs/grpc/javascript.md

Let's run the script to render the guides:
```shell
python render.py
```

Now that you're all set up, you can just run `./update_and_render.sh` to
automatically pull the latest markdown files and render the local Jekyll docs

## Deployment

The Lightning Dev Site is deployed with `s3_website`. Visit their [github
repo](https://github.com/laurilehmijoki/s3_website) for more information.

### Steps

1. Install Google Cloud SDK and authenticate into it:
```bash
brew cask install google-cloud-sdk
gcloud auth login
```

2. Build
```bash
jekyll build
```

3. Push to Google Cloud Bucket
```bash
# -m use faster multithreaded uploads
# -d delete remote files that aren't in the source
# -r recurse into source subdirectories
gsutil -m rsync -d -r ./_site gs://dev.lightning.community
```

In the future, you can just run `./deploy.sh` to deploy automatically.
