from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def prediction(request):
    header_str = 'Hello'
    template = loader.get_template('prediction.html')
    context = {
        'var1': header_str
    }
    return HttpResponse(template.render(context, request))