from django import forms
from .models import Client, ClientProfile
from django.contrib.auth.forms import UserCreationForm

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom_complet', 'numero_telephone']
        
        
class ClientCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telephone = forms.CharField(max_length=20, required=False)
    adresse = forms.CharField(widget=forms.Textarea, required=False)
    # Ajoutez ici d'autres champs spécifiques à vos clients

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'telephone', 'adresse')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    
class ClientProfileForm(forms.ModelForm):
    class Meta:
        model = ClientProfile
        fields = ('telephone', 'adresse', 'autres_champs') # Liste des champs de votre profil