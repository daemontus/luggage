# Morlor Cloud Gateway

Morlor is a small VM running in Hetzner cloud responsible for routing requests from "the open internet" towards our infrastructure. Morlor also stores the small amount of data (`/root/data`) needed for working HTTPS and OIDC user authentication.

## HTTPS

Morlor also manages all HTTPS certificates. Ideally, we would use the ACME support built into `nginx`, but we will need to share the certificates across several devices that will handle requests from federated LANs. As such, it must be possible to sync certificates to these devices, since they can't use normal provisioning.

The certificates are managed by `certbot` and stored in `/root/data/letsencrypt`. To create a certificate, simply run:

```
./https/certificate_create.sh some.domain.com
```

The certificates needs to be renewed monthly, and *`nginx` needs to be restarted every time the certificate changes*. This is handled by the `certificate_renew.sh` script, which will also restart the `reverse-proxy` container. To run the script periodically, add the following cron entry (run `crontab -e` to edit):

```
0 0 * * 1 /root/luggage/morlor/https/certificate_renew.sh
```

## Services



## VM Setup

Right now, we don't really have an automated provisioning/setup script, because the actual setup is extremely simple:

 1. Create a Hetzner VM with Debian Trixie and a pre-configured SSH key.
 2. Install basic utilities: `apt-get install git`.
 3. Install `docker` based on official instructions.
 4. Clone the `luggage` repository into the `/root` folder.