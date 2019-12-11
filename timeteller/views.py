from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    return HttpResponse('Welcome to the time machine')

def today(request):
    d = datetime.datetime.today()
    return HttpResponse('Current date and time:'+ str(d))

def timestamp(request):
    ts = datetime.datetime.now().timestamp()
    return HttpResponse('Current timestamp the page loading is ' + str(ts))



