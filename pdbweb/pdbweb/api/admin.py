from django.contrib import admin

# Register your models here.
from pdbweb.api.models import *
admin.site.register(Article)
admin.site.register(Content)
admin.site.register(Media)
admin.site.register(Comment)
admin.site.register(Draft)
