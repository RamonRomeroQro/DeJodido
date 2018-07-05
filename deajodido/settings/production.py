from deajodido.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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

# Google's Keys
GMAPS_API_KEY = 'AIzaSyCcoUgaJSJJteLoXlvtY77eu3xam0hWFME'
GMAPS_API_KEY_JS= 'AIzaSyC3EcXKhyPwcWgVlPAzDGplTa00HkKD0KQ'

#SocialAUTH's Keys
SOCIAL_AUTH_FACEBOOK_KEY = '805766712952383'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'd7b13e308d24be4726f0c81721259a97'  # App Secret
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_FACEBOOK_API_VERSION = '3.0'



# Force https redirect
SECURE_SSL_REDIRECT = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Force HTTPS in the final URIs
