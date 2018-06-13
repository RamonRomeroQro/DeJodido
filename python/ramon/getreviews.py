
import pprint
import requests
import json
import datetime
from html.parser import HTMLParser
from html.entities import name2codepoint





GMAPS_API_KEY = 'AIzaSyAbXCwLfYYs3Hyb8XXvxm5-wzvRNm2JI3Y'
GMAPS_API_KEY_JS= 'AIzaSyC3EcXKhyPwcWgVlPAzDGplTa00HkKD0KQ'

from html.parser import HTMLParser


def googleReviews(g_id):
    detalle_url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + g_id + '&key=' + GMAPS_API_KEY
    new = json.loads(requests.get(detalle_url).text)
    if(new['status']=='OK'):
        i=0
        html='<h2>Google</h2><ul class="collection">'


        while i<len(new['result']['reviews']):
            autor = new['result']['reviews'][i]['author_name']
            url = new['result']['reviews'][i]['author_url']
            photo = new['result']['reviews'][i]['profile_photo_url']
            rate = new['result']['reviews'][i]['rating']
            relativetime = new['result']['reviews'][i]['relative_time_description']
            text = new['result']['reviews'][i]['text']
            time = new['result']['reviews'][i]['time']

            html=html+'<a href="'+url+'">'
            html=html+'<li class="collection-item avatar">'
            html=html+'<img src="'+photo+'" alt="" class="circle">'
            html=html+'<span class="title">'+autor+'</span>'
            html=html+'<p>'+text+'</p>'
            html=html+'<p>'
            for i in range(0,rate):
                html=html+'&#x2b50;'
            html=html+'</p>'
            html=html+'<p>'+str(rate)+'</p>'
            html = html + '<p>' +datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')+'</p>'
            html = html + '<p>' +relativetime+'</p>'
            html=html+'<a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>'
            html=html+'</li>'
            html=html+'</a>'


            i=i+1

        html=html+'</ul>'

        return (html)
    else:
        return 'error'

def yelpReviews(y_id):
    url = 'https://api.yelp.com/v3/businesses/'+y_id+'/reviews'
    headers = {
        'Authorization': 'Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx'}
    response = json.loads(requests.get(url, headers=headers).text)
    html='<h2>Yelp</h2><ul class="collection">'
    for i in range(0,len(response['reviews'])):
        rating=response['reviews'][i]['rating']
        text=response['reviews'][i]['text']
        time=response['reviews'][i]['time_created']
        url=response['reviews'][i]['url']
        usuario=response['reviews'][i]['user']['name']
        profile=response['reviews'][i]['user']['image_url']

        html=html+'<a href="'+url+'">'
        html=html+'<li class="collection-item avatar">'
        html=html+'<img src="'+profile+'" alt="" class="circle">'
        html=html+'<span class="title">'+usuario+'</span>'
        html=html+'<p>'+text+'</p>'
        html=html+'<p>'
        for i in range(0,rating):
            html=html+'&#x2b50;'
        html=html+'</p>'
        html=html+'<p>'+str(rating)+'</p>'
        html = html + '<p>' +time+'</p>'
        html=html+'<a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>'
        html=html+'</li>'
        html=html+'</a>'





    html=html+'</ul>'

    return (html)

def foursquareReviews(id):
    url = 'https://api.foursquare.com/v2/venues/'+id+'/tips'
    params = dict(
        client_id='0U1M35P3PWR3C3NW41MCVIP1OPSYMJJPXDG5EOFPNWTFVUY5',
        client_secret='2P50CX0GU1TBMLTWXO5052XV5JKTT03A3EAQAFXZWWZ0YLTK',
        v='20180323',
        limit='100',
        offset='200',
        sort='popular'
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    if (data['meta']['code']==200):
        html='<h2>FourSquare</h2><ul class="collection">'

        for i in range(0, len(data['response']['tips']['items'])):

            likes=data['response']['tips']['items'][i]['agreeCount']
            url=data['response']['tips']['items'][i]['canonicalUrl']
            unixtime= data['response']['tips']['items'][i]['createdAt']
            dislikes=data['response']['tips']['items'][i]['disagreeCount']
            photoplace=        data['response']['tips']['items'][i]['photourl']
            text=        data['response']['tips']['items'][i]['text']
            usuario=                data['response']['tips']['items'][i]['user']['firstName']+' '+data['response']['tips']['items'][i]['user']['lastName']
            profile= data['response']['tips']['items'][i]['user']['photo']['prefix']+data['response']['tips']['items'][i]['user']['photo']['suffix']

            html = html + '<a href="' + url + '">'
            html = html + '<li class="collection-item avatar">'
            html = html + '<img src="' + profile + '" alt="" class="circle">'
            html = html + '<span class="title">' + usuario + '</span>'
            html = html + '<p>' + text + '</p>'
            html = html + '<p>Likes' + str(likes) + '</p>'
            html = html + '<p>Dislikes' + str(dislikes) + '</p>'
            html = html + '<img src="'+photoplace+'" height="300px" width="auto">'
            html = html + '<p>' +datetime.datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d %H:%M:%S')+'</p>'
            html = html + '<a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>'
            html = html + '</li>'
            html = html + '</a>'

        html = html + '</ul>'
        print (html)
        return html
    else:
        return 'error'














google='ChIJNcvMCixb04URIow3D--DoAw'
facebook='498612900166968'
yelp='xLRJ5jdrE3fw_2wLqlt-hQ'
foursquare='4bd26574462cb713dd67dc07'
pag='https://www.facebook.com/wicklowqro/reviews196002153777406'



googleReviews(google)
print ('\n')
yelpReviews(yelp)
print ('\n')
foursquareReviews(foursquare)
'''

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
        try:
            facebook_link = response['data'][0]['link']
        except KeyError:
            facebook_link="404"

    except (KeyError, IndexError) as e:
        facebook_id = -100
        facebook_rating = -100
        facebook_price = -100
        facebook_link = "404"

    return {'facebook_id': facebook_id, 'facebook_rating': facebook_rating, 'facebook_price': facebook_price, 'facebook_link': facebook_link}


def busquedaGMaps(latitude,longitude, kyword, c, e, p):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + ',' + longitude + '&radius=5000' + '&keyword=' + kyword + '&key=' + settings.GMAPS_API_KEY
    #print (url)

    response = json.loads(requests.get(url).text)
    print(response['status'])
    return {'response': response, 'kyword': kyword, 'c': c, 'e': e, 'p':p}

def saveLocal(arr, kyword, c, e, p):

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
        creacioDBO(gobj, fobj, sobj, yobj, kyword, c, e, p)
        print ('>>>>>>>>>>>>'+gobj['google_nombre'])
        #pprint.pprint(gobj)
        #pprint.pprint(fobj)
        #pprint.pprint(yobj)
        #pprint.pprint(sobj)

        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)

        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + str(arr["next_page_token"]) + '&key=' + settings.GMAPS_API_KEY
        #print (url)
        new = json.loads(requests.get(url).text)
        #print (new['status'])
        #pprint.pprint(new)
        saveLocal(new, kyword, c, e, p)
        #print ('eof')
     # sort by age




#pprint.pprint(response)
#saveLocal(response)
'''