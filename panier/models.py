from django.db import models

# Create your models here.
class Panier(models.Model):
    produits = models.OneToMany("produit.Produit")
