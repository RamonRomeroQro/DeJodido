
import requests
import json
import time
import pprint

GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=<latitude>,<longitude>&radius=<radio>&type=<type>&key=<GMAPS_API_KEY

#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#POR QUESTIONES DE FILTRADO, SE USA KEYWORD EN LUGAR DE TYPE
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

omits=['el', 'la', 'los', 'las', 'bar', 'un', 'un', 'restaurante', ]



def busquedaFacebook(regex, lat, lng):
    # specific="bar los amigos"
    token = 'EAAcqB1ocdIUBAJd6E0kAQaalP46qrbMdDosbhiVZAOO9O10yoccZCqQZCkjoBbD8Gujb8gMQ8RdZAs9BzDKUOo8pxqVz1I6EKkrLSBDZB3wYQ63YblQqxJqGNzTkrRSLw00oaL7yCAaybyEWetYAYPguSgL2MbFrZBD1fp5rhs2g6vyyfTZAEApecoIdLNJo4Bkg4MIeSxtkwZDZD'

    urlFB = "https://graph.facebook.com/v3.0/search?type=place&center=" + lat + "," + lng + "&distance=5000&q=" + regex + "&fields=name,link,overall_star_rating,website&access_token=" + token
    response = json.loads(requests.get(urlFB).text)
    if len(response['data']) >0:
        print('nombre FB: ' + response['data'][0]['name'])
        print('facebook_ID: ' + response['data'][0]['id'])
        print('facebook_ID: ' + response['data'][0]['link'])

        try:
            print('rating FB: ' + str(response['data'][0]['overall_star_rating']))

        except KeyError:
            print ('rating FB: NO DISP')
    else:

        print ('info de fb no disponible')


def busquedaGMaps(latitude,longitude, kyword):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + ',' + longitude + '&radius=5000' + '&keyword=' + kyword + '&key=' + GMAPS_API_KEY
    #print (url)
    response = json.loads(requests.get(url).text)
    #pprint.pprint(response)
    return response

def saveLocal(arr):

    count = 0
    while (count < len(arr['results'])):


        print (arr['results'][count]['name'])
        print  (arr['results'][count]['place_id'])

        try:
            print  ('rating Google=  ',  arr['results'][count]['rating'])
        except KeyError:
            print  ('rating Google= Desconocido')

        print  ('Direccion: ' + (arr['results'][count]['vicinity']))
        print  (arr['results'][count]['geometry']['location']['lat'])
        print (arr['results'][count]['geometry']['location']['lng'])

        busquedaFacebook(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))



        print  ('---------------------')
        '''
        
        
        obj, created = Lugar.objects.get_or_create(
            nombre= name,
            lat = lat,
            lng = lng,
            direccion = vicinity,
            place_id = place_id,
            rating = rating
        )
        '''
        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + str(arr["next_page_token"]) + '&key=' + GMAPS_API_KEY
        #print (url)
        new = json.loads(requests.get(url).text)
        #print (new['status'])
        #pprint.pprint(new)
        saveLocal(new)
        #print ('eof')
     # sort by age




lat='20.5924074'
lng='-100.3788854'
kyword='bar'
nombre='bar varela'
nombre='bar los amigos'
nombre='bar el sevillano'




response = busquedaGMaps(lat, lng, kyword)
saveLocal(response)


#pprint.pprint(response)
#saveLocal(response)
