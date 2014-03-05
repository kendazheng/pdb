from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('pdbweb.index',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', 'views.index', name='index'),
)
