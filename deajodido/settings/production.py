from deajodido.settings.common import *

# SECURITY WARNING: keep the secret key used in production secret!


'''


with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
    
    
'''

SECRET_KEY = '-3eh!c!w_&@pn))c^nrmq*cy(#48orq%+4sj#vw6l_z9b&obu&'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['dejodido.com','138.197.222.177']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

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