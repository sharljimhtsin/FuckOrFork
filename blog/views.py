from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Comment, Variable
from django.forms.models import model_to_dict


# Create your views here.
def index(request):
    return HttpResponse("OK")


def get_variable_by_key(key):
    obj = None
    try:
        obj = Variable.objects.get(keyName=key)
    except Variable.DoesNotExist:
        obj = None
    if obj is None:
        return None
    else:
        dict_obj = model_to_dict(obj)
        value = dict_obj['keyValue']
        if value.strip() == '':
            return None
        else:
            return value
