from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input('enter topic')
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse('topic inserted')

def insert_webpage(request):
    tn=input('enter topic')
    name=input('enetr name')
    url=input('enter url:')

    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse('webpage inserted')