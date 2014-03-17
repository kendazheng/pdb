from django.conf.urls import patterns, include, url
from pdbweb.food.views import FoodView

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdbweb.views.home', name='home'),

    url(r'^$', FoodView.as_view(), name='food'),
)
