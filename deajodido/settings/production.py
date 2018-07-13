from deajodido.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['138.197.223.47', 'dejodido.com']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'deajodido',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Email Djnago Parameters
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'help.dejodido@gmail.com'
EMAIL_HOST_PASSWORD = 'queretaro'
EMAIL_USE_TLS = True

# Google's Keys
GMAPS_API_KEY = 'AIzaSyCcoUgaJSJJteLoXlvtY77eu3xam0hWFME'
GMAPS_API_KEY_JS= GMAPS_API_KEY


