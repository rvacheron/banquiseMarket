from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     # new url definition
     url(r'^archives/$', views.archives, name='archives')
]
