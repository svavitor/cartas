from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from datetime import datetime
from carta.models import Carta
from carta.serializers import CartaSerializer

class CartaAPI(APIView):
    serializer_class = CartaSerializer

    def get_object(self, card_id):
        """ Returns single object using card_id """
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

#(TODO) Criar uma função para mostrar apenas os reviews do dia atual ou atrasados.

class CardViewSet(ViewSet):
    def cards_to_review(self, request):
        queryset = Carta.objects.all().filter(next_review__lte = datetime.today())
        print(queryset)
        serializer = CartaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




