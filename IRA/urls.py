"""Configuration des URLs pour l'application IRA

La liste `urlpatterns` route les URLs vers des vues. Pour plus d'informations, voir :
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Exemples :
Vues basées sur des fonctions
    1. Ajouter une importation :  from my_app import views
    2. Ajouter une URL à urlpatterns :  path('', views.home, name='home')
Vues basées sur des classes
    1. Ajouter une importation :  from other_app.views import Home
    2. Ajouter une URL à urlpatterns :  path('', Home.as_view(), name='home')
Inclusion d'un autre URLconf
    1. Importer la fonction include() : from django.urls import include, path
    2. Ajouter une URL à urlpatterns :  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guesthouse import views

urlpatterns = [
      path('admin/', admin.site.urls),
    path('guesthouse/', views.index, name='index'),
    path('guesthouse/index.html', views.index, name='index'),
    path('guesthouse/admin.html/', views.admin, name='admin'),
     path('guesthouse/payement.html/', views.payement, name='payement'),
    path('guesthouse/reservation.html/', views.reservation, name='reservation'),
    path('guesthouse/reservation.html/salle.html/', views.salle_form_view, name='RessalleForm'),
    path('guesthouse/reservation.html/liste.html/', views.liste_attributs, name='liste_attributs'),
    path('guesthouse/reservation.html/liste.html/edit.html/', views.update, name='update'),
    path('guesthouse/reservation.html/liste.html/delete.html/', views.delete, name='delete'),
    path('guesthouse/inscription.html/', views.inscription, name='inscription'),
    path('guesthouse/connexion.html/', views.connexion, name='connexion'),
    path('guesthouse/reservation.html/hebergement.html/', views.hebergement_form_view, name='ReshebergementForm'),
    path('guesthouse/reservation.html/salle_heber.html/', views.salle_heber_form_view, name='RessallehebergementForm'),
     path('guesthouse/reservation.html/ajoutChambre.html/', views.hebergement_view, name='HebergementForm'),
     path('guesthouse/reservation.html/ajoutSalle.html/', views.salle_view, name='SalleForm'),
      path('guesthouse/reservation.html/ajoutSalle.html/edit.html/', views.update, name='update'),
       path('guesthouse/reservation.html/ajoutChambre.html/edit.html/', views.update, name='update'),
       
]
