from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Produit

# Create your views here.

def produit_list(request):
    produits = Produit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'produit/produit_list.html', {'produits': produits})

def produit_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'produit/produit_detail.html', {'produit': produit})
