from django.db import models

# Create your models here.

class Fournisseur(models.Model):

	nom = models.CharField(max_length=30)
	email = models.EmailField(max_length=100)
	adresse = models.CharField(max_length=200)
	code_postal = models.PositiveIntegerField()
	ville = models.CharField(max_length=50)
	produit = models.ManyToMany("produit.Produit")
