from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Hebergement, Reshebergement,Ressalle,Ressallehebergement, Salle,Utilisateur


class ReshebergementForm(ModelForm):
    class Meta:
        model = Reshebergement
        fields ="__all__" 
        exclude=['idhebergement','idchambre']         

class RessalleForm(ModelForm):
    class Meta:
        model = Ressalle
        fields ="__all__"
        exclude=['idressalle','idsalle']              

class RessallehebergementForm(ModelForm):
    class Meta:
        model = Ressallehebergement
        fields ="__all__"                                  

class UtilisateurForm(ModelForm):
    class Meta:
        model = Utilisateur
        fields ="__all__"         

class SalleForm(ModelForm):
    class Meta:
        model=Salle
        fields="__all__"  
        exclude=['idsalle']   

class HebergementForm(ModelForm):
    class Meta:
        model=Hebergement
        fields="__all__"
        exclude=['idchambre']   