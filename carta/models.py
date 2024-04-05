from django.db import models

class Carta(models.Model):
    frente = models.TextField(max_length=500)
    verso = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.frente} - {self.verso}'
