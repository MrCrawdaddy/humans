from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views


app_name = 'documentaries'
urlpatterns = [
    #url(r'^login/$', auth_views.login, {'template_name': 'documentaries/login.html'}),
    #url(r'^accounts/logout/$', auth_views.logout, {})
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='delete'),
]

