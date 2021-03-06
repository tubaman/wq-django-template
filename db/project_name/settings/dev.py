import os
import sys
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = 'manage.py' in sys.argv[0]

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'conf', '{{ project_name }}.sqlite3'),
    }
}

SPATIALITE_LIBRARY_PATH = 'mod_spatialite'

