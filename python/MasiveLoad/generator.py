
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


def busquedaYelp(regex, lat, lng):
    url = "https://api.yelp.com/v3/businesses/search?term="+regex+"&latitude="+lat+"&longitude="+lng
    headers={'Authorization':'Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx'}
    response = json.loads(requests.get(url,headers=headers).text)
    print (response['businesses'][0]['id'])
    print (response['businesses'][0]['rating'])
    print (response['businesses'][0]['price'])

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

    if len(data['response']['venues']) > 0:

        print('foursquare_name: ' +data['response']['venues'][0]['name'])
        print('foursquare_id: ' +data['response']['venues'][0]['id'])

        urlrating='https://api.foursquare.com/v2/venues/'+data['response']['venues'][0]['id']
        resp2 = requests.get(url=urlrating, params=params2)
        data2 = json.loads(resp2.text)


        try:
            print('foursquare_price: ' + str((data2['response']['venue']['price']['tier'])))
            print('foursquare_rating: ' + str((data2['response']['venue']['rating'])/2))
        except KeyError:
            print('foursquare_rating: NO DISP')

    else:
        print('NO HAY INFORMACION DE FOURSQUARES')





def busquedaFacebook(regex, lat, lng):
    # specific="bar los amigos"
    token = 'EAAcqB1ocdIUBAMxl7Gc0ad5IOOKqzVugvwcxVlg6Nh2HGxLnoO2yZATS8KOiqzFqBElYHI72VLBPYrgmfWtPjgaQtH6tmzzILsGD2wtSFyX09vI5GpAZAch8IlPaESr7dCZBZAVEK1chyDNHc5xw8OfP8JTE3Ve2ZCrylmz9x40ztZCbsEg6ZCB1NelCxMEeBoZD'

    urlFB = "https://graph.facebook.com/v3.0/search?type=place&center=" + lat + "," + lng + "&distance=5000&q=" + regex + "&fields=name,link,overall_star_rating,website&access_token=" + token
    response = json.loads(requests.get(urlFB).text)

    try:
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

    except KeyError:
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
        busquedaFoursquare(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))


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
