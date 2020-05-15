import os
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOADSTORAGE = FileSystemStorage(location=BASE_DIR, base_url='/uploads')
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'lugares',
    'landing',
    'usuarios',
    'social_django',
    'api',
    'sm',
    # New for google
    'django.contrib.sites',  # <--
    'allauth',  # <--
    'allauth.account',  # <--
    'allauth.socialaccount',  # <--
    'allauth.socialaccount.providers.google',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'deajodido.middleware.AutoLogout',

]
ROOT_URLCONF = 'deajodido.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]
WSGI_APPLICATION = 'deajodido.wsgi.application'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    # New login
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

)

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
SITE_ID = 2
LOGIN_REDIRECT_URL = '/'

# retrived info
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
]

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'locale': 'ru_RU',
    'fields': 'id,name,email',
}
AUTO_LOGOUT_DELAY = 180

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = 'America/Mexico_City'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#########
# Al Agregar variables de ambiente a manage.py, settings.py, wsgy y nginx

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = eval(os.getenv("DEBUG"))
ALLOWED_HOSTS = [x.strip() for x in str(os.getenv("ALLOWED_HOSTS")).split(',')]

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DBENGINE'),
        'NAME': os.getenv('DBNAME'),
        'USER': os.getenv('DBUSER'),
        'PASSWORD': os.getenv('DBPSWD'),
        'HOST': os.getenv('DBHOST'),
        'PORT': os.getenv('DBPORT'),
    }
}
GMAPS_API_KEY = os.getenv('GMAPS_API_KEY')
GMAPS_API_KEY_JS = os.getenv('GMAPS_API_KEY_JS')
FBTOKEN = os.getenv('FBTOKEN')
YELP_AUTH = os.getenv('YELP_AUTH')
FSQID = os.getenv('FSQID')
FSQS = os.getenv('FSQS')
FSQV = os.getenv('FSQV')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_REDIRECT_IS_HTTPS = eval(os.getenv("SOCIAL_AUTH_REDIRECT_IS_HTTPS"))
SECURE_SSL_REDIRECT = eval(os.getenv("SECURE_SSL_REDIRECT"))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BROKER_URL = os.getenv("BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
