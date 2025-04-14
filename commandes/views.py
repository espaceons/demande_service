from django.shortcuts import render, redirect, get_object_or_404
from .models import Commande
from .forms import CommandeForm
from django.utils import timezone



# CRUD Commandes : affichage, mise a jour, suppression, creation
#------------------------------------------------------------


def commande_list(request):
    if request.user.is_superuser:
        commandes = Commande.objects.all()
    else:
        commandes = Commande.objects.filter(client__user=request.user)
    return render(request, 'commandes/commande_list.html', {'commandes': commandes})

def commande_create(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            commande.client = request.user.client  # Associer la commande au client connecté
            commande.date_commande = timezone.now()  # Définir la date de commande actuelle
            commande.save()
            return redirect('commande_list')
    else:
        form = CommandeForm()
    return render(request, 'commandes/commande_form.html', {'form': form})

def commande_update(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('commandes:commande_list')
    else:
        form = CommandeForm(instance=commande)
    return render(request, 'commandes/commande_form.html', {'form': form})

def commande_delete(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('commandes:commande_list')
    return render(request, 'commandes/commande_confirm_delete.html', {'commande': commande})



#

def commande_confirme(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    commande.confirme = True
    commande.save()
    return redirect('commandes:commande_list')