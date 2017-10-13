from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    dateNaiss = models.DateField()
    adresse = models.CharField(max_length=255)
    codePostal = models.IntegerField()
    ville = models.CharField(max_length=255)
    panier = models.ForeignKey("panier.Panier")

