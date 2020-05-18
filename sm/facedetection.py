# python3 manage.py shell < ./solve.py
from lugares.models import *
from django.conf import settings
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot
from django.core.files.uploadedfile import SimpleUploadedFile


def eval_faces():
    list_places = Lugar.objects.all()
    for place in list_places:
        images = place.imagen_set.all()
        for i in images:
            filename = (settings.BASE_DIR + str(i))
            try:
                pixels = pyplot.imread(filename)
                detector = MTCNN()
                faces = detector.detect_faces(pixels)
                pyplot.close()
            except:
                i.imagen = SimpleUploadedFile(name=place.id_google + '-' + 'default' + '.jpg',
                                              content=open(settings.BASE_DIR + '/static/images/default.jpg', 'rb').read(),
                                              content_type='image/jpeg')
                i.descripcion = None
                i.status = True
                continue

            if faces:
                i.status = False
                i.save()
            else:
                i.status = True
                i.save()
        place.status = True
        place.save()
