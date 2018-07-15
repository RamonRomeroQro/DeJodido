from django.shortcuts import render
from lugares.models import *
from django.shortcuts import get_object_or_404
from  django.conf import  settings
import json
import requests
import datetime
from django.http import HttpResponse
from usuarios.forms import UsuarioReview
from django.http import HttpResponseRedirect




def yelpReviews(request,id_yelp):
    url = 'https://api.yelp.com/v3/businesses/'+id_yelp+'/reviews'
    headers = {
        'Authorization': 'Bearer CpMKG2Z-E_WAiDNoHTnGCUzZ2wUCTPsOwd2B6egscNf6p7BNOY81zt6JjtScUNRaQqq6ttHEqEYLW5PySrEVMe9KFpyeNY9q0Ao7U3ujCGbObr2IDRXTFUD-D1gEW3Yx'}
    response = json.loads(requests.get(url, headers=headers).text)
    try:
        html='<h2>Yelp</h2><ul class="collection">'
        for i in range(0,len(response['reviews'])):
            rating=response['reviews'][i]['rating']
            text=response['reviews'][i]['text']
            time=response['reviews'][i]['time_created']
            url=response['reviews'][i]['url']
            usuario=response['reviews'][i]['user']['name']
            profile=response['reviews'][i]['user']['image_url']
            if profile==None:
                profile=''

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

        return HttpResponse(html)
    except KeyError:
        return HttpResponse('error')



def foursquareReviews(request,id_foursquare):
    url = 'https://api.foursquare.com/v2/venues/'+id_foursquare+'/tips'
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
            try:
                photoplace=        data['response']['tips']['items'][i]['photourl']
            except KeyError:
                photoplace=''

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
        return HttpResponse(html)
    else:
        return HttpResponse('error')






def googleReviews(request, id_google):
    detalle_url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + id_google + '&key=' + settings.GMAPS_API_KEY
    new = json.loads(requests.get(detalle_url).text)
    if (new['status'] == 'OK'):
        i = 0
        html = '<h2>Google</h2><ul class="collection">'

        while i < len(new['result']['reviews']):
            autor = new['result']['reviews'][i]['author_name']
            url = new['result']['reviews'][i]['author_url']
            photo = new['result']['reviews'][i]['profile_photo_url']
            rate = new['result']['reviews'][i]['rating']
            relativetime = new['result']['reviews'][i]['relative_time_description']
            text = new['result']['reviews'][i]['text']
            time = new['result']['reviews'][i]['time']

            html = html + '<a href="' + url + '">'
            html = html + '<li class="collection-item avatar">'
            html = html + '<img src="' + photo + '" alt="" class="circle">'
            html = html + '<span class="title">' + autor + '</span>'
            html = html + '<p>' + text + '</p>'
            html = html + '<p>'
            for i in range(0, rate):
                html = html + '&#x2b50;'
            html = html + '</p>'
            html = html + '<p>' + str(rate) + '</p>'
            html = html + '<p>' + datetime.datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S') + '</p>'
            html = html + '<p>' + relativetime + '</p>'
            html = html + '<a href="#!" class="secondary-content"><i class="material-icons">grade</i></a>'
            html = html + '</li>'
            html = html + '</a>'

            i = i + 1

        html = html + '</ul>'

        return HttpResponse(html)
    else:
        return HttpResponse('error')
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#Visualizar partidos en la landing page
def detalle_lugar(request, nombre_lugar,id_lugar):
    l = get_object_or_404(Lugar, id=id_lugar)
    gkey=settings.GMAPS_API_KEY_JS
    formresena=UsuarioReview(prefix="resena")
    return render(request, 'lugares/details.html' , { 'lugar': l, 'gkey':gkey, 'forma':formresena })



def busqueda(request):

    try:

        fullname = request.GET['city']
        parsedlocation = fullname.split(', ')
        city = parsedlocation[0]
        state = parsedlocation[1]
        country = parsedlocation[2]
        qpais = Pais.objects.get(nombre=country)
        qstate = Estado.objects.filter(pais=qpais).get(nombre=state)
        qcity = Ciudad.objects.filter(estado=qstate).get(nombre=city)
        lugares = Lugar.objects.filter(ciudad=qcity)
        placerandom=lugares.order_by('?').first()
        lugar =[]

        presupuesto = request.GET.getlist('presupuesto')

        for lug in lugares.filter(precio__range=(min(presupuesto), max(presupuesto))).order_by('-rating'):
            lugar.append(lug)

        page = request.GET.get('page', 1)



        noPrecio=lugares.filter(precio='-100').order_by('-rating')

        for l in noPrecio:
            lugar.append(l)

        paginator = Paginator(lugar, 3)
        # agregando desconocidos




        try:
            numbers = paginator.page(page)
        except PageNotAnInteger:
            numbers = paginator.page(1)
        except EmptyPage:
            numbers = paginator.page(paginator.num_pages)


        return render(request, 'lugares/list.html', {'lugares': lugar, 'id_ciudad': qcity.id, 'min_lugar': min(presupuesto),
                                                     'max_lugar:': max(presupuesto), 'numbers': numbers, 'placerandom':placerandom})

    except:

        with open('failed_search.log', 'a') as f:
            f.write(request.GET['city']+'\n')
        f.closed



        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


