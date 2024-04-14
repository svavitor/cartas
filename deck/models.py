from django.db import models

class Deck(models.Model):
    name = models.TextField(max_length=400)
    card_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
