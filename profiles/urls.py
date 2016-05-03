from django.conf.urls import url
from . import views


app_name = 'profiles'
urlpatterns = [
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_user, name='edit'),
    url(r'^account/$', views.account_redirect, name='redirect'),
]

