#  python3 manage.py shell < ./solve.py

from lugares.models import Lugar
import requests
import json

ll = Lugar.objects.all()

for l in ll:
    url1 = f"https://graph.facebook.com/v3.0/search?type=place&center={str(l.latitud)},{str(l.longitud)}&distance=5000&q={str(l.nombre)}&fields=name,link,overall_star_rating,price_range,website,phone&access_token=544112989843154|hBY39frkP-_8ovjnNsR3al2A08I"
    url2 = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={str(l.id_google)}&key=AIzaSyAyWoMzx2h4NwDk5NRmUqsODLC6vJKD_KA"
    new = json.loads(requests.get(url2).text)
    if new["status"] != "OK":
        print("Fallo recuperacion imagen: " + url2 + " " + str(new["status"]))
        pass
    else:
        try:
            l.phoneG = new['result']["international_phone_number"]
        except Exception as e:
            l.phoneG = None

    response = json.loads(requests.get(url1).text)
    if "error" in response:
        print("broken fb api: " + url1 + " " + str(response))
    else:
        try:
            try:
                l.website = response['data'][0]['website']
            except KeyError:
                l.website = "404"
            try:
                l.phoneFB = response['data'][0]['phone']
            except KeyError:
                l.phoneFB = None
        except (KeyError, IndexError) as e:

            l.website = "404"
            l.phoneFB = None
    l.save()
print("suc")











