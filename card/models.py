from datetime import datetime
from django.db import models
from deck.models import Deck

class Card(models.Model):
    front = models.TextField(max_length=500)
    back = models.TextField(max_length=500)
    review_count = models.IntegerField(default=1)
    review_multiplier = models.FloatField(default=1)
    last_review = models.DateTimeField(default=datetime.now)
    next_review = models.DateTimeField(default=datetime.now) #Esse campo deverá ser separado futuramente, crie uma relção com cada usuário 
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.front} - {self.back}'

