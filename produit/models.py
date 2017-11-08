from django.db import models

# Create your models here.

class Produit(models.Model):
	nom = models.CharField(max_length=30)
	prix = models.FloatField()
	descriptif = models.TextField()
	qte = models.PositiveIntegerField()
<<<<<<< HEAD
        image = models.ImageField(
                blank=True, null=True)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.nom
=======
>>>>>>> fc6c34a0682967dc1d86e1fbf6e8a1b7bad56512
