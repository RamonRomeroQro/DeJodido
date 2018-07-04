from django.urls import path, include
from .import views


app_name = 'usuarios'

urlpatterns = [
    path('', views.singup, name='singup'),
    path('resena/<str:nombre_lugar>-<int:id_lugar>', views.resena, name='resena'),
    path('prueba_fb', views.prueba_fb, name='prueba_fb'),
]
