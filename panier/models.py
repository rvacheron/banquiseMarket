from django.db import models

# Create your models here.
class Panier(models.Model):
    produtis = models.ManyToManyField("produit.Produit")
