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



def busqueda(request):
    fullname = request.POST['city']
    parsedlocation = fullname.split(', ')
    city = parsedlocation[0]
    state = parsedlocation[1]
    country = parsedlocation[2]
    qpais = Pais.objects.get(nombre=country)
    qstate = Estado.objects.filter(pais=qpais).get(nombre=state)
    qcity = Ciudad.objects.filter(estado=qstate).get(nombre=city)
    lugares = Lugar.objects.filter(ciudad=qcity)
    lugar =[]

    presupuesto = request.POST.getlist('presupuesto')

    for lug in lugares.filter(precio__range=(min(presupuesto), max(presupuesto))):
        lugar.append(lug)



    return render(request, 'lugares/list.html', {'lugares': lugar })