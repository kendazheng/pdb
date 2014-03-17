from django.conf.urls import patterns, include, url
from pdbweb.technology.views import TechnologyView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', TechnologyView.as_view(), name='technology'),
)
