import json, requests

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

        print('nombre Foursquare: ' +data['response']['venues'][0]['name'])
        print('foursquare_id: ' +data['response']['venues'][0]['id'])

        urlrating='https://api.foursquare.com/v2/venues/'+data['response']['venues'][0]['id']
        resp2 = requests.get(url=urlrating, params=params2)
        data2 = json.loads(resp2.text)
        try:
            print('foursquare_rating: ' + str(data2['response']['venue']['rating']))
        except KeyError:
            print('foursquare_rating: NO DISP')

    else:
        print('No Hay')


busquedaFoursquare('diablo',20.5962703,-100.4028663)

