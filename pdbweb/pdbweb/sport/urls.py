from django.conf.urls import patterns, include, url
from pdbweb.sport.views import SportView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', SportView.as_view(), name='sport'),
)
