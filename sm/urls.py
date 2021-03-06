
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import *
from . import master

app_name = 'sm'

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('lugares', views.lugares, name='lugares'),
    path('lugar/<int:id_lugar>', views.detalle_lugar, name='detalle_lugar'),
    path('update_place/<int:id_lugar>', views.update_place, name='update_place'),
    path('update_image/<int:id_image>', views.update_image, name='update_image'),
    path('quickimages', views.quickimages, name='quickimages'),
    path('atrue/<int:id_imagen>', views.atrue, name='atrue'),
    path('faces_command', views.faces_command, name='faces_command'),
    path('afalse/<int:id_imagen>', views.afalse, name='afalse'),
    path('imagenes', views.imagenes, name='imagenes'),
    path('', views.consola, name='consola'),
    path('log/<int:id_comando>', views.log, name='log'),

    #path('listaciudades', views.listaciudades, name='listaciudades'),

]
