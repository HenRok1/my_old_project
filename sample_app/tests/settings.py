import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.sqlite3', 
        'NAME':     'django_sample_app_test',
    }
}

TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

MEDIA_ROOT = os.path.join(os.path.abspath(os.path.curdir), 'tests')

MEDIA_URL = ''

STATIC_URL = '/static/'

SECRET_KEY = 'v2824l&2-n+4zznbsk9c-ap5i)b3e8b+%*a=dxqlahm^%)68jn'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'sample_app.tests.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'sample_app',
    'sample_app.tests',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            ],
        },
    },
]

SAMPLE_APP_REDIRECT_TO_URL_NAME = 'home'
