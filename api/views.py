from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from lugares.models import Lugar
from .serializers import lugarSerializer

class search(APIView):

    def get(self, request):
        p=Lugar.objects.all()
        serial= lugarSerializer(p, many=True)
        return Response(serial.data)
