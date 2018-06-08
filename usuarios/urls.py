from django.urls import path, include
from .import views


app_name = 'usuarios'

urlpatterns = [
    path('', views.Prueba_index, name='Prueba_index'),
    path('resena/<str:nombre_lugar>-<int:id_lugar>', views.prueba_resena, name='Prueba_resena'),
    path('verificacion_FB/', views.verificacion_FB, name='nueva_cuentaFB'),
]