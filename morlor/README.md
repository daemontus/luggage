# Morlor Cloud Gateway

Morlor is a small VM running in Hetzner cloud responsible for routing requests from "the open internet" towards our infrastructure. Morlor also stores the small amount of data (`/root/data`) needed for working HTTPS and OIDC user authentication.

## HTTPS

Morlor also manages all HTTPS certificates. Ideally, we would use the ACME support built into `nginx`, but we will need to share the certificates across several devices that will handle requests from federated LANs. As such, it must be possible to sync certificates to these devices, since they can't use normal provisioning.

The certificates are managed by `certbot` and stored in `/root/data/letsencrypt`. Assuming `reverse-proxy` is running, to create a certificate, simply run:

```
./https/certificate_create.sh some.domain.com
```

The certificates needs to be renewed monthly, and *`nginx` needs to be restarted every time the certificate changes*. This is handled by the `certificate_renew.sh` script, which will also restart the `reverse-proxy` container. To run the script periodically, add the following cron entry (run `crontab -e` to edit):

```
0 0 * * 1 /root/luggage/morlor/https/certificate_renew.sh
```

## Services

### Reverse proxy

### Authelia

Authelia is an identity provider that we use for user management. All configuration values for `authelia` are stored in 1Password (vault `Ticha posta`, item `AUTHELIA_SECRETS`). However, for redundancy, the secrets are also stored locally with the configuration files. To apply configuration changes, follow these steps:

 * Make sure `/root/data/authelia/users.yml` is present and contains all user data.
 * Make sure you are logged in to 1Password, and then run `./authelia/secrets.sh`. This should populate the `/root/data/authelia/secrets.env` file as well as `/root/data/authelia/jwtRS256.key`.
 * Make a backup copy of current `/root/data/authelia/configuration.yml` (if it exists).
 * Finally, copy current `./authelia/configuration.template.yml` into `/root/data/authelia/configuration.yml` (the configuration should be automatically populated from environment variables in the `secrets.env` file).

## VM Setup

Right now, we don't really have an automated provisioning/setup script, because the actual setup is extremely simple:

 1. Create a Hetzner VM with Debian Trixie and a pre-configured SSH key.
 2. Install basic utilities: `apt-get install git magic-wormhole zip unzip`.
 3. Install `docker` based on official instructions.
 4. Install `op` (1password) using official instructions and log in (`op account add`, etc.).
 5. Clone the `luggage` repository into the `/root` folder.
 6. Prepare HTTPS certificates in `/root/data/letsencrypt`. 
 7. Prepare configuration and user data in `/root/data/authelia`.
 8. Make sure to add `certificate_renew.sh` to `crontab` (see HTTPS section).
 9. Create authelia configuration and import user data per instructions above.