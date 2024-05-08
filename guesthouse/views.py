from calendar import Calendar
from datetime import date, timedelta
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

import calendar
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import generic
from django.views.generic import View

from .models import *
from .utils import Calendar
from django.utils.safestring import mark_safe

from datetime import date, datetime, timedelta
#import datetime
from django.utils.translation import gettext_lazy as _
from .forms import *
from datetime import datetime
from .models import Hebergement, Reshebergement




def salle_form_view(request):
    form = RessalleForm()  # Initialisez le formulaire en dehors de la condition
    
    if request.method == 'POST':
        # Créez une instance du formulaire avec les données de la requête POST
        form = RessalleForm(request.POST)
        if form.is_valid():
            # Sauvegardez les données du formulaire dans la base de données
            form.save()
            # Redirigez vers une page de succès ou effectuez une autre action
            return redirect('RessalleForm')
    
    return render(request, 'salle.html', {'form': form})

def home(request):
    context = {'role': None}
    user = request.user
    if user and user.is_authenticated:
        role = Role.objects.filter(user=user).first()
        context = {'role': role}
    return render(request, 'home.html', context=context)

def reservation(request):
    return render(request, 'reservation.html')

def admin(request):
    return render(request, 'admin.html')

def payement(request):
    return render(request, 'payement.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle login failure
            return render(request, 'connexion.html', {'error': 'Identifiants invalides'})
    return render(request, 'connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('home')


def hebergement_form_view(request):
    form = ReshebergementForm()  # Initialisez le formulaire en dehors de la condition
    
    if request.method == 'POST':
        # Créez une instance du formulaire avec les données de la requête POST
        form = ReshebergementForm(request.POST)
        if form.is_valid():
            # Sauvegardez les données du formulaire dans la base de données
            form.save()
            # Redirigez vers une page de succès ou effectuez une autre action
            return redirect('ReshebergementForm')
    
    return render(request, 'hebergement.html', {'form': form})

def salle_heber_form_view(request):
    if request.method == 'POST':
        # Créer une instance du formulaire avec les données de la requête POST
        form = RessallehebergementForm(request.POST)
        if form.is_valid():
            # Sauvegarder les données du formulaire dans la base de données
            form.save()
            # Rediriger vers une page de succès ou effectuer une autre action
    else:
        # Créer une instance vide du formulaire
        form = RessallehebergementForm()
    
    return render(request, 'salle_heber.html', {'form': form})

def liste_attributs(request):
    liste_attributs = Ressalle.objects.all()
    return render(request, "liste.html", {'liste_attributs': liste_attributs})

def update(request):
    obj=Ressalle.objects.get(idressalle=2)
    form = RessalleForm(request.POST or None,instance=obj)  
    messages = ''

    if form.is_valid():
        form.save()
        form = RessalleForm()
        messages = "modification avec succès"
    
    return render(request, 'edit.html', {'form': form, 'message': messages})

def delete(request):
    obj = Ressalle.objects.get(idressalle=2)
    obj.delete()
    return render(request, 'liste.html')
class CalendarView(generic.ListView):
    model= Ressalle
    template_name = "calendar.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

         # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

         # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class CalendarViewNew(generic.View):
   # login_url = "guesthouse:signin"
    model = Ressalle
    template_name = "reserve_calendar.html"

    def get(self, request, *args, **kwargs):
        
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        all_events = Ressalle.objects.filter(statue = 'Réservation confirmée')
        events_today = Ressalle.objects.filter(ateSortie=today, statue = 'Réservation confirmée').order_by(" dateEntrée")
        events_month = Ressalle.objects.filter(ateSortie__gte=seven_day_after, statue = 'Réservation confirmée').order_by(" dateEntrée")
        
        # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('statue') == "all":
                all_events = Ressalle.objects.all()
            else:   
                all_events = Ressalle.objects.filter(statue= 'Réservation confirmée')

            for i in all_events:
                event_sub_arr = {}
                event_sub_arr['title'] = i.administration
                dateEntrée = datetime.datetime.strptime(str(i.dateEntrée.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                dateSortie = datetime.datetime.strptime(str(i.dateSortie.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                event_sub_arr['start'] = dateEntrée
                event_sub_arr['end'] = dateSortie
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "events":all_events,
            "events_month": events_month, 
            "events_today": events_today
        }
        return render(request, self.template_name, context)
    
    """ def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("guesthouse:reserve_calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)  """


class reserve_details(View):
    template_name = "reserve_details.html"

    def get(self, request, *args, **kwargs):
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        reservation = Ressalle.objects.filter(dateSortie__gte=today, statue = 'Annulée')
        
        running_reserve = Ressalle.objects.filter(dateSortie=today).order_by(" dateEntrée")
        
        latest_reserve = Ressalle.objects.filter(dateSortie__gte=seven_day_after, statue = 'Réservation confirmée').order_by(" dateEntrée")

        occupied_meeting_room =Ressalle.objects.extra(select={"Reservation.salle": "IN SELECT Salle.type FROM Salle"}).filter(statutres = 'Réservation confirmée', ddateSortie=today)

        empty_meeting_room = Salle.objects.extra(
            select={"Salle.type": "NOT IN SELECT Reservation.salle FROM Resrvation WHERE statutres like 'Réservation confirmée' AND today BETWEEN datedeb AND dateSortie"}
        )

        context = {
            "total_reserve": reservation.count(),
            "running_reserve": running_reserve.count(),
            "total_empty_meeting_room": empty_meeting_room.count(),
            "total_occupied_meeting_room": occupied_meeting_room.count(),
            "latest_reserve": latest_reserve,
        }
        return render(request, self.template_name, context)


class CalendarViewHosting(generic.View):
    #login_url = "guesthouse:signin"
    model = Reshebergement
    template_name = "hosting_calendar.html"

    def get(self, request, *args, **kwargs):
        
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        all_events = Reshebergement.objects.filter(statue='Confirmé')
        events_today = Reshebergement.objects.filter(dates=today, statue='Confirmé').order_by("dateEntrée")
        events_month = Reshebergement.objects.filter(dates__gte=seven_day_after, statut='Confirmé').order_by("dateEntrée")
        
        # if filters applied then get parameter and filter based on condition else return object
        if request.GET:  
            event_arr = []
            if request.GET.get('statue') == "all":
                all_events = Reshebergement.objects.all()
            else:   
                all_events = Reshebergement.objects.filter(statut='Confirmé')

            for i in all_events:
                event_sub_arr = {}
                #event_sub_arr['id'] = i.idhebergement
                event_sub_arr['title'] = i.etablissement
               # event_sub_arr['cap'] = i.capacite
                dateh = datetime.datetime.strptime(str(i.dateh.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                dates = datetime.datetime.strptime(str(i.dates.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
                event_sub_arr['start'] = dateh
                event_sub_arr['end'] = dates
                event_arr.append(event_sub_arr)
            return HttpResponse(json.dumps(event_arr))

        context = {
            "events":all_events,
            "events_month": events_month, 
            "events_today": events_today
        }
        return render(request, self.template_name, context)

class hosting_details(View):
    template_name = "hosting_details.html"

    def get(self, request, *args, **kwargs):
        #today = datetime.datetime.now()
        #current_month = datetime.now().month
        #start_of_month = datetime.date.today().replace(day=1)
        today = date.today()
        seven_day_after = today + timedelta(days=7)

        hebergement = Hebergement.objects.filter(datesortie__gte=today, statuthebg='Annulé')
        
        running_hosting = Hebergement.objects.filter(datesortie=today).order_by("dateheberg")
        
        latest_hosting = Hebergement.objects.filter(datesortie__gte=seven_day_after, statuthebg='Confirmé').order_by("dateheberg")

        occupied_room = Hebergement.objects.extra(select={"Hebergement.roomnum": "IN SELECT Chambre.numero FROM Chambre"}).filter(statuthebg='Confirmé', datesortie=today)

        empty_room = hebergement.objects.extra(
            select={"Chambre.numero": "NOT IN SELECT Hebergement.roomnum FROM Hebergement WHERE statuthebg like 'Confirmé' AND today BETWEEN dateheberg AND datesortie"}
        )

        context = {
            "total_hosting": hebergement.count(),
            "running_hosting": running_hosting.count(),
            "total_room_empty": empty_room.count(),
            "total_occupied_room": occupied_room.count(),
            "latest_hosting": latest_hosting,
        }
        return render(request, self.template_name, context)

def salle_view(request):
    form = SalleForm()  # Initialisez le formulaire en dehors de la condition
    
    if request.method == 'POST':
        # Créez une instance du formulaire avec les données de la requête POST
        form = SalleForm(request.POST)
        if form.is_valid():
            # Sauvegardez les données du formulaire dans la base de données
            form.save()
            # Redirigez vers une page de succès ou effectuez une autre action
            return redirect('SalleForm')
    return render(request, 'ajoutSalle.html', {'form': form})
def hebergement_view(request):
    form = HebergementForm()  # Initialisez le formulaire en dehors de la condition
    
    if request.method == 'POST':
        # Créez une instance du formulaire avec les données de la requête POST
        form = HebergementForm(request.POST)
        if form.is_valid():
            # Sauvegardez les données du formulaire dans la base de données
            form.save()
            # Redirigez vers une page de succès ou effectuez une autre action
            return redirect('HebergementForm')
    return render(request, 'ajoutChambre.html', {'form': form})
def update(request):
    obj=Salle.objects.get(idsalle=1)
    form = SalleForm(request.POST or None,instance=obj)  
    messages = ''

    if form.is_valid():
        form.save()
        form = SalleForm()
        messages = "modification avec succès"
    
    return render(request, 'edit.html', {'form': form, 'message': messages})
def update(request):
    obj=Hebergement.objects.get(idchambre=1)
    form = HebergementForm(request.POST or None,instance=obj)  
    messages = ''

    if form.is_valid():
        form.save()
        form = HebergementForm()
        messages = "modification avec succès"
    
    return render(request, 'edit.html', {'form': form, 'message': messages})