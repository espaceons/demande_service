from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_complet = models.CharField(max_length=255)
    adresse = models.TextField()
    numero_telephone = models.CharField(max_length=20)
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username