from django.db import models




class Ciudad(models.Model):
    ciudad=models.CharField(max_length=100, verbose_name='Ciudad')
    pais=models.CharField(max_length=100, verbose_name='Pais')
    latitud=models.FloatField(verbose_name='Latitud')
    longitud=models.FloatField(verbose_name='Longitud')

    def __str__(self):
        return 'Ciudad: %s Pais: %s latitud: %s longitud: %s' % (self.ciudad, self.pais, self.latitud, self.latitud)

'''
class TipoLugar(models.Model):
    descripcion = models.CharField(max_length=20, verbose_name="Tipo de Lugar")
'''


class Lugar(models.Model):
#   tipo = models.ManyToManyField(TipoLugar)
    nombre = models.CharField(max_length=300, verbose_name='Nombre del Lugar')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')
    direccion = models.CharField(max_length=300, verbose_name='Dirección')
    place_id = models.CharField(max_length=100, verbose_name="ID Google", default=None )
    rating = models.FloatField(verbose_name='rating',)

#   id_facebook = models.CharField(max_length=20, verbose_name="ID Facebook", default=None )
#   id_yelp = models.CharField(max_length=20, verbose_name="ID Yelp", default=None )
#   id_foursquare = models.CharField(max_length=20, verbose_name="ID FourSquare", default=None )

