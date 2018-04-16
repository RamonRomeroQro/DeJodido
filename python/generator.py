import requests
import json
import pymongo

GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

class startpoint():
#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=<latitude>,<longitude>&radius=<radio>&type=<type>&key=<GMAPS_API_KEY
    latitude=20.5923144
    longitude=-100.3878238
    radio=100
    type='bar'


r = startpoint()


url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(r.latitude) + ',' + str(r.longitude) + '&radius=' + str(r.radio) + '&type='+ r.type + '&key=' + GMAPS_API_KEY

response = json.loads(requests.get(url).text)



connection = pymongo.MongoClient("mongodb://localhost")
db=connection.jodido
db.busquedas.insert(response)

print(str(response['status']))