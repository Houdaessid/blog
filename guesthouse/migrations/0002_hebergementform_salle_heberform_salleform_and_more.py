# Generated by Django 4.1.7 on 2024-04-21 16:25

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('guesthouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HebergementForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_courrier', models.IntegerField(verbose_name='Nombre de courrier')),
                ('etablissement', models.CharField(max_length=100, verbose_name='Etablissement')),
                ('demandeur', models.CharField(max_length=100, verbose_name='Demandeur')),
                ('capacite', models.IntegerField(verbose_name='Capacité')),
                ('date_arrivee', models.DateField(verbose_name='Date au')),
                ('date_depart', models.DateField(verbose_name='Date du')),
                ('chambre_disponible', models.CharField(max_length=100, verbose_name='Chambre disponible')),
                ('prise_charge', models.CharField(max_length=100, verbose_name='Prise en charge')),
                ('nombre_personnes', models.IntegerField(verbose_name='Nombre de personnes')),
                ('moyen', models.CharField(max_length=100, verbose_name='Moyen')),
                ('statue', models.CharField(max_length=100, verbose_name='Statut')),
                ('type', models.TextField(blank=True, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Salle_heberForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('etablissement', models.CharField(max_length=100, verbose_name='Etablissement')),
                ('date_arrivee', models.DateField(verbose_name='Date au')),
                ('date_depart', models.DateField(verbose_name='Date du')),
                ('nom_salle_souhaite', models.CharField(max_length=100, verbose_name='Nom de la salle souhaitée')),
                ('nombre_personnes', models.IntegerField(verbose_name='Nombre de personnes')),
                ('type_evenement', models.CharField(max_length=100, verbose_name="Type d'événement")),
                ('pause_cafe', models.IntegerField(verbose_name='Pause café')),
                ('dejeuner', models.IntegerField(verbose_name='Déjeuner')),
                ('diner', models.IntegerField(verbose_name='Dîner')),
                ('nombre_courrier', models.IntegerField(verbose_name='Nombre de courrier')),
                ('moyen', models.CharField(max_length=100, verbose_name='Moyen')),
                ('statue', models.CharField(max_length=100, verbose_name='Statut')),
                ('commentaire', models.TextField(blank=True, verbose_name='Commentaire')),
            ],
        ),
        migrations.CreateModel(
            name='SalleForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('etablissement', models.CharField(max_length=100, verbose_name='Etablissement')),
                ('date_arrivee', models.DateField(verbose_name='Date au')),
                ('date_depart', models.DateField(verbose_name='Date du')),
                ('nom_salle_souhaite', models.CharField(max_length=100, verbose_name='Nom de la salle souhaitée')),
                ('nombre_personnes', models.IntegerField(verbose_name='Nombre de personnes')),
                ('type_evenement', models.CharField(max_length=100, verbose_name="Type d'événement")),
                ('pause_cafe', models.IntegerField(verbose_name='Pause café')),
                ('dejeuner', models.IntegerField(verbose_name='Déjeuner')),
                ('diner', models.IntegerField(verbose_name='Dîner')),
                ('nombre_courrier', models.IntegerField(verbose_name='Nombre de courrier')),
                ('moyen', models.CharField(max_length=100, verbose_name='Moyen')),
                ('statue', models.CharField(max_length=100, verbose_name='Statut')),
                ('commentaire', models.CharField(blank=True, max_length=255, verbose_name='Commentaire')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='nom',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
