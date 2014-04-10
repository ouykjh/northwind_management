"""
Django settings for mvp_landing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
#
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# BASE_DIT = '/home/pkala/django/src'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'q)y+n7qqs5yqv-tm_pib8^@kax$axfv8m21^i@o^utb0^2!kus'
SECRET_KEY = '1qb)7k*2-^1na7jk$bgt@9ybaw2ugi2!gz)d-g2rrc_v@k9phn'

SITE_ID = 123;
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

APPEND_SLASH = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'article',
    'orders',
    'regions',
    'shippers',
    'suppliers',
    'territories',
    'usstates',
    'categories',
    'customers',
    'employees',
    'employeeterritories',
    'products',
    'lists',
    'orderdetails',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mvp_landing.urls'

WSGI_APPLICATION = 'mvp_landing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'mydb',
    'USER': 'psql',
    'PASSWORD': '123qwe',
    'HOST': 'localhost',
    'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Template location

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
    #/home/pkala/django/static/templates/',
)

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "templates")
    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
        os.path.join(os.path.dirname(BASE_DIR), "static", "bootstrap"),
    )
    
    
    
