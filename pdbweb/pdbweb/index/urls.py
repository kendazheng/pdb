from django.conf.urls import patterns, include, url
from pdbweb.index.views import IndexView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', IndexView.as_view(), name='index'),
)
