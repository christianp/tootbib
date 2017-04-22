A command-line tool to toot a random entry from [bib-site](https://github.com/christianp/bib-site).

Requires Python 3.

## To set up:

* Register a new app with the Mastodon instance: `tootbib register --mastodon <URL of your Mastodon instance>`
* Log in to Mastodon: `tootbib login --mastodon <URL of your Mastodon instance> --email <your Mastodon account's email address> --password <your Mastodon account's password>`

## To use:

`tootbib --api_base_url <URL of your Mastodon instance> --bibsite <URL of your bib-site instance>` will pick a random entry and create a toot.

## Other options:

* `--order <piece names separated by spaces>` - specify the order in which the pieces of the toot should be assembled. Default is `"title author collections abstract url pdf view"`
* `--appfile <filename>` - path to the file in which to store the token for your Mastodon app.
* `--userfile <filename>` - path to the file in which to store the access token for your Mastodon account.
