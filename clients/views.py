from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.contrib.auth.forms import AuthenticationForm






from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from .forms import ClientCreationForm  # Créez ce formulaire dans clients/forms.py
from django.contrib.auth.decorators import login_required




# CRUD Clients : affichage, mise a jour, suppression, creation
#------------------------------------------------------------

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients:client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clients:client_list')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})




# inscription client : creation d'un compte client
#------------------------------------------------------------ 

from .forms import ClientCreationForm, ClientProfileForm


def inscription_client(request):
    if request.method == 'POST':
        user_form = ClientCreationForm(request.POST)
        profile_form = ClientProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            auth_login(request, user)
            return redirect('accueil')
        else:
            return render(request, 'clients/inscription_client.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        user_form = ClientCreationForm()
        profile_form = ClientProfileForm()
    return render(request, 'clients/inscription_client.html', {'user_form': user_form, 'profile_form': profile_form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('accueil')  # Rediriger vers la page d'accueil
            else:
                form.add_error(None, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'clients/login.html', {'form': form})

login_required
def logout(request):
    logout(request)
    return redirect('clients:login')  # Rediriger vers la page de connexion après la déconnexion