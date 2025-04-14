from django.utils import timezone
from django.shortcuts import render
from articles.models import Article
from clients.models import Client
from commandes.models import Commande
from django.db.models import Count, Sum

def dashboard(request):
    # Statistiques des articles
    total_articles = Article.objects.count()
   

    # Statistiques clients
    total_clients = Client.objects.count()
    new_clients = Client.objects.filter(date_creation__month=timezone.now().month).count()

    # Statistiques commandes
    total_commandes = Commande.objects.count()
    commandes_month = Commande.objects.filter(
        date_commande__month=timezone.now().month
    ).aggregate(
        total=Sum('montant'),
        count=Count('id')
    )

    context = {
        'applications': [
            {
                'name': 'articles',
                'url': 'articles:article_list',
                'icon': 'box',
                'stats': {
                    'Total': total_articles,
                  
                }
            },
            {
                'name': 'clients',
                'url': 'clients:client_list',
                'icon': 'users',
                'stats': {
                    'Total': total_clients,
                    'Nouveaux (mois)': new_clients
                }
            },
            {
                'name': 'commandes',
                'url': 'commandes:commande_list',
                'icon': 'shopping-cart',
                'stats': {
                    'Total': total_commandes,
                    'CA (mois)': f"{commandes_month['total'] or 0} €"
                }
            }
        ],
        'commandes_recentes': Commande.objects.all().order_by('-date_commande')[:5]
    }
    return render(request, 'dashboard/dashboard.html', context)