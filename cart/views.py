# views.py
from cart.cart import Cart
from django.shortcuts import render, redirect
from django.utils import timezone
from produit.models import Produit

def add_to_cart(request, produit_id, quantity):
    produit = Produit.objects.get(id=produit_id)
    cart = Cart(request)
    cart.add(produit, produit.prix, quantity)
    return redirect(get_cart)

def remove_from_cart(request, produit_id):
    produit = Produit.objects.get(id=produit_id)
    cart = Cart(request)
    cart.remove(produit)
    return redirect(get_cart)


def get_cart(request):
    return render(request, 'cart.html', dict(cart=Cart(request)))

def clear_cart(request):
	cart = Cart(request)
	cart.clear()
	return redirect('paye.html')

def payed(request):
	return render(request, 'paye.html')