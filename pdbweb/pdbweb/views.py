import logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext

# Create your views here.
class EntertainmentView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'entertainment.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
class SportView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'sport.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
class CultureView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'culture.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
class TravelView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'travel.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
class TechnologyView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'technology.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
class FoodView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'food.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name, RequestContext(request,{}))
    
class FashionView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'fashion.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
class OthersView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'others.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
