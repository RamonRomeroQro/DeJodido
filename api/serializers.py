
from rest_framework import serializers
from lugares.models import Lugar

class lugarSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields="__all__"


    