# Generated by Django 3.1.2 on 2021-01-02 10:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=25, verbose_name='Prénom')),
                ('N_matricule', models.IntegerField(verbose_name='N° matricule')),
            ],
            options={
                'verbose_name': 'Admin',
                'ordering': ['Nom'],
            },
        ),
        migrations.CreateModel(
            name='Especes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom_vernaculaire', models.CharField(max_length=150, verbose_name='Nom commun')),
                ('Familles', models.CharField(max_length=100)),
                ('Ordre', models.CharField(max_length=100)),
                ('Nom_scientifiques', models.CharField(max_length=150, unique=True, verbose_name='Nom scientifique')),
                ('Photo', models.ImageField(upload_to='media/', verbose_name='Ajouter une photo')),
                ('Description', models.TextField()),
                ('Repartition_geographique', models.CharField(max_length=150, verbose_name='Répartition géographique')),
                ('TaxRef', models.CharField(max_length=150)),
                ('Habitat', models.CharField(max_length=100, verbose_name="Types d'habitat naturel")),
                ('Statut_IUCN', models.CharField(max_length=100, verbose_name='Statut de conservation UICN')),
                ('Categorie_especes', models.IntegerField(choices=[(1, 'Plantes'), (2, 'Champignons'), (3, 'Insectes'), (4, 'Reptiles et Amphibiens'), (5, 'Mammifères'), (6, 'Oiseaux')], verbose_name="Catégorie de l'espèce")),
                ('Auteur_fe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.admin', verbose_name='Auteur fiche espèce')),
            ],
            options={
                'verbose_name': 'Especes',
                'ordering': ['Familles'],
            },
        ),
        migrations.CreateModel(
            name='Personnel_labo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=25, verbose_name='Prénom')),
                ('Email', models.CharField(max_length=100, verbose_name='Adresse é-mail')),
                ('Fonction', models.IntegerField(choices=[(1, 'Botaniste'), (2, 'Directeur'), (3, 'Ecologiste'), (4, 'Paleontologue'), (5, 'Informaticien'), (6, 'Ornithologue'), (7, 'Entomologiste'), (8, 'Autre')], default=8, verbose_name='Fonction')),
                ('N_Martix', models.IntegerField(verbose_name='N° matricule')),
            ],
            options={
                'verbose_name': 'Personnel_labo',
                'ordering': ['Nom'],
            },
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=25, verbose_name='Prénom')),
                ('Photo', models.ImageField(upload_to='media/', verbose_name='Votre photo de profil')),
                ('Email', models.CharField(max_length=100, verbose_name='Adresse é-mail')),
                ('Login', models.CharField(max_length=100, verbose_name='Votre login')),
                ('Pwd', models.CharField(max_length=100, verbose_name='Votre mot de passe')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'ordering': ['Nom'],
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ville', models.CharField(max_length=150, verbose_name="Ville d'observation")),
                ('Departement', models.CharField(max_length=150, verbose_name="Département d'observation")),
                ('Pays', models.CharField(max_length=150, verbose_name='Pays')),
                ('Date', models.DateTimeField(default=datetime.datetime.now, verbose_name="Date d'observation")),
                ('Photos', models.ImageField(upload_to='media/', verbose_name='Ajouter une photo')),
                ('Estimation', models.IntegerField(default=1, verbose_name="Estimation du nombre d'individu")),
                ('Observateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.utilisateur')),
                ('sp_observe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.especes', verbose_name='Espèce observée')),
            ],
            options={
                'verbose_name': 'Observation',
                'ordering': ['Departement'],
            },
        ),
        migrations.AddField(
            model_name='admin',
            name='Personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_site.personnel_labo', verbose_name='Fonction'),
        ),
    ]