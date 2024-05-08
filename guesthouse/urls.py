from django.urls import path
from django.contrib import admin
from guesthouse import views


urlpatterns = [
    path('', views.home, name='home'),
    path('guesthouse/reservation/', views.reservation, name='reservation'),
    path('guesthouse/payement/', views.payement, name='payement'),
    path('guesthouse/reservation/salle/', views.salle_form_view, name='RessalleForm'),
    path('guesthouse/reservation/liste/', views.liste_attributs, name='liste_attributs'),
    path('guesthouse/reservation/liste/edit/', views.update, name='update'),
    path('guesthouse/reservation/liste/delete/', views.delete, name='delete'),
    path('guesthouse/reservation/ajoutSalle/', views.salle_view, name='SalleForm'),
    path('guesthouse/reservation/ajoutChambre/', views.hebergement_view, name='HebergementForm'),
    path('guesthouse/reservation/ajoutSalle//', views.update, name='update'),
    path('guesthouse/reservation/ajoutChambre/edit/', views.update, name='update'),
    path('guesthouse/connexion/', views.connexion, name='connexion'),
    path('guesthouse/deconnexion/', views.deconnexion, name='deconnexion'),
    path('guesthouse/reservation/hebergement/', views.hebergement_form_view, name='ReshebergementForm'),
]
