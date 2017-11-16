from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from produit.models import Produit
from archives.forms import SearchForm

# Create your views here.

def archives(request):
    return render(request, 'archives/archives.html', {'nbar': 'archives'})

def archives(request):
    form_class = SearchForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            text=request.POST.get('text','')
            produits = Produit.objects.all()
            strings = [text]
            for string in strings:
            	produits = produits.filter(nom__icontains=string)
            
            return render(request, 'archives/archives_list.html', {
            	'form': form_class,
            	'text':text,
		        'produits':produits,
		        'nbar': 'archives'
		    })

    return render(request, 'archives/archives.html', {
        'form': form_class,
        'nbar': 'archives'
    })