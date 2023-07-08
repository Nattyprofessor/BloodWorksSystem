from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tutorial

# Create your views here.

def tutorial(request):
    template = loader.get_template('tutorial/tutorial.html')
    context = {
        'check': True
    }
    return HttpResponse(template.render(context,request))


def my_tutorials(request):
    all_tutorials = Tutorial.objects.all().values()
    template = loader.get_template('tutorial/all_tutorials.html')
    context = {
        'all_tutorials': all_tutorials,
    }
    return HttpResponse(template.render(context, request))

def tutorial_detail(request, id):
    tutorial = Tutorial.objects.get(id=id)
    template = loader.get_template('tutorial/tutorial_detail.html')
    context = {
        'tutorial': tutorial,
    }
    return HttpResponse(template.render(context, request))