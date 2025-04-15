from django.urls import path
from . import views


app_name = 'commandes'


urlpatterns = [
    path('', views.commande_list, name='commande_list'),
    path('create/', views.commande_create, name='commande_create'),
    path('<int:pk>/update/', views.commande_update, name='commande_update'),
    path('<int:pk>/delete/', views.commande_delete, name='commande_delete'),
    path('<int:pk>/confirme/', views.commande_confirme, name='commande_confirme'),
    path('<int:pk>/annuler-confirmation/', views.commande_annuler_confirmation, name='commande_annuler_confirmation'),
    path('detail_confirmation/<int:commande_id>/', views.commande_detail_confirmation, name='commande_detail_confirmation'),
]