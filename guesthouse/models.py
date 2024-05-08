# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_directeur = models.BooleanField(default=False)
    is_chefreception = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_financier = models.BooleanField(default=False)


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    prenom = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    numtel = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    email = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    adresse = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')

    class Meta:
        managed = False
        db_table = 'client'


class GuesthouseEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'guesthouse_event'


class Hebergement(models.Model):
    idchambre = models.IntegerField(primary_key=True)
    numero = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    prix = models.IntegerField()
    maison = models.IntegerField()
    chambre = models.IntegerField()
    etage = models.IntegerField()
    local = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'hebergement'


class Historique(models.Model):
    idhistorique = models.IntegerField(primary_key=True)
    adressip = models.CharField(db_column='adressIP', max_length=45)  # Field name made lowercase.
    date = models.DateField()
    tache = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'historique'


class Notification(models.Model):
    idnotification = models.IntegerField(primary_key=True)
    consulte = models.IntegerField()
    email = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notification'


class Reshebergement(models.Model):
    idhebergement = models.IntegerField(primary_key=True)
    numcourrier = models.IntegerField()
    etablissement = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    demandeur = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    capacite = models.IntegerField()
    dateheberg = models.DateField()
    dateentree = models.DateField(db_column='dateEntree')  # Field name made lowercase.
    datesorti = models.DateField(db_column='dateSorti')  # Field name made lowercase.
    chambredispo = models.CharField(db_column='chambreDispo', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    priseencharge = models.CharField(db_column='priseEnCharge', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    moyen = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    statue = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    type = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    idchambre = models.ForeignKey(Hebergement, models.DO_NOTHING, db_column='idchambre')

    class Meta:
        managed = False
        db_table = 'reshebergement'


class Ressalle(models.Model):
    idressalle = models.OneToOneField('Salle', models.DO_NOTHING, db_column='idressalle', primary_key=True, related_name='ressalle_idressalle')
    etablissement = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    demandeur= models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    
    dateEntrée = models.DateField(db_column='dateEntree')  # Field name made lowercase.
    dateSortie = models.DateField(db_column='dateSorti')  # Field name made lowercase.
    nomSalleDispo = models.CharField(db_column='nomSalledispo', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    nombrePersonne = models.IntegerField(db_column='nombrePersonne')  # Field name made lowercase.
    typeEvenement = models.CharField(db_column='typeEvenement', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    dejeuner = models.IntegerField()
    pauseCafe= models.IntegerField()
    nombrecourrier = models.IntegerField(db_column='nombreCourrier')  # Field name made lowercase.
    moyen = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    statue = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    commentaire = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    idsalle = models.ForeignKey('Salle', models.DO_NOTHING, db_column='idsalle')

    class Meta:
        managed = False
        db_table = 'ressalle'


class Ressallehebergement(models.Model):
    idressallehebergement = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    etablissement = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    dateentree = models.DateField(db_column='dateEntree')  # Field name made lowercase.
    datesorti = models.DateField(db_column='dateSorti')  # Field name made lowercase.
    nomsalledispo = models.CharField(db_column='nomSalledispo', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    nombrepersonne = models.IntegerField(db_column='nombrePersonne')  # Field name made lowercase.
    typeevenement = models.CharField(db_column='typeEvenement', max_length=45, db_collation='utf8mb4_0900_ai_ci')  # Field name made lowercase.
    dejeuner = models.IntegerField()
    diner = models.IntegerField()
    nombrecourrier = models.IntegerField(db_column='nombreCourrier')  # Field name made lowercase.
    moyen = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    statue = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    commentaire = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    capacite = models.IntegerField()
    nuite = models.IntegerField()
    dateentre = models.DateField(db_column='dateEntre')  # Field name made lowercase.
    datesortie = models.DateField(db_column='dateSortie')  # Field name made lowercase.
    chambre = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')

    class Meta:
        managed = False
        db_table = 'ressallehebergement'


class Restauration(models.Model):
    idrestauration = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    prix = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'restauration'


class Salle(models.Model):
    idsalle = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    prix = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    local = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')

    class Meta:
        managed = False
        db_table = 'salle'