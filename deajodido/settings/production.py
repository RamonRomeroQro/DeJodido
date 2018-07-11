from deajodido.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

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

''''
ESTO VA EN PRODUCCION


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

GMAPS_API_KEY = 'AIzaSyC9nWuYkCMxKm_PFZ6m04gCAuz-SeuCE2g'
GMAPS_API_KEY_JS= GMAPS_API_KEY

SOCIAL_AUTH_FACEBOOK_KEY = '805766712952383'  # App ID PRUEBA
SOCIAL_AUTH_FACEBOOK_SECRET = 'd7b13e308d24be4726f0c81721259a97'  # App Secret PRUEBA
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
'''


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

#SocialAUTH's Keys
SOCIAL_AUTH_FACEBOOK_KEY = '805766712952383'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'd7b13e308d24be4726f0c81721259a97'  # App Secret
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True



# Force https redirect
SECURE_SSL_REDIRECT = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Force HTTPS in the final URIs


