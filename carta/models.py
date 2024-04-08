from datetime import datetime
from django.db import models

class Carta(models.Model):
    frente = models.TextField(max_length=500)
    verso = models.TextField(max_length=500)
    next_review = models.DateTimeField(default=datetime.now) #Esse campo deverá ser separado futuramente, crie uma relção com cada usuário 

    def __str__(self):
        return f'{self.frente} - {self.verso}'


