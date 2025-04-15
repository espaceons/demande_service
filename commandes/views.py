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
            commande.date_confirmation = timezone.now()
            commande.date_prise_en_charge = commande.date_confirmation # Définir la date de prise en charge à la date de confirmation a la creation
            commande.montant = 0  # Initialiser le montant à 0 ou à une valeur par défaut
            commande.save()
            return redirect('commandes:commande_list')
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

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


def commande_confirme(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    commande.confirme = True
    commande.save()
    return redirect('commandes:commande_list')


@staff_member_required
def commande_annuler_confirmation(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    
    if commande.confirme:
        commande.confirme = False
        commande.date_confirmation = None
        commande.confirme_par = None
        commande.save()
        messages.success(request, f"La confirmation de la commande #{commande.id} a été annulée.")
    else:
        messages.warning(request, f"La commande #{commande.id} n'était pas confirmée.")
    
    return redirect('commandes:commande_list')


def commande_detail_confirmation(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    # Logique pour récupérer et afficher les détails de la confirmation
    return render(request, 'commandes/commande_detail_confirmation.html', {'commande': commande})