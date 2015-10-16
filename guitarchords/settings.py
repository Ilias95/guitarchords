"""
Django settings for guitarchords project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PRODUCTION = (os.getenv('PRODUCTION') == 'True')

# WARNING: Be careful not to override any variables defined on the following files
if PRODUCTION:
    from .settings_prod import *
else:
    from .settings_dev import *

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'registration',
    'password_validation',
    'bootstrapform',
    'compressor',
    'captcha',
    'chords',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

SITE_ID = 1

ROOT_URLCONF = 'guitarchords.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'guitarchords.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5,
        }
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_ROOT = os.path.join(BASE_DIR, 'chords/static')

# django-registration-redux app settings
# http://django-registration-redux.readthedocs.org

REGISTRATION_OPEN = True         # users can register
ACCOUNT_ACTIVATION_DAYS = 7      # one-week activation window
LOGIN_REDIRECT_URL = '/'         # redirect here after a successful log in
LOGIN_URL = '/accounts/login/'   # the page users are directed to if they are not logged in,
                                 # and are trying to access pages requiring authentication
REGISTRATION_EMAIL_HTML = False  # disable html emails (just use the txt version)

# django-recaptcha app settings
# https://github.com/praekelt/django-recaptcha

NOCAPTCHA = True  # if True, use the new No Captcha reCaptcha
RECAPTCHA_PUBLIC_KEY = '6Le9nQ0TAAAAALp08H8WCEg3EVZzwWZ3d7xJ4JoN'
