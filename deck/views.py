from rest_framework import viewsets
from deck.models import Deck
from deck.serializers import DeckSerializer

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
