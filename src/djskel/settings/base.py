import os
from urllib.parse import urlparse
from boto.s3.connection import OrdinaryCallingFormat
from path import path

PROJECT_DIR = path(__file__).dirname().abspath().realpath().parent.parent.parent
SRC_DIR = PROJECT_DIR / 'src'

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = bool(os.environ.get('DEBUG'))

ALLOWED_HOSTS = []

SITE_ID = 1


# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'djcelery',
    'registration',
    'django_ses',
    'djcelery_email',
    'crispy_forms',
    'pipeline',
    'storages',
    'easydump',
    'django_extensions',

    'djskel.apps.core',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'djskel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            PROJECT_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djskel.wsgi.application'


# Database
import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}
REDIS_URL = os.environ.get('REDISTOGO_URL', os.environ.get('REDIS_URL', 'redis://localhost:6959/0'))
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Testing
TEST_RUNNER = 'djskel.utils.testrunner.DiscoverRunner'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR / 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR / 'static'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR / 'assets',
)

# Celery

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'

import djcelery
djcelery.setup_loader()

# Django Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
REGISTRATION_OPEN = not bool(os.environ.get('CLOSE_REGISTRATION'))

# Email
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
CELERY_EMAIL_BACKEND = 'django_ses.SESBackend'
CELERY_EMAIL_TASK_CONFIG = {
    'rate_limit' : '1/s',
    'ignore_result': False,
}
DEFAULT_FROM_EMAIL = 'Adam Charnock <adam@adamcharnock.com>'
SERVER_EMAIL = 'Adam Charnock <adam@adamcharnock.com>'

# AWS
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'

# Crispy forms
CRISPY_TEMPLATE_PACK = 'uni_form'

# Pipeline
STATICFILES_STORAGE = 'djskel.utils.storages.S3PipelineManifestStorage'
# Let cloudinary take care of the minifying for us
PIPELINE_CSS_COMPRESSOR = False
PIPELINE_JS_COMPRESSOR = False

from djskel.assets import *

# Media files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
AWS_HEADERS = {
    'Cache-Control': 'max-age={}'.format(60*60*24*30),
}

# Easydump
EASYDUMP_MANIFESTS = {
    'default': {
        'database': 'default',
        's3-bucket': 'djskel_dumps',
        'jobs': 1,
    }
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        }
    }
}
