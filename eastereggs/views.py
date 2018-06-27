from django.shortcuts import render

# Create your views here.

def salmon(request):
    return render(request, 'eastereggs/salmon.html')


def amezcua(request):
    return render(request, 'eastereggs/amezcua.html')


def rogelio(request):
    return render(request, 'eastereggs/rogelio.html')

