from django.shortcuts import render
from lugares.models import *
from django.shortcuts import get_object_or_404
from  django.conf import  settings


#Visualizar partidos en la landing page
def detalle_lugar(request, nombre_lugar,id_lugar):
    l = get_object_or_404(Lugar, id=id_lugar)
    imagenes = Imagen.objects.filter(lugar=l)
    gkey=settings.GMAPS_API_KEY_JS
    return render(request, 'lugares/details.html' , { 'lugar': l, 'imagenes': imagenes, 'gkey':gkey })

