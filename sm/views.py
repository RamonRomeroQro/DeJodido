from lugares.models import Imagen
from django.shortcuts import render
from lugares.models import *
from django.shortcuts import get_object_or_404
from  django.conf import  settings
import json
import requests
import datetime
from django.http import HttpResponse
from usuarios.forms import UsuarioReview
from django.http import HttpResponseRedirect


#Visualizar partidos en la landing page
def imagenes(request):
    imagenes=Imagen.objects.all()
    return render(request, 'sm/imagenes.html', {'imagenes':imagenes})

