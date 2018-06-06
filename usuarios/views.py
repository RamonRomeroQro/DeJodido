from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FormaUser, FormaUsuario
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def Prueba_index(request):

    if request.method == 'POST':
        formaUser = FormaUser(request.POST, prefix="user")
        formaUsuario = FormaUsuario(request.POST, prefix="usuario")

        if formaUser.is_valid() and formaUsuario.is_valid():
            user = formaUser.save()
            usuario = formaUsuario.save(commit=False)
            usuario.user = user
            usuario.save()
    else:
        formaUser = FormaUser(prefix="user")
        formaUsuario = FormaUsuario(prefix="usuario")

    return render(request, 'prueba_login.html', {'forma': formaUser, 'forma2': formaUsuario})

@login_required
def prueba_resena(request):
    print(request.user)
    return render(request, 'prueba_resena.html')


@login_required
def verificacion_FB(request):
    try:
        print(request.user.usuario)

    except Usuario.DoesNotExist:
        print("si se pudo")
        Usuario.objects.create(
            user=request.user,
            fecha_nacimiento='2010-10-10',
            genero=1,
            ciudad_id=1,
            fb_id=request.user.social_auth.get(provider='facebook').extra_data['id']
        )

    return HttpResponseRedirect(reverse('usuarios:Prueba_resena'))






