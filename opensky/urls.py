__author__ = 'pinballwizard'

from django.conf.urls import patterns, url
from opensky import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^feature', views.features, name='features'),
    url(r'^pricing', views.pricing, name='pricing'),
    url(r'^services', views.services, name='services'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^equipment', views.equipment, name='equipment'),
    url(r'^company', views.company, name='company'),
    url(r'^workers', views.workers, name='workers'),
    url(r'^robot\.txt$', TemplateView.as_view(template_name='robot.txt'), name='robot'),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml'), name='sitemap'),
)