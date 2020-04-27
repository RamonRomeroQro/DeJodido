from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from lugares.models import Ciudad, Estado, Pais, Lugar, Imagen
from django.http import HttpResponse
import pprint
from django.http import JsonResponse
from itertools import chain
import os


# Visualizar partidos en la landing page
def landing(request):
    return render(request, 'landing/index.html')


# Visualizar partidos en la landing page
def log(request):
    return render(request, 'landing/log.html')


def test(request):
    return render(request, 'landing/test.html')


def test_slider(request):
    return render(request, 'landing/test_slider.html')


def listaciudades(request):
    if request.is_ajax():
        q = request.POST.get('term', '')
        cities = Ciudad.objects.filter(
            nombre__contains=q).annotate(Count('nombre'))[:3]
        results = []
        for c in cities:
            place_json = {}
            place_json = c.nombre + ", " + c.estado.nombre + ", " + c.estado.pais.nombre
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_ciudades(request):

    ciudades = Ciudad.objects.all()
    data = {}

    for c in ciudades:
        data.update({c.nombre + ", " + c.estado.nombre +
                     ", " + c.estado.pais.nombre: None})
    #data.update({'Usar Ubicacion Actual': None})
    return JsonResponse(data)


def validar_email(request):
    email = request.GET.get('email', None)

    data = {
        'is_not_taken': not (User.objects.filter(email__iexact=email).exists())
    }

    return JsonResponse(data)
