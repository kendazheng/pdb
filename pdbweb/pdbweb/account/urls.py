from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^login/$', 'pdbweb.account.views.login', name='login'),
)
