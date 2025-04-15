from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        exclude = ['date_confirmation', 'date_retour_prevue', 'prix', 'statut_paiement', 'date_confirmation', 'montant', 'confirme']