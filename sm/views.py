from lugares.models import Imagen
from django.shortcuts import render
from lugares.models import *
from django.shortcuts import get_object_or_404
from  django.conf import  settings
from django.shortcuts import redirect

import json
import requests
import datetime
from django.http import HttpResponse
from usuarios.forms import UsuarioReview
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required




#Visualizar partidos en la landing page
@login_required
def lugares(request):
    numbers=Lugar.objects.all().order_by('nombre')
    return render(request, 'sm/list_all.html', {'numbers':numbers})

@login_required
def detalle_lugar(request, nombre_lugar,id_lugar):
    l = get_object_or_404(Lugar, id=id_lugar)
    gkey=settings.GMAPS_API_KEY_JS
    formresena=UsuarioReview(prefix="resena")
    return render(request, 'lugares/details.html' , { 'lugar': l, 'gkey':gkey, 'forma':formresena })

@login_required
def update_place (request,  id_lugar):
    l = get_object_or_404(Lugar, id=id_lugar)
    previous=str(l.status)
    if (request.POST['update_place']=='True'):
        l.status=True
        l.save()

        mensaje = str('Update: Nombre: '+l.nombre+' id: '+ str(l.id)+' id google: '+ l.id_google+' status: '+ previous+' -> '+ str(l.status))
        messages.success(request, mensaje)


    elif (request.POST['update_place']=='False'):
        l.status=False
        l.save()


        mensaje = str('Update: Nombre: '+l.nombre+' id: '+ str(l.id)+' id google: '+ l.id_google+' status: '+ previous+' -> '+ str(l.status))
        messages.success(request, mensaje)


    elif (request.POST['update_place']=='Delete'):
        mensaje = str('Borrano: Nombre: '+l.nombre+' id: '+ str(l.id)+' id google: '+ l.id_google+' status: '+ str(l.status))
        l.delete()
        messages.warning(request, mensaje)

    else:
        mensaje="Error, intenta de nuevo"
        messages.error(request, mensaje)


    #l.status=
    return HttpResponseRedirect(reverse('sm:lugares'))