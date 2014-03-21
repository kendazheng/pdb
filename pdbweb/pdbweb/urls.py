from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from pdbweb.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),
    # url(r'^pdbweb/', include('pdbweb.foo.urls')),

    url(r'^$', include('pdbweb.index.urls')),
    url(r'^entertainment/$', EntertainmentView.as_view(), name='entertainment'),
    url(r'^sport/$', SportView.as_view(), name='sport'),
    url(r'^culture/$', CultureView.as_view(), name='culture'),
    url(r'^travel/$', TravelView.as_view(), name='travel'),
    url(r'^technology/$', TechnologyView.as_view(), name='technology'),
    url(r'^food/$', FoodView.as_view(), name='food'),
    url(r'^fashion/$', FashionView.as_view(), name='fashion'),
    url(r'^others/$', OthersView.as_view(), name='others'),
    url(r'^usercenter/$', include('pdbweb.usercenter.urls')),
    url(r'^api/', include('pdbweb.api.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
