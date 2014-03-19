from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),
    # url(r'^pdbweb/', include('pdbweb.foo.urls')),

    url(r'^$', include('pdbweb.index.urls')),
    url(r'^entertainment/', include('pdbweb.entertainment.urls')),
    url(r'^sport/', include('pdbweb.sport.urls')),
    url(r'^culture/', include('pdbweb.culture.urls')),
    url(r'^travel/', include('pdbweb.travel.urls')),
    url(r'^technology/', include('pdbweb.technology.urls')),
    url(r'^food/', include('pdbweb.food.urls')),
    url(r'^fashion/', include('pdbweb.fashion.urls')),
    url(r'^others/', include('pdbweb.others.urls')),
    url(r'^api/', include('pdbweb.api.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
