from . import views
from django.http import HttpResponse
from django.shortcuts import render

def homeone(request):
    return render(request,'root.html')
