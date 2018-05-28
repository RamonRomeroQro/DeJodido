import json
import requests
import time
import pprint

from lugares.models import Lugar, Ciudad, Estado, Pais
from lugares.models import Tags
GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'


omits=['el', 'la', 'los', 'las', 'bar', 'un', 'un', 'restaurante', ]

def city(c,e,p):
    pais, cr1 = Pais.objects.get_or_create(
        nombre=p
    )

    estado, cr2 = Estado.objects.get_or_create(
        nombre=e,
        pais=pais
    )


    ciudad, cr3 = Ciudad.objects.get_or_create(
        nombre=c,
        estado = estado
    )


    return ciudad

def taging(kw):
    tag, cr1 = Tags.objects.get_or_create(
        descripcion=kw
    )


    return tag

def creacioDBO(gobj, fobj, sobj, yobj, kw, c,e,p):

    rt=[gobj['google_rating'], yobj['yelp_rating'], sobj['foursquare_rating'], fobj['facebook_rating']]
    #pprint.pprint(rt)
    crt=rt.count(-100)
    sm=sum(rt)+(crt*100)
    d=len(rt)-crt
    try:
        avrt=sm/d
        rat=avrt
    except ZeroDivisionError:
        rat=-100


    rt=[gobj['google_price'], yobj['yelp_price'], sobj['foursquare_price'], fobj['facebook_price']]
    #pprint.pprint(rt)
    crt = rt.count(-100)
    sm = sum(rt) + (crt * 100)
    d = len(rt) - crt
    try:
        avrt=sm/d
        price=avrt
    except ZeroDivisionError:
        price=-100


    c=city(c, e, p)
    t=taging(kw)

    obj, created = Lugar.objects.get_or_create(
        nombre=gobj['google_nombre'],
        direccion = gobj['google_direccion'],
        latitud = gobj['google_latitud'],
        longitud = gobj['google_longitud'],
        botana = None,
        validado = False,
        id_google=gobj['google_id'],
        id_yelp = yobj['yelp_id'],
        id_foursquare = sobj['foursquare_id'],
        id_facebook = fobj['facebook_id'],
        ciudad = c,
        rating=rat,
        precio=price,

    )
    obj.tags.add(t)
    obj.save()

def busquedaYelp(regex, lat, lng):
    url = "https://api.yelp.com/v3/businesses/search?term="+regex+"&latitude="+lat+"&longitude="+lng
    headers={'Authorization':'Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx'}
    response = json.loads(requests.get(url,headers=headers).text)
    try:

        #print ("yelp_name: " + response['businesses'][0]['name'])
        yelp_id= (response['businesses'][0]['id'])
        try:
            yelp_rating= response['businesses'][0]['rating']
        except KeyError:
            yelp_rating = -100
        try:
            yelp_price = len(response['businesses'][0]['price'])
        except KeyError:
            yelp_price = -100

    except (KeyError, IndexError) as e:

        yelp_id = -100

        yelp_rating = -100

        yelp_price = -100


    return {'yelp_id': yelp_id, 'yelp_rating': yelp_rating, 'yelp_price': yelp_price}


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

        #print('foursquare_name: ' +data['response']['venues'][0]['name'])
        foursquare_id = data['response']['venues'][0]['id']

        urlrating='https://api.foursquare.com/v2/venues/'+data['response']['venues'][0]['id']
        resp2 = requests.get(url=urlrating, params=params2)
        data2 = json.loads(resp2.text)


        try:
            foursquare_price = (data2['response']['venue']['price']['tier'])
        except KeyError:
            foursquare_price = -100

        try:
            foursquare_rating = (data2['response']['venue']['rating']) / 2
        except KeyError:
            foursquare_rating = -100



    except (KeyError, IndexError) as e:
        foursquare_id=-100
        foursquare_price=-100
        foursquare_rating=-100

        #print('NO HAY INFORMACION DE FOURSQUARE')

    return {'foursquare_id': foursquare_id, 'foursquare_price': foursquare_price, 'foursquare_rating': foursquare_rating}





def busquedaFacebook(regex, lat, lng):
    # specific="bar los amigos"
    token = '2016535901926533|shNiHD3XAmykHQ0MiFImMpUX4GE'
    urlFB = "https://graph.facebook.com/v3.0/search?type=place&center=" + lat + "," + lng + "&distance=5000&q=" + regex + "&fields=name,link,overall_star_rating,price_range,website&access_token=" + token
    response = json.loads(requests.get(urlFB).text)
    #pprint.pprint(response)
    try:
        #print('facebook_name: ' + response['data'][0]['name'])
        facebook_id = response['data'][0]['id']
        #print('facebook_page: ' + response['data'][0]['link'])
        try:
            facebook_rating = response['data'][0]['overall_star_rating']
        except KeyError:
            facebook_rating=-100
        try:
            facebook_price = len(response['data'][0]['price_range'])
        except KeyError:
            facebook_price = -100

    except (KeyError, IndexError) as e:
        facebook_id = -100
        facebook_rating = -100
        facebook_price = -100
    return {'facebook_id': facebook_id, 'facebook_rating': facebook_rating, 'facebook_price': facebook_price}


def busquedaGMaps(latitude,longitude, kyword):
    GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + ',' + longitude + '&radius=5000' + '&keyword=' + kyword + '&key=' + GMAPS_API_KEY
    #print (url)
    response = json.loads(requests.get(url).text)
    #pprint.pprint(response)
    return response

def saveLocal(arr):

    count = 0
    while (count < len(arr['results'])):
        google_nombre =  arr['results'][count]['name']
        google_id = arr['results'][count]['place_id']
        try:
            google_rating=arr['results'][count]['rating']
        except KeyError:
            google_rating=-100

        google_direccion = arr['results'][count]['vicinity']
        google_latitud = arr['results'][count]['geometry']['location']['lat']
        google_longitud = arr['results'][count]['geometry']['location']['lng']

        try:
            google_price=arr['results'][count]['price_level']
        except KeyError:
            google_price= -100

        gobj={'google_nombre': google_nombre, 'google_id': google_id, 'google_rating':google_rating, 'google_direccion': google_direccion, 'google_latitud': google_latitud, 'google_longitud': google_longitud, 'google_price':google_price}
        fobj=busquedaFacebook(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))
        yobj=busquedaYelp(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))
        sobj=busquedaFoursquare(str(arr['results'][count]['name']), str(arr['results'][count]['geometry']['location']['lat']), str(arr['results'][count]['geometry']['location']['lng']))
        ###
        ###
        ###
        creacioDBO(gobj, fobj, sobj, yobj, 'bar' ,'Queretaro', 'Queretaro', 'Mexico')
        print (gobj['google_nombre'])

        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)
        GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

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


response = busquedaGMaps(lat, lng, kyword)
saveLocal(response)


#pprint.pprint(response)
#saveLocal(response)
