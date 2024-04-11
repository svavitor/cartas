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
        all_cards = Card.objects.all()
        serializer = CardSerializer(all_cards, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        new_card = request.data
        serializer = CardSerializer(data=new_card)
        if serializer.is_valid(raise_exception=True):
            new_card = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, card_id, *args, **kwargs):
        params_to_update = request.data
        card = self.get_object(card_id)
        if not card:
            return Response("Objeto não encontrado")

        serializer = CardSerializer(card, data=params_to_update, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"Parametros errados"}, status=status.HTTP_400_BAD_REQUEST)
    

class CardViewSet(ViewSet):
    
    def set_last_review_to_now(self, card_id):
        card = CardAPI.get_object(CardAPI, card_id)
        updated_card = {}
        updated_card['last_review'] = datetime.now()
        return updated_card

    def cards_to_review_today(self, request):
        time_now = datetime.now(tz=pytz.timezone('America/Fortaleza'))
        cards_for_today = Card.objects.all().filter(next_review__lte = time_now)
        cards_count = cards_for_today.count()
        serializer = CardSerializer(cards_for_today, many=True)
        response = { 'count': cards_count, 'cards': serializer.data } 
        return Response(response, status=status.HTTP_200_OK)
    
    def x(self, request, card_id):
        card = CardAPI.get_object(CardAPI, card_id)
        updated_card = self.set_last_review_to_now(card_id)
        updated_card['review_count'] = card.review_count+1

        delta = timedelta(minutes=2)
        updated_card['next_review'] = updated_card['last_review'] + delta
        #updated_card['review_multiplier'] = card.review_multiplier/2

        #if updated_card['review_multiplier'] < 1:
        #    updated_card['review_multiplier'] = 1        

        serializer = CardSerializer(card, data=updated_card, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(updated_card, status=status.HTTP_200_OK)
    
    def o(self, request, card_id):
        card = CardAPI.get_object(CardAPI, card_id)
        updated_card = self.set_last_review_to_now(card_id)

        updated_card['review_count'] = card.review_count+1

        #if card.review_multiplier < 3:
        #    delta = timedelta(minutes=5*card.review_multiplier)
        #else:
        #    delta = timedelta(days=1*card.review_multiplier)

        delta = timedelta(minutes=5)
        updated_card['next_review'] = card.next_review + delta
        #updated_card['review_multiplier'] = card.review_multiplier + 1

        serializer = CardSerializer(card, data=updated_card, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(updated_card, status=status.HTTP_200_OK)


