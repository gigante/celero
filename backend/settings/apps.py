import os
import datetime
from .base import ROOT_DIR, DEBUG, INSTALLED_APPS
from decouple import config, Csv

INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')
INSTALLED_APPS.append('corsheaders')
INSTALLED_APPS.append('test_without_migrations')
INSTALLED_APPS.append('django_extensions')
INSTALLED_APPS.append('webpack_loader')
INSTALLED_APPS.append('rest_framework_swagger')
INSTALLED_APPS.append('backend.core.apps.CoreConfig')

AUTH_USER_MODEL = 'core.user'

# django webpack
# https://pypi.python.org/pypi/django-webpack-loader
STATS_DIR = f'{ROOT_DIR}/frontend/'

# webpack DEV env
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': '',
        'STATS_FILE': os.path.join(STATS_DIR, 'webpack-stats-dev.json'),
        'CACHE': not DEBUG,
    }
}

# webpack PROD env
if not DEBUG:
    WEBPACK_LOADER = {
        'DEFAULT': {
            'BUNDLE_DIR_NAME': '',
            'STATS_FILE': os.path.join(STATS_DIR, 'webpack-stats-prod.json'),
            'CACHE': not DEBUG,
        }
    }

# DRF
# http://www.django-rest-framework.org/
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# JWT
# http://getblimp.github.io/django-rest-framework-jwt/
payload_handle = 'backend.core.helpers.jwt.jwt_response_payload_handler'
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=24),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=24),
    'JWT_RESPONSE_PAYLOAD_HANDLER': payload_handle,
}

# CORS
# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', default=[], cast=Csv())
