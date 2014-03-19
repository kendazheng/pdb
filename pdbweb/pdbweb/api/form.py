 from django.forms import Form, CharField, IntegerField, BooleanField

 class AccountForm(Form):
    username = CharField(max_length=30, required=True, help_text="User name")
    password = CharField(max_length=30, required=True, help_text="User password")
