from django.conf.urls import patterns, include, url
from pdbweb.travel.views import TravelView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', TravelView.as_view(), name='travel'),
)
