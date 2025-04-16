from django.db import models
from clients.models import Client
from unites.models import ValeurMesure
from django.contrib.auth.models import User

class Article(models.Model):
    ETAT_CHOICES = [
        ('nouveau', 'Nouveau'),
        ('ancien', 'Ancien'),
    ]
    
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    etat = models.CharField(max_length=50, choices=ETAT_CHOICES)
    notes = models.TextField(blank=True, null=True)
    longueur = models.IntegerField( null=True, blank=True)
    largeur = models.DecimalField(max_digits=30, decimal_places=15, null=True, blank=True)
    poids = models.IntegerField( null=True, blank=True)


    def __str__(self):
        return f"{self.nom}"