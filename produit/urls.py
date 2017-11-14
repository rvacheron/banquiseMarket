from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views

urlpatterns = [
            url(r'^produit/$', views.produit_list, name='produit_list'),
            url(r'^produit/(?P<pk>\d+)/$', views.produit_detail, name='produit_detail'),
            ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)