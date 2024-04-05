from rest_framework import serializers
from carta.models import Carta

class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = ['frente','verso']
