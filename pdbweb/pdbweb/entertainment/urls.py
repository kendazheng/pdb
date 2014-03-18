from django.conf.urls import patterns, include, url
from pdbweb.entertainment.views import EntertainmentView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', EntertainmentView.as_view(), name='entertainment'),
)
