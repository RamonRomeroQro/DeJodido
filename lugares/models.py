from django.db import models

# Create your models here.


class Lugar(models.Model):
    nombre= models.CharField(verbose_name='Nombre', null=True, blank=True, max_length=200)
    direccion= models.CharField(verbose_name='Dirección', null=True, blank=True, max_length=500)
    latitud= models.FloatField(verbose_name='Latitud', null=True, blank=True)
    longitud= models.FloatField(verbose_name='Longitud', null=True, blank=True)
    botana=models.NullBooleanField(verbose_name='Botana')
    validado=models.BoleanField(verbose_name='Validado')
    rating=models.FloatField(verbose_name='Rating', null=True, blank=True)
    id_google=models.CharField(verbose_name='ID Google Places', null=True, blank=True, max_length=500)
    id_yelp=models.CharField(verbose_name='ID Yelp', null=True, blank=True, max_length=500)
    id_foursquare=models.CharField(verbose_name='ID FourSquare', null=True, blank=True, max_length=500)
    id_facebook = models.CharField(verbose_name='ID Facebook Place', null=True, blank=True, max_length=500)
    tags = models.ManyToManyField(Tags, verbose_name='Tags',  null=True, blank=True,)
    ciudad = models.ForeignKey(Ciudad, verbose_name='Ciudad', on_delete=models.CASCADE,  null=True, blank=True)

class Tags(models.Model):
    descripcion=models.CharField(verbose_name='Tag', null=True, blank=True, max_length=200)

class Ciudad(models.Model):
    nombre=models.CharField(verbose_name='Ciudad', null=True, blank=True, max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


class Estado(models.Model):
    nombre=models.CharField(verbose_name='Estado', null=True, blank=True, max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


class Pais(models.Model):
    nombre=models.CharField(verbose_name='País', null=True, blank=True, max_length=200)



