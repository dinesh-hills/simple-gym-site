import os
import json
from .base import *


DEBUG = False

with open('gym_app/settings/secrets.json', 'r') as f:
    secrets = json.load(f)

DEBUG = False

SECRET_KEY = secrets['secret_key']

# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

ALLOWED_HOSTS = ['localhost']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}