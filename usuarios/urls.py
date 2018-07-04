from django.urls import path, include
from .import views


app_name = 'usuarios'

urlpatterns = [
    path('', views.singup, name='singup'),
    path('resena/<str:nombre_lugar>-<int:id_lugar>', views.resena, name='resena'),
    path('prueba_fb', views.prueba_fb, name='prueba_fb'),
    path('fb_extras', views.fb_extras, name='fb_extras'),
]
