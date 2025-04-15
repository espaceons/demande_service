from django import forms
from .models import UniteMesure, ValeurMesure

class UniteMesureForm(forms.ModelForm):
    class Meta:
        model = UniteMesure
        fields = '__all__'

class ValeurMesureForm(forms.ModelForm):
    class Meta:
        model = ValeurMesure
        fields = '__all__'