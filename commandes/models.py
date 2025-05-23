from django.db import models
from articles.models import Article
from django.utils import timezone
from django.contrib.auth.models import User

class Commande(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_prise_en_charge = models.DateTimeField(default=timezone.now, null=True, blank=True) # Date de prise en charge de la commande
    date_retour_prevue = models.DateTimeField(null=True, blank=True) # Date de retour prévue de la commande
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Prix de l'article
    statut_paiement = models.CharField(max_length=20, null=True, blank=True)
    date_commande = models.DateTimeField(default=timezone.now, null=True, blank=True) # Date de la commande
    montant = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True) # Montant total de la commande
    confirme = models.BooleanField(default=False) # confirmation de la commande
    date_confirmation = models.DateTimeField(null=True, blank=True) # Date de confirmation de la commande
    

    def __str__(self):
        return f"Commande {self.id} - {self.client.username} - {self.article.nom}"