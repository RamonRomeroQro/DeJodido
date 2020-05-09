#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deajodido.settings")
    '''
    SECRET_KEY="-3eh!c!w_&@pn))c^nrmq*cy(#48orq%+4sj#vw6l_z9b&obu&"
    DEBUG=True
    ALLOWED_HOSTS=["*"]
    DBENGINE="django.db.backends.postgresql"
    DBNAME="dbdejodido"
    DBUSER="dbuserjodido"
    DBPSWD="mkd.3i4cq"
    DBHOST="localhost"
    DBPORT="5432"
    GMAPS_API_KEY="AIzaSyAyWoMzx2h4NwDk5NRmUqsODLC6vJKD_KA"
    GMAPS_API_KEY_JS="AIzaSyAyWoMzx2h4NwDk5NRmUqsODLC6vJKD_KA"
    FBTOKEN="544112989843154|hBY39frkP-_8ovjnNsR3al2A08I"
    YELP_AUTH="Bearer HEumDTz_X--m2lBW9-ZDlrMkQ_JlbuFFuF-6T7fzCJVlHrKYUhm7d7kF_LRCFGA7INdPcVPjd5Bo3LiDrUc9mEh-r5kV7LhSqazuQNB_AULEToDQ07leabVba5yjXnYx"
    FSQID="TFLJCZKNWYCSSZPARN4JDZDRGPUENHKA12JOXYUHN4L5N5I5"
    FSQS="SCLJLKDKO2TSJHUGI0RIEOL53G3FV3HR42NCN00SC3LG5EHN"
    FSQV="20180323"
    EMAIL_HOST="smtp.gmail.com"
    EMAIL_PORT=587
    EMAIL_HOST_USER="help.dejodido@gmail.com"
    EMAIL_HOST_PASSWORD="queretaro"
    EMAIL_USE_TLS=True
    SOCIAL_AUTH_FACEBOOK_KEY="805766712952383"
    SOCIAL_AUTH_FACEBOOK_SECRET="d7b13e308d24be4726f0c81721259a97"
    SOCIAL_AUTH_REDIRECT_IS_HTTPS=True
    SECURE_SSL_REDIRECT=False


    DATABASES = {
    'default': {
        'ENGINE': DBENGINE,
        'NAME': DBNAME,
        'USER': DBUSER,
        'PASSWORD': DBPSWD,
        'HOST': DBHOST,
        'PORT': DBPORT,
    }
}
    '''




    from dotenv import load_dotenv

    load_dotenv()

    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = eval(os.getenv("DEBUG"))
    ALLOWED_HOSTS = [ x.strip() for x in str(os.getenv("ALLOWED_HOSTS")).split(',')]
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
    SOCIAL_AUTH_REDIRECT_IS_HTTPS =  eval(os.getenv("SOCIAL_AUTH_REDIRECT_IS_HTTPS"))
    SECURE_SSL_REDIRECT =  eval(os.getenv("SECURE_SSL_REDIRECT"))
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
