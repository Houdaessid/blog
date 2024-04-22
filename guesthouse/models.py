# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=45)
    prenom = models.CharField(max_length=45)
    numtel = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adresse = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'client'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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


class Reshebergement(models.Model):
    idhebergement = models.IntegerField(primary_key=True)
    numcourrier = models.IntegerField()
    etablissement = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    demandeur = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    capacite = models.IntegerField()
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
    idressalle = models.OneToOneField('Salle', models.DO_NOTHING, db_column='idressalle', primary_key=True)
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


class Utilisateur(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    email = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')
    modpasse = models.CharField(max_length=45, db_collation='utf8mb4_0900_ai_ci')

    class Meta:
        managed = False
        db_table = 'utilisateur'
