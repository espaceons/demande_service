from django.urls import path
from . import views

app_name = 'unites'

urlpatterns = [
    # URLs pour UniteMesure
    path('', views.unite_mesure_list, name='unite_mesure_list'),
    path('create/', views.unite_mesure_create, name='unite_mesure_create'),
    path('update/<int:pk>/', views.unite_mesure_update, name='unite_mesure_update'),
    path('delete/<int:pk>/', views.unite_mesure_delete, name='unite_mesure_delete'),

    # URLs pour ValeurMesure
    path('valeurs/', views.valeur_mesure_list, name='valeur_mesure_list'),
    path('valeurs/create/', views.valeur_mesure_create, name='valeur_mesure_create'),
    path('valeurs/update/<int:pk>/', views.valeur_mesure_update, name='valeur_mesure_update'),
    path('valeurs/delete/<int:pk>/', views.valeur_mesure_delete, name='valeur_mesure_delete'),
]