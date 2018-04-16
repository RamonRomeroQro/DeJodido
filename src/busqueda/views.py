from django.shortcuts import render

# Create your views here.

import urllib, json, ssl

from deajodido.settings import GMAPS_API_KEY
from django.http import HttpResponse

import urllib.request
import json
from django.http import JsonResponse

import requests
import json



def inicio(request):
    if (request.method=='POST'):
        '''
        print('post request')
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + request.POST[
            'latitude'] + ',' + request.POST['longitude'] + '&radius=' + request.POST[
                  'radio'] +'&type= point_of_interest'+ '&key='+GMAPS_API_KEY


        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars

        googleResponse = urllib.request.urlopen(url, context=gcontext)


        jsonResponse = json.loads(googleResponse.read())
        
        return HttpResponse(jsonResponse["status"])
        
        '''



        # This restores the same behavior as before.
        '''
        import ssl

        conte= ssl._create_default_https_context

        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + request.POST[
            'latitude'] + ',' + request.POST['longitude'] + '&radius=' + request.POST[
                  'radio'] + '&type= point_of_interest' + '&key='+GMAPS_API_KEY

        req = urllib.request.Request(url)
        conte.verify_mode = ssl.CERT_NONE
        conte.check_hostname = None
        conte.sock = None
        conte.wrap_socket = None

        #errpor 400, in form request


        ##parsing response

        print( urllib.request.urlopen(req, context=conte).read())
        r = urllib.request.urlopen(req, context=conte).read()
        cont = json.loads(r.decode('utf-8'))
        counter = 0

        ##parcing json

        ##print formated
        # print (json.dumps(cont, indent=4, sort_keys=True))
        print( cont['status'] )
        
        '''



        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + request.POST[
            'latitude'] + ',' + request.POST['longitude'] + '&radius=' + request.POST[
                  'radio'] + '&type=bar' + '&key=' + GMAPS_API_KEY

        response = json.loads(requests.get(url).text)
        json_string = json.dumps(response)
        return render(request, "busqueda/lista.html", {'results': json_string})


        #html = '<html><body>Referred URL:  <a href="'+url+'">GO</a></body></html>'
        #response = JsonResponse({'foo': 'bar'})

        #return render(request, 'busqueda/lista.html', {'resultados': resultados})
        #return JsonResponse(response)



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