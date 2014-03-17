from django.conf.urls import patterns, include, url
from pdbweb.culture.views import CultureView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', CultureView.as_view(), name='culture'),
)
