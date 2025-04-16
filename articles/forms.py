from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # Excluez le champ 'client' pour qu'il ne soit pas affiché dans le formulaire
        exclude = ['client']