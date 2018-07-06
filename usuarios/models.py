from django.db import models
from django.contrib.auth.models import User
from lugares.models import Ciudad
from lugares.models import Lugar
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import os

# Create your models here.

GENEROS = (
    (1, 'Mujer'),
    (2, 'Hombre'),
    (3, 'No Binario')
)


calificaciones = (
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐')
)

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(default='', verbose_name='Fecha de Nacimiento', null=False, blank=False)
    genero = models.IntegerField(choices=GENEROS,verbose_name='Género', null=False, blank=False)
    imagen = models.ImageField(upload_to='imagen_usuarios', verbose_name='Imágen de Perfil', null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name="Ciudad de Residencia")
    ciudadUnparsable = models.CharField( verbose_name="Ciudad Unparseable", max_length=500, blank=True, null=True, default='OK')
    fb_id = models.CharField(max_length=20, unique=True, blank=True, null=True)


    def delete(self):
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super(Usuario, self).delete()




class Resena(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    calificacion = models.IntegerField(choices=calificaciones,verbose_name='Rating', null=False, blank=False, validators=[MinValueValidator(0),
                                                                                                   MaxValueValidator(5)]
                                       )
    precio_cerveza = models.IntegerField(verbose_name='Precio Cerveza', null=False, blank=False, validators=[MinValueValidator(0)])
    comentario = models.TextField(default='', null=True, blank=True)

