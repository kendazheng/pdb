from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from pdbweb.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),
    # url(r'^pdbweb/', include('pdbweb.foo.urls')),

    url(r'^$', RedirectView.as_view(url='/index/')),
    url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^entertainment/$', TemplateView.as_view(template_name='entertainment.html'), name='entertainment'),
    url(r'^sport/$', TemplateView.as_view(template_name='sport.html'), name='sport'),
    url(r'^culture/$', TemplateView.as_view(template_name='culture.html'), name='culture'),
    url(r'^travel/$', TemplateView.as_view(template_name='travel.html'), name='travel'),
    url(r'^technology/$', TemplateView.as_view(template_name='technology.html'), name='technology'),
    url(r'^food/$', TemplateView.as_view(template_name='food.html'), name='food'),
    url(r'^fashion/$', TemplateView.as_view(template_name='fashion.html'), name='fashion'),
    url(r'^others/$', TemplateView.as_view(template_name='others.html'), name='others'),
    url(r'^publish/$', login_required(TemplateView.as_view(template_name='publish.html')), name='publish'),
    url(r'^(?P<tag>\w+)/detail/(?P<id>\d+)/$', ArticleDetailView.as_view(), name='detail'),
    url(r'^usercenter/$', include('pdbweb.usercenter.urls')),
    url(r'^api/', include('pdbweb.api.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
