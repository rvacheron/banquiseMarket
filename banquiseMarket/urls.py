"""banquiseMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from banquiseMarket.views import home, mentions, paye
from banquiseMarket.models import LatestEntriesFeed

admin.autodiscover()

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^rss-feed/',LatestEntriesFeed()),
    url(r'^mentions/', mentions, name="mentions"),
    url(r'', include('produit.urls')),
    url(r'', include('contact.urls')),
    url(r'', include('login.urls')),
    url(r'', include('signup.urls')),
    url(r'', include('cart.urls'))
]
