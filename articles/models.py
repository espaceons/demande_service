from django.db import models
from clients.models import Client

class Article(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    etat = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.client.nom_complet}"