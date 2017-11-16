from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Produit, Comment
from .forms import CommentForm

# Create your views here.

def produit_list(request):
    produits = Produit.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'produit/produit_list.html', {'produits': produits, 'nbar': 'produits'})

def produit_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'produit/produit_detail.html', {'produit': produit, 'nbar': 'produits'})

def add_comment_to_produit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.produit = produit
            comment.save()
            return redirect('produit_detail', pk=produit.pk)
    else:
        form = CommentForm()
    return render(request, 'produit/add_comment_to_produit.html', {'form': form})
