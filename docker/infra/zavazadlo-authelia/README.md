# Authelia

Authelia provides authentication on `luggage` using the `authelia/authelia:latest` docker image. For maximum security, we do not actually perform any modifications to the docker image itself. In this README, we just list how the docker image should be set up. The actual configuration files (including secrets) are only available in a 1Password vault. Authelia only handles user/group management and session login/logout. The rest of the authentication "logic" is handled by the reverse-proxy.

 - Create an `authelia` directory in `/mnt/user/appdata`.
 - In this directory, create `configuration.yml` file. This file is in the 1Password vault. If you are creating a new configuration from scratch, a template based on [this file](https://github.com/authelia/authelia/blob/v4.37.5/config.template.yml) is already available in this folder. This template is configured for "minimalistic" deployments with handful of users stored in a file and an SQLlite database (as opposed to using LDAP, redis and PostgreSQL in a more "professional" setup).
    - Don't forget to set up SMTP notifications (if you are using gmail, create a new app password).
 - Create `users.yml` file in the `authelia` directory (see this [guide](https://www.authelia.com/reference/guides/passwords/#user--password-file)). This file is also in the 1Password vault. However, a user changing their password will change the contents of the file. You should back it up when you create/delete a user.
 - Create the docker container. Configure:
 	- Repository as `authelia/authelia:latest`.
 	- Export port `9091`. 
    - If you plan to also use `prometheus` monitoring (which you probably should), also export port `9959`.
 	- Map `/config` in the container to `/mnt/user/appdata/authelia`.

### Manipulating users

To add/delete a user, simply update the `/mnt/user/appdata/authelia/users.yml` file. Don't worry about generating the password hash from scratch: a user can reset their password, so any hash will do. However, it must be in a "valid format", so you might need to copy the format of some of the other passwords. Once the file is saved, authelia should reload it automatically.