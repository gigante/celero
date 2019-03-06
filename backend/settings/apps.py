import datetime
from .base import INSTALLED_APPS
from decouple import config, Csv

INSTALLED_APPS.append('rest_framework')
INSTALLED_APPS.append('rest_framework.authtoken')
INSTALLED_APPS.append('corsheaders')
INSTALLED_APPS.append('test_without_migrations')
INSTALLED_APPS.append('django_extensions')
INSTALLED_APPS.append('rest_framework_swagger')
INSTALLED_APPS.append('backend.core.apps.CoreConfig')

AUTH_USER_MODEL = 'core.user'

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
JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=24),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(hours=24),
}

# CORS
# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = config('CORS_ORIGIN_WHITELIST', default=[], cast=Csv())
