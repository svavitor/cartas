import pytz
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from datetime import datetime, timedelta
from card.models import Card
from card.serializers import CardSerializer

class CardAPI(APIView):
    serializer_class = CardSerializer

    def get_object(self, card_id):
        """ Returns single object using card_id """
        try:
            return Card.objects.get(id=card_id)
        except Card.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        cards_list = Card.objects.all()
        serializer = CardSerializer(cards_list, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        card = request.data
        serializer = CardSerializer(data=card)
        if serializer.is_valid(raise_exception=True):
            card_saved = serializer.save()
        return Response({"Sucesso"})

    def patch(self, request, card_id, *args, **kwargs):
        card_test = self.get_object(card_id)
        if not card_test:
            return Response("Objeto não encontrado")
        serializer = CardSerializer(card_test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Parametros errados"}, status=status.HTTP_400_BAD_REQUEST)

class CardViewSet(ViewSet):
    
    def set_last_review_to_now(self, card_id):
        card = CardAPI.get_object(CardAPI, card_id)
        new_card = {}
        new_card['last_review'] = datetime.now()
        return new_card

    def cards_to_review(self, request):
        time_now = datetime.now(tz=pytz.timezone('America/Fortaleza'))
        queryset = Card.objects.all().filter(next_review__lte = time_now)
        cards_count = queryset.count()
        serializer = CardSerializer(queryset, many=True)
        response = { 'count': cards_count, 'cards': serializer.data } 
        return Response(response, status=status.HTTP_200_OK)
    
    def x(self, request, card_id):
        card = CardAPI.get_object(CardAPI, card_id)
        new_card = self.set_last_review_to_now(card_id)

        new_card['review_count'] = card.review_count+1
        new_card['next_review'] = new_card['last_review']
        new_card['review_multiplier'] = card.review_multiplier/2

        if new_card['review_multiplier'] < 1:
            new_card['review_multiplier'] = 1        

        serializer = CardSerializer(card, data=new_card, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(new_card, status=status.HTTP_200_OK)
    
    def o(self, request, card_id):
        card = CardAPI.get_object(CardAPI, card_id)
        new_card = self.set_last_review_to_now(card_id)

        new_card['review_count'] = card.review_count+1

        if card.review_multiplier < 3:
            new_delta = timedelta(minutes=5*card.review_multiplier)
        else:
            new_delta = timedelta(days=1*card.review_multiplier)

        new_card['next_review'] = card.next_review + new_delta
        new_card['review_multiplier'] = card.review_multiplier + 1

        serializer = CardSerializer(card, data=new_card, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(new_card, status=status.HTTP_200_OK)


