__author__ = 'pinballwizard'

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from opensky import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^feature', views.features, name='features'),
    url(r'^pricing', views.pricing, name='pricing'),
    url(r'^services', views.services, name='services'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^equipment', views.equipment, name='equipment'),
    url(r'^company', views.company, name='company'),
    url(r'^workers', views.workers, name='workers'),
)