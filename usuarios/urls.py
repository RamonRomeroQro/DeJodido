from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path('', views.Prueba_index, name='Prueba_index'),
    path('success/', views.Prueba_login_si, name='Prueba_si'),
]