from carta.models import Carta
from carta.serializers import CartaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class CartaAPI(APIView):
    serializer_class = CartaSerializer

    def get(self, request):
        lista_cartas = Carta.objects.all()
        serializer = CartaSerializer(lista_cartas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        carta = request.data
        serializer = CartaSerializer(data=carta)
        if serializer.is_valid(raise_exception=True):
            carta_saved = serializer.save()
        return Response({"sucesso"})
