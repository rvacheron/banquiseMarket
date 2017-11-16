# views.py
from cart.cart import Cart
from django.shortcuts import render_to_response
from django.utils import timezone

def get_cart(request):
    return render_to_response('cart.html', dict(cart=Cart(request)))