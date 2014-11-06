from django.conf.urls import patterns, include, url
from pdbweb.usercenter.views import *

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    #url(r'^$', SportView.as_view(), name='usercenter_index'),
    url(r'^publish/$', PublishView.as_view(), name = 'usercenter_publish'),
)
