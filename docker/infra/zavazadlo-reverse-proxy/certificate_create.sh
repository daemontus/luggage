#!/bin/sh

# https://mindsers.blog/post/https-using-nginx-certbot-docker/

docker run -it --rm --name certbot \
	-v "/mnt/user/appdata/letsencrypt:/etc/letsencrypt" \
	-v "/mnt/user/appdata/certbot:/var/www/certbot" \
	certbot/certbot certonly \
	--webroot --webroot-path /var/www/certbot \
	-d $1