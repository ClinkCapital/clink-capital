from clink.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('CLINK_DB_NAME'),
        'USER': os.getenv('CLINK_DB_USER'),
        'PASSWORD': os.getenv('CLINK_DB_PASSWORD'),
        'HOST': os.getenv('CLINK_DB_HOST'),
        'PORT': os.getenv('CLINK_DB_PORT'),
    }
}

STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/'
