
import traceback
import os
import json
import requests
import time
import shutil
from lugares.models import Lugar, Ciudad, Estado, Pais, Imagen
from sm.models import Comando
from lugares.models import Tags
from django.core.files.uploadedfile import SimpleUploadedFile
from difflib import SequenceMatcher
from django.conf import settings


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


omits = ['el', 'la', 'los', 'las', 'bar', 'un', 'un', 'restaurante', ]


def city(c, e, p):
    pais, cr1 = Pais.objects.get_or_create(
        nombre=p
    )

    estado, cr2 = Estado.objects.get_or_create(
        nombre=e,
        pais=pais
    )

    ciudad, cr3 = Ciudad.objects.get_or_create(
        nombre=c,
        estado=estado
    )

    return ciudad


def getImagePath(log, g_id):
    detalle_url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + \
                  g_id + '&key=' + settings.GMAPS_API_KEY
    time.sleep(2)
    new = json.loads(requests.get(detalle_url).text)
    if new["status"]!="OK":
        raise Exception("Fallo recuperacion imagen: "+detalle_url+ " "+ str(new["status"]))
    log.write("\nRetrived info place: "+ detalle_url)
    links = []
    # pprint.pprint(new)
    try:
        phoneG=new['result']["international_phone_number"]
    except Exception as e:
        log.write("No phone: "+str(e))
        phoneG = None

    try:
        ######################
        cantidad = len(new['result']['photos'])
        contador = 0
        while contador < cantidad:
            im_id = new['result']['photos'][contador]['photo_reference']
            image_url = 'https://maps.googleapis.com/maps/api/place/photo?maxheight=1600&photoreference=' + \
                        im_id + '&key=' + settings.GMAPS_API_KEY
            time.sleep(2)
            response = requests.get(image_url, stream=True)
            dir_file = settings.BASE_DIR + '/media/Lugar/' + im_id + '.jpg'
            with open(dir_file, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            log.write("\nDownloaded image "+ dir_file)

            links.append(dir_file)
            contador = contador + 1
        return links, phoneG
    except KeyError:
        dir_file = settings.BASE_DIR + '/media/Lugar/default.jpg'
        links.append(dir_file)
        return links, phoneG


def taging(kw):
    tag, cr1 = Tags.objects.get_or_create(
        descripcion=kw
    )

    return tag


def creacioDBO(log, gobj, fobj, sobj, yobj, kw, c, e, p):
    rt = [gobj['google_rating'], yobj['yelp_rating'],
          sobj['foursquare_rating'], fobj['facebook_rating']]
    # pprint.pprint(rt)
    crt = rt.count(-100)
    sm = sum(rt) + (crt * 100)
    d = len(rt) - crt
    try:
        avrt = sm / d
        rat = avrt
    except ZeroDivisionError:
        rat = -100

    rt = [gobj['google_price'], yobj['yelp_price'],
          sobj['foursquare_price'], fobj['facebook_price']]
    # pprint.pprint(rt)
    crt = rt.count(-100)
    sm = sum(rt) + (crt * 100)
    d = len(rt) - crt
    try:
        avrt = sm / d
        price = avrt
    except ZeroDivisionError:
        price = -100

    c = city(c, e, p)
    t = taging(kw)

    try:
        obj = Lugar.objects.get(id_google=gobj['google_id'])

    except Lugar.DoesNotExist:
        obj = Lugar.objects.create(
            nombre=gobj['google_nombre'],
            direccion=gobj['google_direccion'],
            latitud=gobj['google_latitud'],
            longitud=gobj['google_longitud'],
            botana=None,
            validado=False,
            id_google=gobj['google_id'],
            id_yelp=yobj['yelp_id'],
            id_foursquare=sobj['foursquare_id'],
            id_facebook=fobj['facebook_id'],
            facebook_link=fobj['facebook_link'],
            ciudad=c,
            rating=rat,
            precio=price,
            phoneFB=fobj["facebook_phone"],
            website=fobj["facebook_website"],
        )
    if obj.imagen_set.all().count()==0:

        imagenes, phone_google = getImagePath(log ,gobj['google_id'])
        obj.phoneG=phone_google
        log.write("\n Attached phone")
        # print (imagenes)
        cont = 0
        while cont < len(imagenes):
            im = Imagen.objects.get_or_create(lugar=obj,
                                              imagen=SimpleUploadedFile(name=obj.id_google + '-' + str(cont) + '.jpg',
                                                                        content=open(imagenes[cont],
                                                                                     'rb').read(),
                                                                        content_type='image/jpeg'),
                                              descripcion='Importada desde Google Imagenes')
            log.write("\nSaved image "+ imagenes[cont])
            # Descargar y luego asignar y borrar
            if 'default' not in imagenes[cont]:
                os.remove(imagenes[cont])
            cont = cont + 1

    obj.save()
    log.write("\nSaved Object " + str(obj.nombre))

    obj.tags.add(t)
    log.write("\ntag added " + kw)


def busquedaYelp(regex, lat, lng):
    url = "https://api.yelp.com/v3/businesses/search?term=" + \
          regex + "&latitude=" + lat + "&longitude=" + lng
    headers = {'Authorization': settings.YELP_AUTH}
    response = json.loads(requests.get(url, headers=headers).text)
    # pprint.pprint(response)
    if "error" in response:
        raise Exception("Break Yelp "+ url +" "+ str(response))
    try:

        # print ("yelp_name: " + response['businesses'][0]['name'])
        yelp_id = (response['businesses'][0]['id'])
        try:
            yelp_rating = response['businesses'][0]['rating']
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


def busquedaFoursquare(regex, lat, lng):
    url = 'https://api.foursquare.com/v2/venues/search'

    a=settings.FSQID
    b=settings.FSQS
    c=settings.FSQV


    params2 = dict(
        client_id= a ,
        client_secret= b ,
        v= c ,
    )

    params = dict(
        client_id= a ,
        client_secret= b ,
        v= c ,
        ll=str(lat) + ',' + str(lng),
        name=regex,
        intent='match',
        limit=4
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    if data["meta"]["code"] != 200:
        raise Exception("Error FSQ APi "+ str(data["meta"]["code"])+" "+url)

    try:

        # print('foursquare_name: ' +data['response']['venues'][0]['name'])
        foursquare_id = data['response']['venues'][0]['id']

        urlrating = 'https://api.foursquare.com/v2/venues/' + \
                    data['response']['venues'][0]['id']
        resp2 = requests.get(url=urlrating, params=params2)
        data2 = json.loads(resp2.text)
        if data2["meta"]["code"] != 200:
            raise Exception("Error FSQ APi: "+ str(data2["meta"]["code"])+ " "+urlrating)

        try:
            foursquare_price = (data2['response']['venue']['price']['tier'])
        except KeyError:
            foursquare_price = -100

        try:
            foursquare_rating = (data2['response']['venue']['rating']) / 2
        except KeyError:
            foursquare_rating = -100

    except (KeyError, IndexError) as e:
        foursquare_id = -100
        foursquare_price = -100
        foursquare_rating = -100

        # print('NO HAY INFORMACION DE FOURSQUARE')

    return {'foursquare_id': foursquare_id, 'foursquare_price': foursquare_price,
            'foursquare_rating': foursquare_rating}


def busquedaFacebook(regex, lat, lng):
    # specific="bar los amigos"
    token = settings.FBTOKEN
    urlFB = "https://graph.facebook.com/v3.0/search?type=place&center=" + lat + "," + lng + "&distance=5000&q=" + \
            regex + "&fields=name,link,overall_star_rating,price_range,website,phone&access_token=" + token
    response = json.loads(requests.get(urlFB).text)
    if "error" in response:
        raise Exception("broken fb api: "+urlFB +" " +str(response))
    try:
        # print('facebook_name: ' + response['data'][0]['name'])
        facebook_id = response['data'][0]['id']
        # print('facebook_page: ' + response['data'][0]['link'])
        try:
            facebook_rating = response['data'][0]['overall_star_rating']
        except KeyError:
            facebook_rating = -100
        try:
            facebook_price = len(response['data'][0]['price_range'])
        except KeyError:
            facebook_price = -100
        try:
            facebook_link = response['data'][0]['link']
        except KeyError:
            facebook_link = "404"

        try:
            facebook_website = response['data'][0]['website']
        except KeyError:
            facebook_website = "404"
        try:
            facebook_phone = response['data'][0]['phone']
        except KeyError:
            facebook_phone = None

    except (KeyError, IndexError) as e:
        facebook_id = -100
        facebook_rating = -100
        facebook_price = -100
        facebook_link = "404"
        facebook_website = "404"
        facebook_phone = None

    return {'facebook_id': facebook_id, 'facebook_rating': facebook_rating, 'facebook_price': facebook_price,
            'facebook_link': facebook_link, 'facebook_website':facebook_website, "facebook_phone": facebook_phone}


def busquedaGMaps(log, latitude, longitude, kyword, c, e, p):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + latitude + \
          ',' + longitude + '&radius=5000' + '&keyword=' + \
          kyword + '&key=' + settings.GMAPS_API_KEY
    # print (url)

    response = json.loads(requests.get(url).text)
    # print(response['status'])
    if response['status'] != "OK":
        raise Exception("Fallo Google PLACES-API: check: GMAPS_API_KEY "+url + " "+response['status'])
    else:

        log.write("\n+"+url+"\nGoogle: "+response['status'])
    return {'response': response, 'kyword': kyword, 'c': c, 'e': e, 'p': p}


def saveLocal(log, arr, kyword, c, e, p):
    count = 0
    while count < len(arr['results']):
        try:
            obj = Lugar.objects.get(
                id_google=arr['results'][count]['place_id'])
            t, created = Tags.objects.get_or_create(
                descripcion=kyword
            )
            if obj.tags.filter(descripcion=kyword).exists() == False:
                obj.tags.add(t)
                log.write("\n"+'tag agregada: '+kyword)

            log.write('\n>>>' + str(obj.nombre + ': recuperado'))

        except Lugar.DoesNotExist:

            google_nombre = arr['results'][count]['name']

            google_id = arr['results'][count]['place_id']
            try:
                google_rating = arr['results'][count]['rating']
            except KeyError:
                google_rating = -100

            google_direccion = arr['results'][count]['vicinity']
            google_latitud = arr['results'][count]['geometry']['location']['lat']
            google_longitud = arr['results'][count]['geometry']['location']['lng']

            try:
                google_price = arr['results'][count]['price_level']
            except KeyError:
                google_price = -100


            gobj = {'google_nombre': google_nombre, 'google_id': google_id, 'google_rating': google_rating,
                    'google_direccion': google_direccion,
                    'google_latitud': google_latitud, 'google_longitud': google_longitud, 'google_price': google_price}
            log.write('\n>>>>>>>>>>>>' + gobj['google_nombre'] + "Update Google")

            fobj = busquedaFacebook(str(arr['results'][count]['name']), str(
                arr['results'][count]['geometry']['location']['lat']),
                                    str(arr['results'][count]['geometry']['location']['lng']))
            log.write('\n>>>>>>>>>>>>' + gobj['google_nombre'] + "Update FB")

            yobj = busquedaYelp(str(arr['results'][count]['name']), str(
                arr['results'][count]['geometry']['location']['lat']),
                                str(arr['results'][count]['geometry']['location']['lng']))
            log.write('\n>>>>>>>>>>>>' + gobj['google_nombre'] + "Update Yelp")

            sobj = busquedaFoursquare(str(arr['results'][count]['name']), str(
                arr['results'][count]['geometry']['location']['lat']),
                                      str(arr['results'][count]['geometry']['location']['lng']))
            log.write('\n>>>>>>>>>>>>' + gobj['google_nombre'] + "Update fsq")

            ###
            ###
            creacioDBO(log, gobj, fobj, sobj, yobj, kyword, c, e, p)
            # pprint.pprint(gobj)
            # pprint.pprint(fobj)
            # pprint.pprint(yobj)
            # pprint.pprint(sobj)

        count = count + 1

    if 'next_page_token' in arr:
        time.sleep(2)

        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken=' + \
              str(arr["next_page_token"]) + '&key=' + settings.GMAPS_API_KEY
        # print (url)
        new = json.loads(requests.get(url).text)
        if new['status']!="OK":
            raise Exception("Fail next page: "+url+": "+new['status'])

        log.write("\n\nOK next page: "+url+": "+new['status'])

        # print (new['status'])
        # pprint.pprint(new)
        saveLocal(log, new, kyword, c, e, p)
        # print ('eof')
    # sort by age


def exec_command(request):

    options=request.POST
    log_base=str(settings.BASE_DIR) + '/Logs/'
    if not os.path.isdir(log_base):
        os.makedirs(log_base)
    timestamp = (time.strftime("%d-%m-%Y-%H:%M"))
    log_file_p=log_base+timestamp+".log"
    log_file = open(log_file_p, 'w+')
    base = str(settings.BASE_DIR) + '/media/Lugar/'
    if not (os.path.isfile(settings.BASE_DIR + '/media/Lugar/default.jpg')):
        log_file.write("\n Created: /media/Lugar/default.jpg ")
        os.makedirs(base)
        f = open(base + 'default.jpg', 'w+')
        f.write('default')
        f.close()

    c = Comando.objects.create(
        lat=options['lat'], lng=options['lng'], keyword=options['keyword'],
        city=options['city'], state=options['state'], country=options['country'])
    try:
        response = busquedaGMaps(log_file, str(options['lat']), str(options['lng']), str(
            options['keyword']), str(options['city']), str(options['state']), str(options['country']))


        saveLocal(log_file, response['response'], response['kyword'],
                  response['c'], response['e'], response['p'])
        c.status_exec=True
        print(">.",c.status_exec)



    except Exception as e:
        log_file.write("\n\n"+str(e)+traceback.format_exc())
        c.status_exec = True
        print(">.", c.status_exec)
    log_file.write("\n\n"+str(c))
    log_file.close()
    c.log_file=SimpleUploadedFile(name=str(c)+'.log', content=open(log_file_p, 'rb').read(), content_type="text/plain")
    c.save()
    os.remove(log_file_p)



