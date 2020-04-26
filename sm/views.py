from django.shortcuts import render
from lugares.models import *
from django.shortcuts import get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Comando
import deajodido.settings.final as settings

@login_required
def imagenes(request):
    nulls = Imagen.objects.filter(status=None).filter(lugar__status=True).order_by("lugar")
    trues = Imagen.objects.filter(status=True).filter(lugar__status=True).order_by("lugar")
    falses = Imagen.objects.filter(status=False).filter(lugar__status=True).order_by("lugar")
    return render(request, 'sm/imagenes_all.html', {'falses':falses,'trues':trues,'nulls':nulls})


#FIX FOR NEXT UPDATE
@login_required
def quickimages(request):
    q = Imagen.objects.filter(status=None).filter(lugar__status=True).order_by("lugar")
    n= q.count()
    s = q.first()
    return render(request, 'sm/quick.html', {'s':s, 'n':n})

@login_required
def atrue(request, id_imagen):
    i=Imagen.objects.get(id=id_imagen)
    i.status=True
    i.save()
    return HttpResponseRedirect(reverse('sm:quickimages'))

@login_required
def afalse(request, id_imagen):
    i=Imagen.objects.get(id=id_imagen)
    i.status=False
    i.save()
    return HttpResponseRedirect(reverse('sm:quickimages'))





#Visualizar partidos en la landing page
@login_required
def lugares(request):
    numbers1=Lugar.objects.filter(status=True).order_by('nombre')
    numbers2=Lugar.objects.filter(status=False).order_by('nombre')
    numbers3=Lugar.objects.filter(status=None).order_by('nombre')

    return render(request, 'sm/list_all.html', {'numbers1':numbers1, 'numbers2':numbers2, 'numbers3':numbers3})

@login_required
def detalle_lugar(request, id_lugar):
    l = get_object_or_404(Lugar, id=id_lugar)
    gkey=settings.GMAPS_API_KEY
    return render(request, 'sm/details.html' , { 'lugar': l, 'gkey':gkey  })

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

    elif (request.POST['update_place']=='None'):
        l.status=None
        l.save()
        mensaje = str('Update: Nombre: '+l.nombre+' id: '+ str(l.id)+' id google: '+ l.id_google+' status: '+ previous+' -> '+ str(l.status))
        messages.success(request, mensaje)


    elif (request.POST['update_place']=='Delete'):
        mensaje = str('Borrado: Nombre: '+l.nombre+' id: '+ str(l.id)+' id google: '+ l.id_google+' status: '+ str(l.status))
        l.delete()
        messages.warning(request, mensaje)

    else:
        mensaje="Error, intenta de nuevo"
        messages.error(request, mensaje)


    #l.status=
    return HttpResponseRedirect(reverse('sm:lugares'))



@login_required
def update_image (request,  id_image):
    i = get_object_or_404(Imagen, id=id_image)
    previous=str(i.status)
    lugar=i.lugar

    if (request.POST['update_image']=='True'):
        i.status=True
        i.save()
        mensaje = str('Update: URL: '+i.imagen.url+' from: '+ lugar.nombre +' id: '+ str(i.id)+' status: '+ previous+' -> '+ str(i.status))
        messages.success(request, mensaje)


    elif (request.POST['update_image']=='False'):
        i.status=False
        i.save()


        mensaje = str('Update: URL: '+i.imagen.url+' from: '+ lugar.nombre +' id: '+ str(i.id)+' status: '+ previous+' -> '+ str(i.status))
        messages.success(request, mensaje)

    elif (request.POST['update_image'] == 'None'):
        i.status = None
        i.save()

        mensaje = str('Update: URL: ' + i.imagen.url + ' from: ' + lugar.nombre + ' id: ' + str(
            i.id) + ' status: ' + previous + ' -> ' + str(i.status))
        messages.success(request, mensaje)



    elif (request.POST['update_image']=='Delete'):
        mensaje = str('Borrado: URL: '+i.imagen.url+' from: '+ lugar.nombre +' id: '+ str(i.id)+' status: '+ previous+' -> '+ str(i.status))
        i.delete()
        messages.warning(request, mensaje)

    else:
        mensaje="Error, intenta de nuevo"
        messages.error(request, mensaje)


    #l.status=
    return HttpResponseRedirect(reverse('sm:detalle_lugar',  kwargs={'nombre_lugar': lugar.nombre,'id_lugar':lugar.id}))


from .master import exec_command

@login_required
def consola(request):
    return exec_command(request)




import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes

@login_required
def log(request, id_comando):
    c = get_object_or_404(Comando, id=id_comando)
    if os.path.exists(c.log_file_path):
        fl = open(c.log_file_path, 'r')
        mime_type, _ = mimetypes.guess_type(c.log_file_path)
        response = HttpResponse(fl, content_type=mime_type)
        response['Content-Disposition'] = f"attachment; filename="+ os.path.basename(c.log_file_path)
        return response
    raise Http404
