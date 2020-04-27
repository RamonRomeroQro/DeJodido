
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path
from django.views.generic import TemplateView
from .import views
from .views import *
from django.urls import include, path

app_name = 'lugares'

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('busqueda', views.busqueda, name='busqueda'),
    path('lugar/<str:name>-<int:id_l>', views.detalle_lugar, name='detalle_lugar'),
    path('ajax/google/<str:id_google>', views.googleReviews, name='googleReviews'),
    path('ajax/foursquare/<str:id_foursquare>', views.foursquareReviews, name='foursquareReviews'),
    path('ajax/yelp/<str:id_yelp>', views.yelpReviews, name='yelpReviews'),
    #path('listaciudades', views.listaciudades, name='listaciudades'),

]
