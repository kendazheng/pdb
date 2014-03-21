from django.conf.urls import patterns, include, url
from pdbweb.api.views import *
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^account/$', AccountAPIView.as_view(), name='account-api'),
    url(r'^entertainment/$', EntertainmentAPIView.as_view(), name='entertainment-api'),
)
