from django.urls import path
from . import views


app_name = 'clients'

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('create/', views.client_create, name='client_create'),
    path('<int:pk>/update/', views.client_update, name='client_update'),
    path('<int:pk>/delete/', views.client_delete, name='client_delete'),
    path('inscription/', views.inscription_client, name='inscription_client'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]