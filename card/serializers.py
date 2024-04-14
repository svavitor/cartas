from rest_framework import serializers
from card.models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'front',
            'back',
            'review_count',
            'review_multiplier',
            'last_review', 
            'next_review',
            'deck'
            ]
