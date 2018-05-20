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
        print ('>>>>>>>>>>>>>>'+obj.nombre)

        q.append(obj)





        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + str(arr["next_page_token"]) + '&key=' + GMAPS_API_KEY
        print (url)
        new = json.loads(requests.get(url).text)
        print (new['status'])
        saveLocal(new, q)

    else:

        print ('eof')

    return  q





def inicio(request):

    type1 = 'bar'

    if (request.method=='POST'):


        if ( request.POST['city']=='' ):

            if ( request.POST['latitude'] == '' or   request.POST['longitude']==''):

                return render(request, 'busqueda/inicio.html', {'error': "ingrese nombre de ciudad o use ubicacion"})

            else:

                response = busquedaGMaps(request.POST['latitude'], request.POST['longitude'], type1)
                lista=[]
                q=[]
                lista = saveLocal(response, q)

                print  (lista)

                return render(request, 'busqueda/lista.html', {'lista': lista})


        else:


            lugar=[]
            lugar = request.POST['city'].split(', ')
            instance = Ciudad.objects.get(ciudad=lugar[0], pais=lugar[1])
            response = busquedaGMaps(str(instance.latitud), str(instance.longitud), type1)
            lista = []
            q = []
            lista = saveLocal(response, q)

            print  (lista)

            return render(request, 'busqueda/lista.html', {'lista': lista})


    else:
        return render(request, 'busqueda/inicio.html')


def listaciudades(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        cities = Ciudad.objects.filter(ciudad__icontains=q).annotate(Count('ciudad'))[:3]
        results = []
        for c in cities:
            place_json = {}
            place_json = c.ciudad + ", " + c.pais
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

'''


# {u'results': [{u'address_components': [{u'long_name': u'1600',
#                                         u'short_name': u'1600',
#                                         u'types': [u'street_number']},
#                                        {u'long_name': u'Amphitheatre Pkwy',
#                                         u'short_name': u'Amphitheatre Pkwy',
#                                         u'types': [u'route']},
#                                        {u'long_name': u'Mountain View',
#                                         u'short_name': u'Mountain View',
#                                         u'types': [u'locality',
#                                                    u'political']},
#                                        {u'long_name': u'San Jose',
#                                         u'short_name': u'San Jose',
#                                         u'types': [u'administrative_area_level_3',
#                                                    u'political']},
#                                        {u'long_name': u'Santa Clara',
#                                         u'short_name': u'Santa Clara',
#                                         u'types': [u'administrative_area_level_2',
#                                                    u'political']},
#                                        {u'long_name': u'California',
#                                         u'short_name': u'CA',
#                                         u'types': [u'administrative_area_level_1',
#                                                    u'political']},
#                                        {u'long_name': u'United States',
#                                         u'short_name': u'US',
#                                         u'types': [u'country',
#                                                    u'political']},
#                                        {u'long_name': u'94043',
#                                         u'short_name': u'94043',
#                                         u'types': [u'postal_code']}],
#                u'formatted_address': u'1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA',
#                u'geometry': {u'location': {u'lat': 37.4216227,
#                                            u'lng': -122.0840263},
#                              u'location_type': u'ROOFTOP',
#                              u'viewport': {u'northeast': {u'lat': 37.424770299999999,
#                                                           u'lng': -122.0808787},
#                                            u'southwest': {u'lat': 37.418475100000002,
#                                                           u'lng': -122.0871739}}},
#                u'types': [u'street_address']}],
#  u'status': u'OK'}

test = json.dumps([s['geometry']['location'] for s in jsonResponse['results']], indent=3)
print(test)
# [
#    {
#       "lat": 37.4216227, 
#       "lng": -122.0840263
#    }
# ]
jsonResponse is a dict.
jsonResponse['results'] is a list of dicts.
The loop for s in jsonResponse['results'] assigns s to a dict for each iteration through the loop.
s['geometry'] is a dict.
s['geometry']['location'] (finally!) contains the latitude/longitude dict.



'''