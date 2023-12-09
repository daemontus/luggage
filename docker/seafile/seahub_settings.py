# -*- coding: utf-8 -*-
SECRET_KEY = "!!!SECRET!!!"
SERVICE_URL = "https://seafile.unsigned-short.com/"

# See https://forum.seafile.com/t/403-forbidden-csrf-verification-failed-referer-checking-failed-does-not-match-trusted-origins/8577/9
CSRF_TRUSTED_ORIGINS = ['https://seafile.unsigned-short.com']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': '!!!SECRET!!!',
        'PASSWORD': '!!!SECRET!!!',
        'HOST': 'seafile-db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'seafile-memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Etc/UTC'
FILE_SERVER_ROOT = "http://seafile.unsigned-short.com/seafhttp"

# OAuth configuration using authelia.
ENABLE_OAUTH = True
OAUTH_ENABLE_INSECURE_TRANSPORT = True
OAUTH_CREATE_UNKNOWN_USER = True
OAUTH_ACTIVATE_USER_AFTER_CREATION = True
OAUTH_CLIENT_ID = "seafile"
OAUTH_CLIENT_SECRET = "!!!SECRET!!!"
OAUTH_REDIRECT_URL = 'https://seafile.unsigned-short.com/oauth/callback/'
OAUTH_PROVIDER_DOMAIN = 'auth.unsigned-short.com'
OAUTH_AUTHORIZATION_URL = 'https://auth.unsigned-short.com/api/oidc/authorization'
OAUTH_TOKEN_URL = 'https://auth.unsigned-short.com/api/oidc/token'
OAUTH_USER_INFO_URL = 'https://auth.unsigned-short.com/api/oidc/userinfo'
OAUTH_SCOPE = [
    "openid",
    "profile",
    "email",
]
OAUTH_ATTRIBUTE_MAP = {
    "email": (True, "email"),
    "name": (False, "name"),
    "id": (False, "not used"),
}
