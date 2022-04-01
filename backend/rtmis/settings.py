"""
Django settings for rtmis project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from datetime import timedelta
from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ["DJANGO_SECRET"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if "DEBUG" in environ else False

ALLOWED_HOSTS = ['*']

# Application definition

# Default django apps
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Add third party apps below
EXTERNAL_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'django_dbml',
    'django_extensions',
    'django_q'
]

# Add API apps below
API_APPS = [
    'api.v1.v1_users',
    'api.v1.v1_profile',
    'api.v1.v1_forms',
    'api.v1.v1_data',
    'api.v1.v1_jobs',
]

INSTALLED_APPS = DJANGO_APPS + API_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rtmis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(BASE_DIR, 'rtmis/templates')],
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

WSGI_APPLICATION = 'rtmis.wsgi.application'

# Rest Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':
        ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.URLPathVersioning',
    'DATE_FORMAT':
        "%d-%m-%Y",
    "DEFAULT_VERSION":
        "v1",
    "DATETIME_FORMAT":
        "%d-%m-%Y %H:%M:%S",
    'DEFAULT_SCHEMA_CLASS':
        'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}
SPECTACULAR_SETTINGS = {
    'TITLE': 'RTMIS',
    'DESCRIPTION': '',
    'VERSION': '1.0.0',
    'SORT_OPERATIONS': False,
    'COMPONENT_SPLIT_REQUEST': True
}
# JWT Config
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
}
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ["DB_SCHEMA"],
        'USER': environ["DB_USER"],
        'PASSWORD': environ["DB_PASSWORD"],
        'HOST': environ["DB_HOST"],
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{
    'NAME':
        'django.contrib.auth.password_validation'
        '.UserAttributeSimilarityValidator',
}, {
    'NAME':
        'django.contrib.auth.password_validation'
        '.MinimumLengthValidator',
}, {
    'NAME':
        'django.contrib.auth.password_validation'
        '.CommonPasswordValidator',
}, {
    'NAME':
        'django.contrib.auth.password_validation'
        '.NumericPasswordValidator',
}]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static-files/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "v1_users.SystemUser"

FORM_GEO_VALUE = {"lat": 9.145, "lng": 40.4897}

BUCKET_NAME = "rtmis"
FAKE_STORAGE = False

EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'
MAILJET_API_KEY = environ["MAILJET_APIKEY"]
MAILJET_API_SECRET = environ["MAILJET_SECRET"]
EMAIL_FROM = 'noreply@akvo.org'

Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default'
}
