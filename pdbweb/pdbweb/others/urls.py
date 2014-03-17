from django.conf.urls import patterns, include, url
from pdbweb.others.views import OthersView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', OthersView.as_view(), name='others'),
)
