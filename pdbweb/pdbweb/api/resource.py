from rest_framework.resources import FormResource
from pdbweb.api.form import AccountForm

class AccountView(FormResource):
    fields = ('username','password')

    form = AccountForm
    allow_unknown_form_fields = True
