from django.shortcuts import render

# Create your views here.


#Visualizar partidos en la landing page
def landing(request):
    return render(request, 'landing/index.html')
