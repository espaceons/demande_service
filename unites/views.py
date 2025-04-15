from django.shortcuts import render, redirect, get_object_or_404
from .models import UniteMesure, ValeurMesure
from .forms import UniteMesureForm, ValeurMesureForm



# Vues pour UniteMesure
def unite_mesure_list(request):
    unites = UniteMesure.objects.all()
    return render(request, 'unites/unite_mesure_list.html', {'unites': unites})

def unite_mesure_create(request):
    if request.method == 'POST':
        form = UniteMesureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unites:unite_mesure_list')
    else:
        form = UniteMesureForm()
    return render(request, 'unites/unite_mesure_form.html', {'form': form})

def unite_mesure_update(request, pk):
    unite = get_object_or_404(UniteMesure, pk=pk)
    if request.method == 'POST':
        form = UniteMesureForm(request.POST, instance=unite)
        if form.is_valid():
            form.save()
            return redirect('unites:unite_mesure_list')
    else:
        form = UniteMesureForm(instance=unite)
    return render(request, 'unites/unite_mesure_form.html', {'form': form})

def unite_mesure_delete(request, pk):
    unite = get_object_or_404(UniteMesure, pk=pk)
    if request.method == 'POST':
        unite.delete()
        return redirect('unites:unite_mesure_list')
    return render(request, 'unites/unite_mesure_confirm_delete.html', {'unite': unite})


# Vues pour ValeurMesure
def valeur_mesure_list(request):
    valeurs = ValeurMesure.objects.all()
    return render(request, 'unites/valeur_mesure_list.html', {'valeurs': valeurs})

def valeur_mesure_create(request):
    if request.method == 'POST':
        form = ValeurMesureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unites:valeur_mesure_list')
    else:
        form = ValeurMesureForm()
    return render(request, 'unites/valeur_mesure_form.html', {'form': form})

def valeur_mesure_update(request, pk):
    valeur = get_object_or_404(ValeurMesure, pk=pk)
    if request.method == 'POST':
        form = ValeurMesureForm(request.POST, instance=valeur)
        if form.is_valid():
            form.save()
            return redirect('unites:valeur_mesure_list')
    else:
        form = ValeurMesureForm(instance=valeur)
    return render(request, 'unites/valeur_mesure_form.html', {'form': form})

def valeur_mesure_delete(request, pk):
    valeur = get_object_or_404(ValeurMesure, pk=pk)
    if request.method == 'POST':
        valeur.delete()
        return redirect('unites:valeur_mesure_list')
    return render(request, 'unites/valeur_mesure_confirm_delete.html', {'valeur': valeur})