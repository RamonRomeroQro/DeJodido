from django.db import models
from django.contrib.auth.models import User
from lugares.models import Ciudad
from lugares.models import Lugar
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

GENEROS = (
    (1, 'Mujer'),
    (2, 'Hombre'),
    (3, 'Otro')
)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(default='', verbose_name='Fecha de Nacimiento', null=False, blank=False)
    genero = models.IntegerField(choices=GENEROS,verbose_name='Género', null=False, blank=False)
    imagen = models.ImageField(upload_to='imagen_usuarios', verbose_name='Imágen de Perfil', null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad de Residencia")
    fb_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
    resena = models.ManyToManyField(Lugar, through='UsuarioResenaLugar')



class UsuarioResenaLugar(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    calificaicon = models.IntegerField(verbose_name='Rating', null=False, blank=False, validators=[MinValueValidator(0),
                                                                                                   MaxValueValidator(5)]
                                       )
    precio_cerveza = models.IntegerField(verbose_name='Precio Cerveza', null=False, blank=False)
    comentario = models.TextField(default='', null=True, blank=True)

