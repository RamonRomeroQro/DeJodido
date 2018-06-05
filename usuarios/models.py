from django.db import models
from django.contrib.auth.models import User
from lugares.models import Ciudad
from lugares.models import Lugar
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

GENEROS = (
    (1, 'mujer'),
    (2, 'hombre'),
    (3, 'Prefiro no decir')
)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(default='', verbose_name='Fecha de Nacimiento', null=False, blank=False)
    genero = models.IntegerField(choices=GENEROS,verbose_name='Genero', null=False, blank=False)
    imagen = models.ImageField(upload_to='imagen_usuarios', verbose_name='Perfil', null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fb_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    resena = models.ManyToManyField(Lugar, through='UsuarioResenaLugar')



class UsuarioResenaLugar(models.Model):
    fecha = models.DateField(default='')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    calificaicon = models.IntegerField(verbose_name='Rating', null=False, blank=False)
    precio_cerveza = models.IntegerField(verbose_name='Precio Cerveza', null=False, blank=False)
    comentario = models.TextField(default='', null=True, blank=True)

