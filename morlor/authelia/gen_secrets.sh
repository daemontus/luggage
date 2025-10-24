#!/bin/bash

ENV_FILE = '/root/data/authelia/secrets.env'
echo "" > $ENV_FILE

echo "AUTHELIA_JWT_SECRET=`op read op://TichaPosta/AUTHELIA_SECRETS/JWT_SECRET`" >> $ENV_FILE
echo "AUTHELIA_SESSION_SECRET=`op read op://TichaPosta/AUTHELIA_SECRETS/SESSION_SECRET`" >> $ENV_FILE
echo "AUTHELIA_STORAGE_KEY=`op read op://TichaPosta/AUTHELIA_SECRETS/STORAGE_KEY`" >> $ENV_FILE
echo "AUTHELIA_SMTP_PASSWORD=`op read op://TichaPosta/AUTHELIA_SECRETS/SMTP_PASSWORD`" >> $ENV_FILE
echo "AUTHELIA_OIDC_HMAC_SECRET=`op read op://TichaPosta/AUTHELIA_SECRETS/OIDC_HMAC_SECRET`" >> $ENV_FILE
echo "AUTHELIA_CLIENT_SECRET_SEAFILE=`op read op://TichaPosta/AUTHELIA_SECRETS/CLIENT_SECRET_SEAFILE`" >> $ENV_FILE
echo "AUTHELIA_CLIENT_SECRET_IMMICH=`op read op://TichaPosta/AUTHELIA_SECRETS/CLIENT_SECRET_IMMICH`" >> $ENV_FILE
echo "AUTHELIA_CLIENT_SECRET_SYNAPSE=`op read op://TichaPosta/AUTHELIA_SECRETS/CLIENT_SECRET_SYNAPSE`" >> $ENV_FILE

echo `op read op://TichaPosta/AUTHELIA_SECRETS/jwtRS256.key` > /root/data/authelia/jwtRS256.key
echo `op read op://TichaPosta/AUTHELIA_SECRETS/jwtRS256.key.pub` > /root/data/authelia/jwtRS256.key.pub