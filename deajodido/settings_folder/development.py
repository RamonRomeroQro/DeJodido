
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-3eh!c!w_&@pn))c^nrmq*cy(#48orq%+4sj#vw6l_z9b&obu&'

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
        'PASSWORD': "",
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Google's Keys
GMAPS_API_KEY = 'AIzaSyAyWoMzx2h4NwDk5NRmUqsODLC6vJKD_KA'
GMAPS_API_KEY_JS= GMAPS_API_KEY
FBTOKEN = '544112989843154|hBY39frkP-_8ovjnNsR3al2A08I'
YELP_AUTH="Bearer HEumDTz_X--m2lBW9-ZDlrMkQ_JlbuFFuF-6T7fzCJVlHrKYUhm7d7kF_LRCFGA7INdPcVPjd5Bo3LiDrUc9mEh-r5kV7LhSqazuQNB_AULEToDQ07leabVba5yjXnYx"
FSQ_client_id='TFLJCZKNWYCSSZPARN4JDZDRGPUENHKA12JOXYUHN4L5N5I5'
FSQ_client_secret='SCLJLKDKO2TSJHUGI0RIEOL53G3FV3HR42NCN00SC3LG5EHN'
FSQ_v='20180323'

#SocialAUTH's Keys
SOCIAL_AUTH_FACEBOOK_KEY = '805766712952383'  # App ID PRUEBA
SOCIAL_AUTH_FACEBOOK_SECRET = 'd7b13e308d24be4726f0c81721259a97'  # App Secret PRUEBA
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False