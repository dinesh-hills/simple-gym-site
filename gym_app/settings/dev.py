import json
from .base import *

with open('gym_app/settings/secrets.json', 'r') as f:
    secrets = json.load(f)

DEBUG = True

SECRET_KEY = secrets['secret_key']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}