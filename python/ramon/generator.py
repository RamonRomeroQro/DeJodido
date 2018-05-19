



import requests
import json


#https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCXm58tMXQ48sO1IKP956SRE-hrwswn1GQ

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



#connection = pymongo.MongoClient("mongodb://localhost")
#db=connection.jodido
#db.busquedas.insert(response)

print (url)

count=0
while (count < len(response['results'])):
    print (response['results'][count]['name'])
    count = count + 1



'''

import matplotlib.pyplot as plt


import math
class Coord:
    """A simple example class"""
    x = 0.00
    y = 0.00
    radio = 0.00
    ev=False

    def __init__(self):
        self.x = 0.00
        self.y = 0.00
        self.ev=False
        self.radio = 0.00

    def __init__(self, x, y,r):
        self.x=x
        self.y=y
        self.radio=r
        self.ev=False
    def __str__(self):
        return ('x: '+ str(self.x)+' y: '+ str(self.y) +' r: '+ str(self.radio))




class Hexagon():

    inicial=Coord(0,0,0)
    nextones=[]
    radio=50.00

    def __init__(self, x, y,r):
        self.inicial=Coord(x,y,r)
        #criculo colindante a PI/3 radianes (60 grados)

        equidistancia = (math.sin(math.pi / 3) * self.radio)*2

        calculadaY = self.inicial.y + (equidistancia * math.sin((math.pi / 3)*0))
        calculadaX = self.inicial.x + (equidistancia * math.cos((math.pi / 3)*0))
        ncoord = Coord(calculadaX, calculadaY,r)
        self.nextones.append(ncoord)

        calculadaY = self.inicial.y + (equidistancia * math.sin((math.pi / 3) * 1))
        calculadaX = self.inicial.x + (equidistancia * math.cos((math.pi / 3) * 1))
        ncoord = Coord(calculadaX, calculadaY,r)

        self.nextones.append(ncoord)

        calculadaY = self.inicial.y + (equidistancia * math.sin((math.pi / 3) * 2))
        calculadaX = self.inicial.x + (equidistancia * math.cos((math.pi / 3) * 2))
        ncoord = Coord(calculadaX, calculadaY,r)

        self.nextones.append(ncoord)

        calculadaY = self.inicial.y + (equidistancia * math.sin((math.pi / 3) * 3))
        calculadaX = self.inicial.x + (equidistancia * math.cos((math.pi / 3) * 3))
        ncoord = Coord(calculadaX, calculadaY,r)

        self.nextones.append(ncoord)

        calculadaY = self.inicial.y + (equidistancia * math.sin((math.pi / 3) * 4))
        calculadaX = self.inicial.x + (equidistancia * math.cos((math.pi / 3) * 4))
        ncoord = Coord(calculadaX, calculadaY,r)

        self.nextones.append(ncoord)



        calculadaY = self.inicial.y + (equidistancia * math.sin((math.pi / 3) * 5))
        calculadaX = self.inicial.x + (equidistancia * math.cos((math.pi / 3) * 5))
        ncoord = Coord(calculadaX, calculadaY,r)

        self.nextones.append(ncoord)

    def __str__(self):
        print('Inicial')
        print(self.inicial.__str__())
        for i in self.nextones:
           print('Hex '+i.__str__())


x=0.00
y=0.00
r=50.00
print(x)
print(y)
by=y+r
ny=by+(math.sin(1/6)*r)
print(ny)
nx=x+(math.cos(1/6)*r)
print(nx)

latitude=0.00
longitude=0.00
radio=50.00

h=Hexagon(latitude,longitude,radio)

print(h.__str__())
circleinicial = plt.Circle((h.inicial.x, h.inicial.y), h.inicial.radio, color='r')
circle0 = plt.Circle((h.nextones[0].x, h.nextones[0].y), h.nextones[0].radio, color='blue')
circle1 = plt.Circle((h.nextones[1].x, h.nextones[1].y), h.nextones[1].radio, color='blue')
circle2 = plt.Circle((h.nextones[2].x, h.nextones[2].y), h.nextones[2].radio, color='blue')
circle3 = plt.Circle((h.nextones[3].x, h.nextones[3].y), h.nextones[3].radio, color='blue')
circle4 = plt.Circle((h.nextones[4].x, h.nextones[4].y), h.nextones[4].radio, color='blue')
circle5 = plt.Circle((h.nextones[5].x, h.nextones[5].y), h.nextones[5].radio, color='blue')


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()
ax.set_xlim((-200, 200))
ax.set_ylim((-200, 200))
ax.add_artist(circleinicial)
ax.add_artist(circle0)
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(circle4)
ax.add_artist(circle5)

fig.savefig('plotcircles.png')






6,378,137.0 meters[1] resulting in a circumference of 40,075,161.2 meters.
The equator is divided into 360 degrees of longitude, so each degree at the
equator represents 111,319.9 meters or approximately 111.32 km. 

20.5923513,-100.3788655
20.5928005,-100.3788655
20.59280045602236,-100.3788655




import math
class Coord:
    """A simple example class"""
    y = 0.00
    x = 0.00
    radio = 0.00
    ev=False

    def __init__(self):
        self.x = 0.00
        self.y = 0.00
        self.radio = 0.00

    def __init__(self, y,x,r):
        self.x=x
        self.y=y
        self.radio=r
    def __str__(self):
        return (str(self.y)+','+ str(self.x)+'\n' )


#14*15 km
#evalua y guarda

def ev(c):
    return c

>>> eq
>>> 
>>> 
>>> adegree=eq/360
>>> adegree
111319.89222222223
>>> round(adegree,2)
111319.89
>>> round(adegree,1)
111319.9
>>> 50/adegree
0.00044915602235930617


y=20.5121348
x=-100.5072866
r=50
limitey=20.7477784
limitex=-100.3101173
inicial = Coord(y,x, r)
print('inicial: '+inicial.__str__())
ecuador=40075161.2
adegree=ecuador/360
radiodegrees=inicial.radio/adegree
equidistancia = (math.sin(math.pi / 3) * radiodegrees) * 2
contador=0

thex=inicial.x


while (inicial.y < limitey):


    while (inicial.x < limitex):
        #ev(inicial)
        print(contador)
        inicial.x = inicial.x + equidistancia
        with open('coor.txt', "a") as myfile:
            myfile.write(inicial.__str__())
        contador=contador+1

    inicial.y = inicial.y + (equidistancia * math.sin((math.pi / 3) * 2))
    if (contador%2==0):
        inicial.x=thex
    else:
        inicial.x=thex-equidistancia


'''


