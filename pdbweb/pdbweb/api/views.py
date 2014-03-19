from django.shortcuts import render
from rest_framework.views import View
from rest_framework.renderers import JSONRenderer

#from pdbweb.api.resource import AccountResource
# Create your views here.
class BaseView(View):
    renderers = (JSONRenderer,)

class AccountView(BaseView):
    #resource = AccountResource

    def post(self, request):
        """
        Create an account
        """
        print request
        return {'username':'aaa'}
