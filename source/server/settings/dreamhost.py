from .base import *
import os
from configparser import RawConfigParser

config = RawConfigParser()
config.read(os.environ.get('CONFIGURATIONS_FILE'))

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.authentication.OAuth2Authentication',
    )
}

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend'
)

STATIC_ROOT = config.get('fe-auth-server', 'STATIC_ROOT')
