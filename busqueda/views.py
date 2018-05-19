from django.shortcuts import render
from django.http import HttpResponse
from .models import Ciudad

import requests
import json
from django.db.models import Count

GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=<latitude>,<longitude>&radius=<radio>&type=<type>&key=<GMAPS_API_KEY



def inicio(request):

    types = 'bar'

    if (request.method=='POST'):


        if ( request.POST['city']=='' ):

            if ( request.POST['latitude'] == '' or   request.POST['longitude']==''):

                return render(request, 'busqueda/inicio.html', {'error': "ingrese nombre de ciudad o use ubicacion"})

            else:

                url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' +  request.POST['latitude']+ ',' + request.POST['longitude'] + '&radius=5000' + '&types=' + types + '&key=' + GMAPS_API_KEY
                response = json.loads(requests.get(url).text)

                html = '<p>'+ url + '</p><p>' + (str(response['status'])) + '</p>'
                return HttpResponse(html)

        else:


            lugar=[]
            lugar = request.POST['city'].split(', ')

            instance = Ciudad.objects.get(ciudad=lugar[0], pais=lugar[1])



            url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(instance.latitud) + ',' + str(instance.longitud) + '&radius=5000' +  '&types=' + types + '&key=' + GMAPS_API_KEY

            response = json.loads(requests.get(url).text)

            html = '<p>' + url + '</p><p>' + (str(response['status'])) + '</p>'
            return HttpResponse(html)




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