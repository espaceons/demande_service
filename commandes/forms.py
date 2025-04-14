from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['article', 'date_prise_en_charge', 'date_retour_prevue', 'prix', 'statut_paiement']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # La date de commande est automatiquement définie lors de la sauvegarde
        self.fields['date_prise_en_charge'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['date_retour_prevue'].widget = forms.DateInput(attrs={'type': 'date'})