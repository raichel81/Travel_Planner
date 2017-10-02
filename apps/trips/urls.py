from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^trips/add/$', views.add_trip, name='add_trip'),
    url(r'^destination/(?P<pk>\d+)$', views.destination, name='destination'),
    url(r'^join/(?P<pk>\d+)$', views.join, name='join'),

]