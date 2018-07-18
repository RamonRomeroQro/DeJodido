from django.db import models

# Create your models here.


class Comando(models.Model):

    lat = models.FloatField(verbose_name='lat', null=True, blank=True)
    lng = models.FloatField(verbose_name='lng', null=True, blank=True)
    keyword = models.CharField(verbose_name='keyword', null=True, blank=True, max_length=200)
    city = models.CharField(verbose_name='city', null=True, blank=True, max_length=200)
    state = models.CharField(verbose_name='state', null=True, blank=True, max_length=200)
    country = models.CharField(verbose_name='country', null=True, blank=True, max_length=200)