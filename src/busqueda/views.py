from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'busqueda/inicio.html')


def lista_de_resultados(request):
    print(request.POST["lugar"])
    return render(request, 'busqueda/list.html')




'''

17
down vote
The key to understanding jsonResponse's format is to print it out:

import urllib, json
import pprint

URL2 = "http://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false"

googleResponse = urllib.urlopen(URL2)
jsonResponse = json.loads(googleResponse.read())
pprint.pprint(jsonResponse)
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