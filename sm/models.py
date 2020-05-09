from django.db import models
from django.conf import settings

import os
class Comando(models.Model):

    lat = models.FloatField(verbose_name='lat', null=True, blank=True)
    lng = models.FloatField(verbose_name='lng', null=True, blank=True)
    keyword = models.CharField(verbose_name='keyword', null=True, blank=True, max_length=200)
    city = models.CharField(verbose_name='city', null=True, blank=True, max_length=200)
    state = models.CharField(verbose_name='state', null=True, blank=True, max_length=200)
    country = models.CharField(verbose_name='country', null=True, blank=True, max_length=200)
    status_exec = models.BooleanField(verbose_name="execution result", blank=True, default=False)
    timestamp = models.DateTimeField(auto_now=True)
    log_file = models.FileField(upload_to='logs', verbose_name='logs', null=True, blank=True)

    def __str__(self):
        return "|".join(list(map(str, [self.lat, self.lng, self.keyword, self.city, self.state,
                                       self.country, self.timestamp.strftime("%d-%m-%Y-%H:%M")])))

    def delete(self):
        if os.path.isfile(self.log_file.path):
            os.remove(self.log_file.path)
        super(Comando, self).delete()
