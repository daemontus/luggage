#!/bin/sh

# https://mindsers.blog/post/https-using-nginx-certbot-docker/

docker run -it --rm --name certbot \
	-v "/root/data/letsencrypt:/etc/letsencrypt" \
	-v "/root/data/certbot:/var/www/certbot" \
	certbot/certbot certonly \
	--webroot --webroot-path /var/www/certbot \
	-d $1