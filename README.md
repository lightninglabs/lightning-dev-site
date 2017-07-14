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

## Deployment

The Lightning Dev Site is deployed with `s3_website`. Visit their [github
repo](https://github.com/laurilehmijoki/s3_website) for more information.

### Steps

1. Install `s3_website`
```bash
gem install s3_website
```

2. Add the deployment credentials for `s3_config.yml`
```
export LN_S3_ID="YOUR_S3_ID"
export LN_S3_SECRET="YOUR_S3_SECRET"
export LN_CLOUDFRONT_DISTRIBUTION_ID="YOUR_CLOUDFRONT_DISTRIBUTION_ID"
```

3. Deploy the site from local changes:

```
s3_website push
```
