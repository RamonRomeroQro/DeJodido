from django.shortcuts import render
from .forms import FormaUser, FormaUsuario, UsuarioReview, FormaUserFB, FormaUsuarioFB
from django.http import HttpResponseRedirect
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from lugares.models import *
from django.shortcuts import redirect
from usuarios.models import *
from usuarios.decorators import verificacion_FB


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
                usuario.ciudad_id = 1
                usuario.ciudadUnparsable = ciudad

            usuario.save()
            return redirect('/login')

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
@verificacion_FB
def resena(request,nombre_lugar,id_lugar):

    if request.method == 'POST' :
        resena = Resena.objects.create(
                usuario=request.user.usuario,
                lugar = Lugar.objects.get(id=id_lugar),
                calificacion = request.POST['resena-calificacion'],
                precio_cerveza = request.POST['resena-precio_cerveza'],
                comentario = request.POST['resena-comentario']
        )
        resena.save()

    return redirect('lugares:detalle_lugar', nombre_lugar=nombre_lugar, id_lugar=id_lugar )

@login_required
@verificacion_FB
def prueba_fb(request):
    return render(request, 'usuarios/prueb_fb.html')




def fb_extras(request):
    FormaUser = FormaUserFB(prefix="user")
    formaUsuario = FormaUsuarioFB(prefix="usuario")
    return render(request, 'usuarios/fb_extras.html', {'forma': FormaUser, 'forma2': formaUsuario})












