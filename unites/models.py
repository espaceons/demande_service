from django.db import models

class UniteMesure(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    symbole = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

class ValeurMesure(models.Model):
    unite = models.ForeignKey(UniteMesure, on_delete=models.CASCADE)
    valeur = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.valeur} {self.unite.symbole}"