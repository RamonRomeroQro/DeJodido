from django.db import models

# Create your models here.
import os


class Pais(models.Model):
    nombre=models.CharField(verbose_name='País', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    nombre=models.CharField(verbose_name='Estado', null=True, blank=True, max_length=200)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class Ciudad(models.Model):
    nombre=models.CharField(verbose_name='Ciudad', null=True, blank=True, max_length=200)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class Tags(models.Model):
    descripcion=models.CharField(verbose_name='Tag', null=True, blank=True, max_length=200)

    def __str__(self):
        return self.descripcion




class Lugar(models.Model):
    nombre= models.CharField(verbose_name='Nombre', null=True, blank=True, max_length=200)
    direccion= models.CharField(verbose_name='Dirección', null=True, blank=True, max_length=500)
    latitud= models.FloatField(verbose_name='Latitud', null=True, blank=True)
    longitud= models.FloatField(verbose_name='Longitud', null=True, blank=True)
    botana=models.NullBooleanField(verbose_name='Botana')
    validado=models.BooleanField(verbose_name='Validado')
    rating=models.FloatField(verbose_name='Rating', null=True, blank=True)
    precio=models.FloatField(verbose_name='Precio', null=True, blank=True)
    id_google=models.CharField(verbose_name='ID Google Places', null=True, blank=True, max_length=500, unique=True)
    id_yelp=models.CharField(verbose_name='ID Yelp', null=True, blank=True, max_length=500)
    id_foursquare=models.CharField(verbose_name='ID FourSquare', null=True, blank=True, max_length=500)
    id_facebook = models.CharField(verbose_name='ID Facebook Place', null=True, blank=True, max_length=500)
    facebook_link = models.CharField(verbose_name='ID Facebook Link', null=True, blank=True, max_length=500)
    tags = models.ManyToManyField(Tags, verbose_name='Tags')
    ciudad = models.ForeignKey(Ciudad, verbose_name='Ciudad', on_delete=models.CASCADE,  null=True, blank=True)
    status=models.NullBooleanField(verbose_name='status', default=None ,  null=True)
    update_command = models.DateField(auto_now=True)


    def delete(self):

        imagenes=Imagen.objects.filter(lugar=self.id)
        for i in imagenes:
            i.delete()
        super(Lugar, self).delete()




    def __str__(self):
        return self.nombre



class Imagen(models.Model):

    imagen=models.ImageField(upload_to='imagen', verbose_name='Imagen', null=True, blank=True)
    lugar=models.ForeignKey(Lugar, on_delete=models.CASCADE)
    descripcion=models.CharField(verbose_name="Descripción", null=True, blank=True, max_length=1000)
    status=models.NullBooleanField(verbose_name='status', default=None ,  null=True)

    def __str__(self):
        return self.imagen.url

    def delete(self):
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super(Imagen, self).delete()
