
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path
from django.views.generic import TemplateView
from .import views
from .views import *

app_name = 'lugares'

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('', views.busqueda, name='busqueda'),
    #path('listaciudades', views.listaciudades, name='listaciudades'),


]