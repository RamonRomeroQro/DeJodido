from django.forms import ModelForm
from .models import Usuario, UsuarioResenaLugar
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
        fields = ('ciudad','fecha_nacimiento','genero','imagen')


class UsuarioReview(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UsuarioReview, self).__init__(*args, **kwargs)
        self.fields['calificaicon'].widget.attrs['min'] = '0'
        self.fields['calificaicon'].widget.attrs['max'] = '5'

    class Meta:
        model = UsuarioResenaLugar
        fields =('calificaicon','precio_cerveza','comentario')