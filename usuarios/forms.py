from django.forms import ModelForm
from .models import Usuario, Resena
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormaUser(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2')


class FormaUsuario(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormaUsuario, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.input_type = 'date'

    class Meta:
        model = Usuario
        fields = ('fecha_nacimiento','genero','imagen')


class UsuarioReview(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioReview, self).__init__(*args, **kwargs)
        self.fields['calificacion'].widget.attrs['min'] = '0'
        self.fields['calificacion'].widget.attrs['max'] = '5'
        self.fields['precio_cerveza'].widget.attrs['min'] = '0'


    class Meta:
        model = Resena
        fields =('calificacion','precio_cerveza','comentario')


class FormaUsuarioFB(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormaUsuarioFB, self).__init__(*args, **kwargs)
        self.fields['fecha_nacimiento'].widget.input_type = 'date'

    class Meta:
        model = Usuario
        fields = ('fecha_nacimiento','genero')

class FormaUserFB(UserCreationForm):

    class Meta:
        model = User
        fields = ('password1', 'password2')
