from carta.models import Carta
from carta.serializers import CartaSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class CartaAPI(APIView):
    serializer_class = CartaSerializer

    def get_object(self, card_id):
        try:
           return Carta.objects.get(id=card_id)
        except Carta.DoesNotExist:
           return None

    def get(self, request, *args, **kwargs):
        lista_cartas = Carta.objects.all()
        serializer = CartaSerializer(lista_cartas, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        carta = request.data
        serializer = CartaSerializer(data=carta)
        if serializer.is_valid(raise_exception=True):
            carta_saved = serializer.save()
        return Response({"Sucesso"})
    
    def patch(self, request, card_id, *args, **kwargs):
        card_test = self.get_object(card_id)
        if not card_test:
            return Response("Objeto não encontrado")
        serializer = CartaSerializer(card_test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Parametros errados"}, status=status.HTTP_400_BAD_REQUEST)

        #updated_card = None
        #try:
        #    updated_card = Carta.objects.get(id=card_id)
        #except Carta.DoesNotExist:
        #    return Response({"res":"Carta não existe"}, status=status.HTTP_400_BAD_REQUEST)
        #return Response({f"{ card_id } - { request.data }"})

