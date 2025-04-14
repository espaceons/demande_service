from django.urls import path
from . import views


app_name = 'commandes'


urlpatterns = [
    path('', views.commande_list, name='commande_list'),
    path('create/', views.commande_create, name='commande_create'),
    path('<int:pk>/update/', views.commande_update, name='commande_update'),
    path('<int:pk>/delete/', views.commande_delete, name='commande_delete'),
    path('<int:pk>/confirme/', views.commande_confirme, name='commande_confirme'),
]