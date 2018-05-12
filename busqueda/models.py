from django.db import models




class Lugar(models.Model):
    tipo = models.ManyToManyField(TipoLugar)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Lugar')
    id_google = models.CharField(max_length=20, verbose_name="ID Google", default=None )
    id_facebook = models.CharField(max_length=20, verbose_name="ID Facebook", default=None )
    id_yelp = models.CharField(max_length=20, verbose_name="ID Yelp", default=None )
    id_foursquare = models.CharField(max_length=20, verbose_name="ID FourSquare", default=None )
    calificacion = models.FloatField()


class TipoLugar(models.Model):
    descripcion = models.CharField(max_length=20, verbose_name="Tipo de Lugar")