
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path
from django.views.generic import TemplateView
from .import views
from .views import *

from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api'

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    #path('place?id=<int:id_lugar>', views.detalle_lugar, name='detalle_lugar'),
    #path('search?city=<str:city>', views.detalle_lugar, name='detalle_lugar'),
    path('search', views.search.as_view(), name='search'),

    #path('listaciudades', views.listaciudades, name='listaciudades'),

]

urlpatterns=urlpatterns+format_suffix_patterns(urlpatterns)
