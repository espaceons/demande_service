from django.db import models
from clients.models import Client
from articles.models import Article
from django.utils import timezone

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_prise_en_charge = models.DateField()
    date_retour_prevue = models.DateField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    statut_paiement = models.CharField(max_length=20)
    date_commande = models.DateTimeField(default=timezone.now) # Date de la commande
    montant = models.DecimalField(max_digits=10, decimal_places=3, default=0) # Montant total de la commande
    confirme = models.BooleanField(default=False) # confirmation de la commande
    date_confirmation = models.DateTimeField(null=True, blank=True) # Date de confirmation de la commande

    def __str__(self):
        return f"Commande {self.id} - {self.client.nom_complet} - {self.article.nom}"