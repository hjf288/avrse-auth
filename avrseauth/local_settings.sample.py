import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# These are the settings you should update
# SECURITY WARNING: keep the secret key used in production secret! Generate a random string
SECRET_KEY = 'asdasd'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CELERY_APP_NAME = "avrseauth"
BROKER_URL = "redis://127.0.0.1:6379/"
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/"

SOCIAL_AUTH_EVEONLINE_KEY = ""
SOCIAL_AUTH_EVEONLINE_SECRET = ""

ESI_URL = "https://esi.tech.ccp.is/latest"
ESI_DATASOURCE = "tranquility"
ESI_RETRIES = 15

MUMBLE_HOST = ""
MUMBLE_PORT = 64738

members = {
    "alliances": [
    ],
    "corps": [
    ]
}

blues = {
    "alliances": [
    ],
    "corps": [
    ]
}