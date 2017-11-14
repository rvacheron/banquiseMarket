
from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

urlpatterns = [
     # new url definition
     url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
     url(r'^logout/$', auth_views.logout,{'template_name': 'logged_out.html','next_page': '/'}, name='logout')
]