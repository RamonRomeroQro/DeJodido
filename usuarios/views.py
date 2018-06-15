from django.shortcuts import render
from .forms import FormaUser, FormaUsuario, UsuarioReview
from django.http import HttpResponseRedirect
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from lugares.models import *
from django.shortcuts import redirect


# Create your views here.

def singup(request):

    if request.method == 'POST':
        formaUser = FormaUser(request.POST, prefix="user")
        formaUsuario = FormaUsuario(request.POST, prefix="usuario")
        if formaUser.is_valid() and formaUsuario.is_valid():
            user = formaUser.save()
            usuario = formaUsuario.save(commit=False)
            usuario.user = user

            ciudad = request.POST['city']

            if ", "  in ciudad:
                try:
                    parsedlocation = ciudad.split(', ')
                    city = parsedlocation[0]
                    state = parsedlocation[1]
                    country = parsedlocation[2]
                    qpais = Pais.objects.get(nombre=country)
                    qstate = Estado.objects.filter(pais=qpais).get(nombre=state)
                    qcity = Ciudad.objects.filter(estado=qstate).get(nombre=city)
                    usuario.ciudad_id = qcity.id
                except:
                    usuario.ciudad_id = 1
                    usuario.ciudadUnparsable=ciudad

            else:
                usuario.ciudadUnparsable = ciudad

            usuario.save()
            return render(request, 'landing/index.html')

            #return redirect('/login')
        else:
            return render(request, 'singup.html', {'forma': formaUser, 'forma2': formaUsuario})


            #request.user.message_set.create(message='no creado')
            #return redirect('/login')


    else:
        formaUser = FormaUser(prefix="user")
        formaUsuario = FormaUsuario(prefix="usuario")
        return render(request, 'singup.html', {'forma': formaUser, 'forma2': formaUsuario})

@login_required
def prueba_resena(request,nombre_lugar,id_lugar):

    if request.method == 'POST':
        formaResena = UsuarioReview(request.POST)

        if formaResena.is_valid():
            resena = formaResena.save(commit=False)
            resena.usuario = request.user.usuario
            resena.lugar_id = id_lugar
            resena.save()

    formaResena = UsuarioReview
    lugar = Lugar.objects.get(id=id_lugar)

    return render(request, 'prueba_resena.html', {'forma_resena':formaResena,'lugar':lugar})


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

    return render(request, 'landing/index.html')







