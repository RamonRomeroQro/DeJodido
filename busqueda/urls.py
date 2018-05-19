from django.urls import path
from .import views

app_name = 'busqueda'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('listaciudades', views.listaciudades, name='listaciudades'),

]
