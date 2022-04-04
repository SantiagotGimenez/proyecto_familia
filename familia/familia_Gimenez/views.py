from multiprocessing import context
from re import template
from django.shortcuts import render
from django.template import loader
from .models import Familiares
from django.http import HttpResponse

# Create your views here.
def listado_familiares(request):

    template = loader.get_template('listado_familiares.html')
    familiares = Familiares.objects.all()
    print(familiares)
    context = {
        'familiares':familiares,
    }
    return HttpResponse(template.render(context,request))