# Revese proxy using nginx

This image implements a reverse proxy functionality using `nginx`. Compared to the official image, we are adding our own custom configuration files. As such, this image is mostly specific to our particular setup. However, feel free to use it as an inspiration for other reverse-proxy setups.

This readme assumes you have `certificate_create.sh` and `certificate_renew.sh` somewhere on your Unraid server (`/mnt/user/appdata/certbot` is my default location). Furthermore, you should set up `certificate_renew.sh` to run at least once a month/week.

### Deployment

 - Map container port `80` and `443` to some suitable extenal ports (this must be some non-standard ports, because Unraid admin panel already uses `80` and `443`).
 - Make sure your router forwards any outside traffic on `80` and `443` to your server on your designated custom ports.
 
 > Another option is to use a custom network bridge which will give our container a separate IP address. In that case, you can use `80` and `443` directly, since it no longer collides with Unraid. But then you need to forward the traffic to the proper IP.
 
 - Map internal path `/var/www/certbot` to `/mnt/user/appdata/certbot`. This is the place where we save temporary files during certificate aquisition. Ideally, you also want to have `certificate_create.sh` and `certificate_renew.sh` here for future use.
 - Map internal path `/etc/nginx/ssh` to `/mnt/user/appdata/letsencrypt`. This is the place where `certbot` will save HTTPS certificates for us. As such, you can consider backing this up regularly.

### Adding a new server

 > This assumes you already have the proper DNS record and port forwarding set up for your domain and local network. Also, consider that your "local" DNS settings must be different because on your local network, the "global" settings just point to your router instead of the server (see `dnsmasq` docker).

 - Create a HTTP server in the corresponding `.conf` file inside `sites`. For example, see the first `server` object in `sites/sw.mtlrank.conf`. Just remeber to repace `mtlrank.software.unsigned-short.com` with your domain. 

  > Do not create the second (HTTPS) server yet: the config will not work without a valid certificate. 
 
 - Update `Dockerfile` and `nginx.conf` to include the new `.conf` file for your domain.
 - Rebuild the image and deploy it. 
 - If you don't want HTTPS, you are done.
 - Run `certificate_create.sh YOUR_DOMAIN` on the server (this should create new certificates in `/mnt/user/appdata/letsencrypt/` which is mapped to `/etc/nginx/ssl` in the container).
 - Now add the HTTPS end point: if you also want authentication through `authelia`, you can again use `sites/sw.mtlrank.conf` as a template. If you don't want authentication, simply remove all `authelia` related imports.

  > By default, our `authelia` container requires single-factor authentication for all endpoints and groups. If you want some other settings for your specific server, see the `authelia` image for instructions on how to change this.
