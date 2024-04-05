from django.db import models

class Carta(models.Model):
    frente = models.TextField(max_length=500)
    verso = models.TextField(max_length=500)
