"""
DJANGO HONEYWORDS LOCAL DEVELOPMENT SETTINGS
config/settings/local.py
"""
from .base import *

DEBUG = True

SECRET_KEY = get_env_variable("SECRET_KEY")

INSTALLED_APPS += ['honeywords',]

HONEYCHECKER_URI = 'http://192.168.56.101:55555'

ALLOWED_HOSTS = ['localhost',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
