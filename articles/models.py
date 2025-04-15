from django.db import models
from clients.models import Client
from unites.models import ValeurMesure

class Article(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    etat = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)
    longueur = models.ForeignKey(ValeurMesure, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles_longueur')
    largeur = models.ForeignKey(ValeurMesure, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles_largeur')
    poids = models.ForeignKey(ValeurMesure, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles_poids')


    def __str__(self):
        return f"{self.nom} - {self.client.nom_complet}"