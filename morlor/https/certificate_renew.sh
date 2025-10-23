#!/bin/sh

# https://mindsers.blog/post/https-using-nginx-certbot-docker/

docker run --rm --name certbot \
	-v "/root/data/letsencrypt:/etc/letsencrypt" \
	-v "/root/data/certbot:/var/www/certbot" \
	certbot/certbot renew \
	--webroot --webroot-path /var/www/certbot

docker restart reverse-proxy