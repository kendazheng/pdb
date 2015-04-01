import logging
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext


# Create your views here.
class PublishView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'usercenter/publish.html'
    
    def get(self, request):
        return render_to_response(self.template_name, RequestContext(request, {}))


class DraftView(TemplateView):
    logger = logging.getLogger('pdbweb')
    template_name = 'usercenter/publish.html'
    
    def get(self, request):
        return render_to_response(self.template_name, RequestContext(request, {}))
