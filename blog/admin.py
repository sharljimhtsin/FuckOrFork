from django.contrib import admin
from .models import TypechoComments, TypechoContents, TypechoFields, TypechoMetas, TypechoOptions, TypechoRelationships, \
    TypechoUsers

# Register your models here.
admin.site.register(TypechoComments)
admin.site.register(TypechoContents)
admin.site.register(TypechoFields)
admin.site.register(TypechoMetas)
admin.site.register(TypechoOptions)
admin.site.register(TypechoRelationships)
admin.site.register(TypechoUsers)
