from usuarios.models import Usuario
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect



def verificacion_FB(function):
    def wrap(request, *args, **kwargs):

        if not hasattr(request.user, 'usuario'):
            print("NO tiene")
            Usuario.objects.create(
                user=request.user,
                fecha_nacimiento='2010-10-10',
                genero=1,
                ciudad_id=1,
                fb_id=request.user.social_auth.get(provider='facebook').extra_data['id']
            )

        else:
            print("Si tiene")
            print(request.user.username)


        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
