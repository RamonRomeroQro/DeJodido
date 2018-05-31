
#curl -X GET -H "Authorization: Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx"  "https://api.yelp.com/v3/businesses/search?term=alquimia&latitude=20.5732807&longitude=-100.3614291"





import requests, json, pprint
import shutil


#pprint.pprint(response)


def busquedaGMaps(latitude,longitude, kyword, c, e, p):
    GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + ',' + longitude + '&radius=5000' + '&keyword=' + kyword + '&key=' + GMAPS_API_KEY
    #print (url)
    response = json.loads(requests.get(url).text)
    #pprint.pprint(response)
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



        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)
        GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + str(arr["next_page_token"]) + '&key=' + GMAPS_API_KEY
        #print (url)
        new = json.loads(requests.get(url).text)
        #print (new['status'])
        #pprint.pprint(new)
        saveLocal(new, kyword, c, e, p)
        #print ('eof')
     # sort by age


lat='20.5924074'
lng='-100.3788854'
keyword='Bar varela'
city="QRO"
state="QRO"
country="MEX"
options={'lat': lat, 'lng': lng, 'keyword':keyword, 'city':city, 'state': state, 'country':country}

response = busquedaGMaps(str(options['lat']), str(options['lng']), str(options['keyword']), str(options['city']), str(options['state']), str(options['country']))
saveLocal(response['response'], response['kyword'], response['c'], response['e'], response['p'])

