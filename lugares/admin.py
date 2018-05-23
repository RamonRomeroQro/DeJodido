
# Register your models here.


from django.contrib import admin
from .models import Tags, Estado, Ciudad, Pais, Lugar


admin.site.register(Tags)
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Lugar)