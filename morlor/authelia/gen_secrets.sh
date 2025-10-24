#!/bin/bash

ENV_FILE='/root/data/authelia/secrets.env'
echo "" > $ENV_FILE

echo "JWT_SECRET='`op read op://TichaPosta/SECRETS_AUTHELIA/JWT_SECRET`'" >> $ENV_FILE
echo "SESSION_SECRET='`op read op://TichaPosta/SECRETS_AUTHELIA/SESSION_SECRET`'" >> $ENV_FILE
echo "STORAGE_KEY='`op read op://TichaPosta/SECRETS_AUTHELIA/STORAGE_KEY`'" >> $ENV_FILE
echo "SMTP_PASSWORD='`op read op://TichaPosta/SECRETS_AUTHELIA/SMTP_PASSWORD`'" >> $ENV_FILE
echo "OIDC_HMAC_SECRET='`op read op://TichaPosta/SECRETS_AUTHELIA/OIDC_HMAC_SECRET`'" >> $ENV_FILE
echo "CLIENT_SECRET_DIGEST_SEAFILE='`op read op://TichaPosta/SECRETS_SEAFILE/OIDC_CLIENT_SECRET_DIGEST`'" >> $ENV_FILE
echo "CLIENT_SECRET_DIGEST_IMMICH='`op read op://TichaPosta/SECRETS_IMMICH/OIDC_CLIENT_SECRET_DIGEST`'" >> $ENV_FILE
echo "CLIENT_SECRET_DIGEST_SYNAPSE='`op read op://TichaPosta/SECRETS_SYNAPSE/OIDC_CLIENT_SECRET_DIGEST`'" >> $ENV_FILE

op read op://TichaPosta/SECRETS_AUTHELIA/jwtRS256.key > /root/data/authelia/jwtRS256.key
op read op://TichaPosta/SECRETS_AUTHELIA/jwtRS256.key.pub > /root/data/authelia/jwtRS256.key.pub