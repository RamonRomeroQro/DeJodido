from django.shortcuts import render

# Create your views here.
from lugares.models import Lugar



#Visualizar partidos en la landing page
def landing(request):
    return render(request, 'landing/index.html',  )
