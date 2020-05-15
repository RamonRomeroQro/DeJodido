# python3 manage.py shell < ./solve.py
from lugares.models import *
from django.conf import settings
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot

list_places = Lugar.objects.all()
for place in list_places:
    images = place.imagen_set.all()
    for i in images:
        filename = (settings.BASE_DIR + str(i))
        pixels = pyplot.imread(filename)
        # create the detector, using default weights
        detector = MTCNN()
        # detect faces in the image
        faces = detector.detect_faces(pixels)
        if faces:
            i.status=False
            i.save()
    place.status=True
    place.save()



'''



# load image from file
filename = 'test1.jpg'

    
'''
