from django.db import models

# Create your models here.

class Produit(models.Model): 
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
