import requests
import json
import time

GMAPS_API_KEY = 'AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'

class startpoint():
#https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=<latitude>,<longitude>&radius=<radio>&type=<type>&key=<GMAPS_API_KEY
    latitude = 20.5923144
    longitude = -100.3878238
    radio = 10000
    type = 'bar'

r = startpoint()
counter=0

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=20.5915833,-100.4075112&radius=1000&type=bar&key=AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ'
response = json.loads(requests.get(url).text)
lugares = json.dumps(response, indent=4, sort_keys=True)






while True:
    time.sleep(2)
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + str(response["next_page_token"]) + '&key=' + GMAPS_API_KEY
    response = json.loads(requests.get(url).text)
    try:
        if response["next_page_token"]:
            #print(json.dumps(response["results"][1], indent=4, sort_keys=True))
            lugares += "\n" + json.dumps(response, indent=4, sort_keys=True)
    except KeyError:
        lugares += "\n" + json.dumps(response, indent=4, sort_keys=True)
        print("Bye")
        break


f = open("lugaresAle.json", "w+")
f.write(lugares)
f.close()






