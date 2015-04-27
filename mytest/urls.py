from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('opensky.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)