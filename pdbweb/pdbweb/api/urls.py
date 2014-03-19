from django.conf.urls import patterns, include, url
from pdbweb.api.views import AccountView
# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}, name='logout'),
    url(r'^login/$', AccountView.as_view(), name='login'),
)
