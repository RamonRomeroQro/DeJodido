
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

import json, requests

nombre = ""
direccion = ""
latitud = 0.0
longitud = 0.0
botana = None
validado = False
rating = 0.0
precio = 0.0
id_google = ''
id_yelp = ''
id_foursquare = ''
id_facebook = ''
tags = None
ciudad = 777

count_rt=0
count_pr=0

def printeo():
    print (nombre)
    print (direccion)
    print (latitud)
    print (longitud)
    print (botana)
    print (validado)
    print (rating)
    print (precio)
    print (id_google)
    print (id_yelp)
    print (id_foursquare)
    print (id_facebook)
    print (tags)
    print (ciudad)


def busquedaYelp(regex, lat, lng):
    url = "https://api.yelp.com/v3/businesses/search?term="+regex+"&latitude="+lat+"&longitude="+lng
    headers={'Authorization':'Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx'}
    response = json.loads(requests.get(url,headers=headers).text)
    try:
        a=len(response['businesses'])
        if (a > 0):
            try:

                print ("yelp_name: " + response['businesses'][0]['name'])
                print ("yelp_id: " + response['businesses'][0]['id'])

                print ("yelp_rating: " + str(response['businesses'][0]['rating']))
                print ("yelp_price: " + response['businesses'][0]['price'])
            except KeyError:
                print('NO HAY INFORMACION DE YELP')
        else:
            print('NO HAY INFORMACION DE YELP')

    except KeyError:
        print('NO HAY INFORMACION DE YELP')


def busquedaFoursquare(regex,lat,lng):
    url = 'https://api.foursquare.com/v2/venues/search'

    params2 = dict(
        client_id='0U1M35P3PWR3C3NW41MCVIP1OPSYMJJPXDG5EOFPNWTFVUY5',
        client_secret='2P50CX0GU1TBMLTWXO5052XV5JKTT03A3EAQAFXZWWZ0YLTK',
        v='20180323',
    )

    params = dict(
        client_id='0U1M35P3PWR3C3NW41MCVIP1OPSYMJJPXDG5EOFPNWTFVUY5',
        client_secret='2P50CX0GU1TBMLTWXO5052XV5JKTT03A3EAQAFXZWWZ0YLTK',
        v='20180323',
        ll=str(lat)+','+str(lng),
        name=regex,
        intent='match',
        limit=4
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    try:

        print('foursquare_name: ' +data['response']['venues'][0]['name'])
        print('foursquare_id: ' +data['response']['venues'][0]['id'])

        urlrating='https://api.foursquare.com/v2/venues/'+data['response']['venues'][0]['id']
        resp2 = requests.get(url=urlrating, params=params2)
        data2 = json.loads(resp2.text)


        try:
            print('foursquare_price: ' + str((data2['response']['venue']['price']['tier'])))
            print('foursquare_rating: ' + str((data2['response']['venue']['rating'])/2))
        except KeyError:
            print('NO HAY INFORMACION DE FOURSQUARE')

    except (KeyError, IndexError) as e:
        print('NO HAY INFORMACION DE FOURSQUARE')




def busquedaFacebook(regex, lat, lng):
    # specific="bar los amigos"
    token = '2016535901926533|shNiHD3XAmykHQ0MiFImMpUX4GE'
    urlFB = "https://graph.facebook.com/v3.0/search?type=place&center=" + lat + "," + lng + "&distance=5000&q=" + regex + "&fields=name,link,overall_star_rating,price_range,website&access_token=" + token
    response = json.loads(requests.get(urlFB).text)
    #pprint.pprint(response)
    try:
        if len(response['data']) >0:
            print('facebook_name: ' + response['data'][0]['name'])
            print('facebook_ID: ' + response['data'][0]['id'])
            print('facebook_page: ' + response['data'][0]['link'])
            try:
                print('facebook_rating: ' + str(response['data'][0]['overall_star_rating']))
                print('facebook_price: ' + response['data'][0]['price_range'])
            except KeyError:
                print ('NO HAY INFORMACION DE FACEBOOK')
        else:
            print ('NO HAY INFORMACION DE FACEBOOK')
    except KeyError:
        print ('NO HAY INFORMACION DE FACEBOOK')



def busquedaGMaps(latitude,longitude, kyword):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + ',' + longitude + '&radius=5000' + '&keyword=' + kyword + '&key=' + GMAPS_API_KEY
    #print (url)
    response = json.loads(requests.get(url).text)
    #pprint.pprint(response)
    return response

def saveLocal(arr):

    count = 0
    while (count < len(arr['results'])):
        print ('google_nombre: '+ arr['results'][count]['name'])
        print  ('google_id: '+ arr['results'][count]['place_id'])
        try:
            print  ('google_rating: ', arr['results'][count]['rating'])
        except KeyError:
            print  ('google_rating: Desconocido')

        print  ('google_direccion: ' + (arr['results'][count]['vicinity']))
        print  ('google_latitud: ' ,arr['results'][count]['geometry']['location']['lat'])
        print ('google_longitud: ' , arr['results'][count]['geometry']['location']['lng'])


        #pprint.pprint(arr)

        try:
            print  ('google_price: ' + arr['results'][count]['price_level'])
        except KeyError:
            print ('PRICE NO DISPONIBLE')


        print ('-----------')
        busquedaFacebook(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))
        print ('-----------')
        busquedaYelp(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))
        print ('-----------')
        busquedaFoursquare(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))

        print  ('\n')
        print  ('<><><><><><><><><><><><><><>')
        print  ('\n')


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


response = busquedaGMaps(lat, lng, 'nightclub')
saveLocal(response)


#pprint.pprint(response)
#saveLocal(response)
