from django.db import models
from django.contrib.auth.models import User
from lugares.models import Ciudad

# Create your models here.

GENEROS = (
    (1, 'mujer'),
    (2, 'hombre'),
    (3, 'Prefiro no decir')
)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(default='', verbose_name='Fecha de Nacimiento')
    genero = models.IntegerField(choices=GENEROS,verbose_name='Genero', null=False, blank=False)
    imagen = models.ImageField(upload_to='imagen_usuarios', verbose_name='Perfil', null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    fb_id = models.CharField(max_length=17, unique=True, blank=True, null=True)
