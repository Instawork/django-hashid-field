import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'fake-key'
HASHID_FIELD_SALT = 'gg ez'
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.admin",
    "tests",
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
