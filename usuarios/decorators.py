from usuarios.models import Usuario
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from usuarios.forms import FormaUserFB, FormaUsuarioFB
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def verificacion_FB(function):
    def wrap(request, *args, **kwargs):

        if not hasattr(request.user, 'usuario') and hasattr(request.user, 'social_auth'):
            print("No tiene usuario pero tiene FB")

            if request.method == "POST":
                print("recibi un post")
                formaUser = FormaUserFB(request.POST or None, prefix="user", instance=request.user)
                formaUsuario = FormaUsuarioFB(request.POST, prefix="usuario")

                if formaUser.is_valid() and formaUsuario.is_valid():
                    formaUser.save()
                    usuario = formaUsuario.save(commit=False)
                    usuario.user = request.user
                    usuario.ciudad_id = 1
                    usuario.save()

                    return HttpResponseRedirect(reverse_lazy('landing:landing'))

            FormaUser = FormaUserFB(prefix="user")
            formaUsuario = FormaUsuarioFB(prefix="usuario")
            return render(request, 'usuarios/fb_extras.html', {'forma': FormaUser, 'forma2': formaUsuario})



        else:
            print("Si tiene")
            print(request.user.username)

        return HttpResponseRedirect(reverse_lazy('landing:landing'))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
