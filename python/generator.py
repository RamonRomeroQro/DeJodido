import requests
import json
import pymongo
'''
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


'''
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

'''

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
'''


'''


