from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

class startpoint():
#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=<latitude>,<longitude>&radius=<radio>&type=<type>&key=<GMAPS_API_KEY
    latitude=0
    longitude=0
    radio=0
    tipodebusqueda=0

    def __init__(self):
        self.latitude = 0
        self.longitude = 0
        self.radio = 0
        self.type = 0


    def __init__(self, lat, long, type):
        self.latitude = lat
        self.longitude = long
        self.radio = 5000
        self.type = type



#connection = pymongo.MongoClient("mongodb://localhost")
#db=connection.jodido
#db.busquedas.insert(response)




def inicio(request):
    if (request.method=='POST'):


        r = startpoint(request.POST['latitude'], request.POST['longitude'], 0)
        types=''
        if r.type==0:
            types='amusement_park,aquarium,art_gallery,bar, bowling_alley,cafe,campground,'
            types=types+'casino,church,city_hall,local_government_office,movie_theater,'
            types=types+'museum,night_club,park,restaurant,shopping_mall,spa,'
            types=types+'stadium,synagogue,zoo'
        else:
            types='bar'



        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(r.latitude) + ',' + str(
            r.longitude) + '&radius=' + str(r.radio) + '&types=' + types + '&key=' + GMAPS_API_KEY

        response = json.loads(requests.get(url).text)

        html = url+'\n\n'+(str(response['status']))





        return HttpResponse(html)




    else:
        return render(request, 'busqueda/inicio.html')


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