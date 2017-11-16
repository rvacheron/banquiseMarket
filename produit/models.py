from django.db import models
from django.utils import timezone

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

class Comment(models.Model):
    produit = models.ForeignKey('produit.Produit', related_name='comments')
    auteur = models.CharField(max_length=200)
    commentaire = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


