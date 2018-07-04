from django.db import models


class Colonne(models.Model):

    colonne_id = models.CharField(max_length=12)
    commentaire = models.TextField()
    data_type = models.CharField(max_length=32)
    data_type_pivot = models.CharField(max_length=32)
    donnees_perso = models.TextField()
    fk = models.CharField(max_length=32)
    longueur = models.TextField()
    nom_colonne_long = models.TextField()
    nom_court = models.TextField()
#     agr_age_maxi = models.CharField(max_length=32, null=True)
    not_null = models.TextField()
    primary_key = models.CharField(max_length=32)
    table_id = models.TextField()
