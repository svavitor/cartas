from carta.models import Carta
from carta.serializers import CartaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class CartaAPI(APIView):
    def get(self, request):
        lista_cartas = Carta.objects.all()
        serializer = CartaSerializer(lista_cartas, many=True)
        return Response(serializer.data)

def cartas_lista(request):
    return HttpResponse(status=201)

