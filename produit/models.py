from django.db import models
from django.utils import timezone

# Create your models here.

<<<<<<< HEAD
class Produit(models.Model):
=======
class Produit(models.Model): 
>>>>>>> 49118f825e27073741915e9d2d9d4299745029b0
    nom = models.CharField(max_length=30)
    prix = models.FloatField()
    descriptif = models.TextField()
    qte = models.PositiveIntegerField()
    image = models.ImageField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nom
