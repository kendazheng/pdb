from django.conf.urls import patterns, include, url
from pdbweb.fashion.views import FashionView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', FashionView.as_view(), name='fashion'),
)
