
from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
     # new url definition
     url(r'^panier/$', views.get_cart, name='panier'),
     url(r'^panierajout/(?P<produit_id>[0-9]+)/(?P<quantity>[1-9]+)$', views.add_to_cart, name='add_to_cart'),
     url(r'^panierenleve/(?P<produit_id>[0-9]+)$', views.remove_from_cart, name='remove_from_cart'),
     url(r'^panierclear/$', views.clear_cart, name='clear_cart')
     
]