from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm


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


# 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def inscription_client(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        client_form = ClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
        client_form = ClientForm()
    return render(request, 'clients/inscription_client.html', {'user_form': user_form, 'client_form': client_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('commandes:commande_list')  # Rediriger vers la page souhaitée après la connexion
    else:
        form = AuthenticationForm()
    return render(request, 'clients/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('clients:login')  # Rediriger vers la page de connexion après la déconnexion