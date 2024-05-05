from django.urls import path
from django.contrib import admin
from guesthouse import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('guesthouse/', views.index, name='index'),
    path('guesthouse/index.html', views.index, name='index'),
    path('guesthouse/reservation.html/', views.reservation, name='reservation'),
    path('guesthouse/admin.html/', views.admin, name='admin'),
    path('guesthouse/payement.html/', views.payement, name='payement'),
    path('guesthouse/reservation.html/salle.html/', views.salle_form_view, name='RessalleForm'),
    path('guesthouse/reservation.html/liste.html/', views.liste_attributs, name='liste_attributs'),
    path('guesthouse/reservation.html/liste.html/edit.html/', views.update, name='update'),
    path('guesthouse/reservation.html/liste.html/delete.html/', views.delete, name='delete'),
    path('guesthouse/reservation.html/ajoutSalle.html/', views.salle_view, name='SalleForm'),
    path('guesthouse/reservation.html/ajoutChambre.html/', views.hebergement_view, name='HebergementForm'),
     path('guesthouse/reservation.html/ajoutSalle.html/edit.html/', views.update, name='update'),
    path('guesthouse/reservation.html/ajoutChambre.html/edit.html/', views.update, name='update'),
    path('guesthouse/inscription.html/', views.inscription, name='inscription'),
    path('guesthouse/connexion.html/', views.connexion, name='connexion'),
    path('guesthouse/reservation.html/hebergement.html/', views.hebergement_form_view, name='ReshebergementForm'),
    

]
