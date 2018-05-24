from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENEROS = (
    (1, 'mujer'),
    (2, 'hombre'),
    (3, 'Prefiro no decir')
)


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField()
    genero = models.IntegerField(choices=GENEROS)
