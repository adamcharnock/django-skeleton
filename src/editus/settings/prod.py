import os
from .base import *

SITE_URL = 'https://author.co'

# SSL
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

INSTALLED_APPS += ['gunicorn']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# HEROKU CONFIG

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'static'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    PROJECT_DIR / 'assets',
)
# This should be enabled on prod regardless of DEBUG setting
PIPELINE_ENABLED = True

# Celery
CELERYD_CONCURRENCY = 3
