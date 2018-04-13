from django.db import models

# Create your models here.


from django.contrib.postgres.fields import JSONField
from django.db import models

class Busqueda(models.Model):
    presupuesto = models.FloatField(verbose_name='presupuesto', name='presupuesto', default=100)
    data = JSONField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name

