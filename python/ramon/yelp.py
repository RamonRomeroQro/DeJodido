
#curl -X GET -H "Authorization: Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx"  "https://api.yelp.com/v3/businesses/search?term=alquimia&latitude=20.5732807&longitude=-100.3614291"





import requests, json, pprint

    #pprint.pprint(response)


def busquedaFacebook(regex, lat, lng):
    # specific="bar los amigos"
    token = '2016535901926533|shNiHD3XAmykHQ0MiFImMpUX4GE'
    urlFB = "https://graph.facebook.com/v3.0/search?type=place&center=" + lat + "," + lng + "&distance=5000&q=" + regex + "&fields=name,link,overall_star_rating,price_range,website&access_token=" + token
    response = json.loads(requests.get(urlFB).text)
    #pprint.pprint(response)
    try:
        if len(response['data']) >0:
            print('facebook_name: ' + response['data'][0]['name'])
            print('facebook_price: ' + response['data'][0]['price_range'])
            print('facebook_ID: ' + response['data'][0]['id'])
            print('facebook_page: ' + response['data'][0]['link'])
            try:
                print('facebook_rating: ' + str(response['data'][0]['overall_star_rating']))
            except KeyError:
                print ('NO HAY INFORMACION DE FACEBOOK')
        else:
            print ('NO HAY INFORMACION DE FACEBOOK')
    except KeyError:
        print ('NO HAY INFORMACION DE FACEBOOK')





lat='20.5924074'
lng='-100.3788854'
kyword='alquimia'

busquedaFacebook(kyword,lat,lng)



#Authorization: Bearer <YOUR API KEY>


