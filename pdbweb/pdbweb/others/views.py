import logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext

# Create your views here.
class OthersView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'others/others.html'
    
    def get(self, request):
        self.logger.info('aaa')
        self.logger.debug('aaa')
        self.logger.error('aaa')
        return render_to_response(self.template_name,RequestContext(request,{}))
    
