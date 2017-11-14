from django.shortcuts import render
from django.utils import timezone
from produit.models import Produit


def home(request):
	last_prod = Produit.objects.latest('published_date')
	return render(request,'home.html', {'last_prod':last_prod})