from django.shortcuts import render
from django.http import HttpResponse
from .models import TypechoComments, TypechoContents, TypechoFields, TypechoMetas, TypechoOptions, TypechoRelationships, \
    TypechoUsers
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    return HttpResponse("OK")


def get_variable_by_key(key):
    obj = None
    try:
        obj = TypechoOptions.objects.get(name=key)
    except TypechoOptions.DoesNotExist:
        obj = None
    if obj is None:
        return None
    else:
        dict_obj = model_to_dict(obj)
        value = dict_obj['value']
        if value.strip() == '':
            return None
        else:
            return value
