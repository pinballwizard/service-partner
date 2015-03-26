__author__ = 'pinballwizard'

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from opensky import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'index', views.index),
    url(r'features', views.features),
    url(r'pricing', views.pricing),
    url(r'services', views.services),
    url(r'contacts', views.contacts),
    url(r'equipment', views.equipment),
    url(r'company', views.company),
    url(r'workers', views.workers),
)