from django.shortcuts import render


#Visualizar partidos en la landing page
def landing(request):
    return render(request, 'landing',  )

