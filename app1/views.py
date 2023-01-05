from django.shortcuts import render
from django.http import HttpResponse
from app1.tasks import add

# Create your views here.

def index(request):
    add.delay(2,3)
    return HttpResponse('response done')

