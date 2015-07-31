"""
Django settings for scblog project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import ast



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# keys are defined in bin/activate of virtualenv
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = ast.literal_eval(os.environ['DJANGO_SCBLOG_DEVELOPMENT'])
if DEBUG is not True:
    ALLOWED_HOSTS = ['sanketchauhan.com', 'wwww.sanketchauhan.com']


# Application definition

INSTALLED_APPS = (
    'flat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'django_markdown',
    'django_summernote',
)

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'scblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'scblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'scblog_db',
        'USER' : os.environ['DB_USERNAME'],
        'PASSWORD' : os.environ['DB_PASSWORD'],
        'HOST' : '',
        'PORT' : '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

SETTINGS_DIR = os.path.dirname(__file__) #gets to folder containing this file
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH) #goes back up

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"), )
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

INSTALLED_APPS += (
    'opbeat.contrib.django',
)
OPBEAT = {
    'ORGANIZATION_ID': 'a78ba6fef7824779bb6724b949248401',
    'APP_ID': 'bc313f8620',
    'SECRET_TOKEN': '454b3d2814992b2df042a7f47cc3dc1f5e823955',
}


