from django.db import models

# Create your models here.

class Produit(models.Model):
	nom = models.CharField(max_length=30)
	prix = models.FloatField()
	descriptif = models.TextField()
	qte = models.PositiveIntegerField()
	fournisseur = models.ManyToManyField("fournisseur.Fournisseur")


