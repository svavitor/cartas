from datetime import datetime
from django.db import models

class Card(models.Model):
    front = models.TextField(max_length=500)
    back = models.TextField(max_length=500)
    next_review = models.DateTimeField(default=datetime.now) #Esse campo deverá ser separado futuramente, crie uma relção com cada usuário 

    def __str__(self):
        return f'{self.front} - {self.back}'


