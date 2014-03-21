import logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext

# Create your views here.
class IndexView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'index.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))

class EntertainmentView(TemplateView):
    template_name = 'entertainment.html'
    
class SportView(TemplateView):
    template_name = 'sport.html'
    
class CultureView(TemplateView):
    template_name = 'culture.html'
    
class TravelView(TemplateView):
    template_name = 'travel.html'
    
class TechnologyView(TemplateView):
    template_name = 'technology.html'
    
class FoodView(TemplateView):
    template_name = 'food.html'
    
class FashionView(TemplateView):
    template_name = 'fashion.html'
    
class OthersView(TemplateView):
    template_name = 'others.html'
    
