from django.shortcuts import render
from django.http import HttpResponse
from .models import Ciudad

import requests
import json
from django.db.models import Count
from .models import Lugar
import  time

GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=<latitude>,<longitude>&radius=<radio>&type=<type>&key=<GMAPS_API_KEY

#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#POR QUESTIONES DE FILTRADO, SE USA KEYWORD EN LUGAR DE TYPE
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def busquedaGMaps(latitude,longitude, type):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + ',' + longitude + '&radius=5000' + '&keyword=' + type + '&key=' + GMAPS_API_KEY
    print (url)
    response = json.loads(requests.get(url).text)
    return response

def saveLocal(arr, q):

    count = 0
    while (count < len(arr['results'])):



        name=  (arr['results'][count]['name'])
        place_id= (arr['results'][count]['place_id'])

        try:
            rating =  (arr['results'][count]['rating'])
        except KeyError:
            rating = (0)

        vicinity=  (arr['results'][count]['vicinity'])
        lat =  (arr['results'][count]['geometry']['location']['lat'])
        lng =  (arr['results'][count]['geometry']['location']['lng'])
        '''
        t=0
        while (t < len(arr['results'][count]['types'])):
            print (arr['results'][count]['types'][t])
            t=t+1
        '''

        obj, created = Lugar.objects.get_or_create(
            nombre= name,
            lat = lat,
            lng = lng,
            direccion = vicinity,
            place_id = place_id,
            rating = rating
        )
        #print ('>>>>>>>>>>>>>>'+obj.nombre)

        q.append(obj)





        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + str(arr["next_page_token"]) + '&key=' + GMAPS_API_KEY
        #print (url)
        new = json.loads(requests.get(url).text)
        print (new['status'])
        saveLocal(new, q)



        #print ('eof')

     # sort by age

    return  q







def inicio(request):

    type1 = 'bar'

    if (request.method=='POST'):


                response = busquedaGMaps(request.POST['latitude'], request.POST['longitude'], type1)
                lista=[]
                q=[]
                lista = saveLocal(response, q)

                #print  (lista)

                return render(request, 'busqueda/lista.html', {'lista': lista})




    else:
        return render(request, 'busqueda/inicio.html')

