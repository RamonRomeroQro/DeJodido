from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def Prueba_index(request):
    print('hola')
    return render(request, 'prueba_FB.html')

@login_required
def Prueba_login_si(request):
    return render(request, 'prueba_FB.html')