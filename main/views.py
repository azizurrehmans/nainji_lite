from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def AboutUs(request):
    return HttpResponse('about us')

def index(request):
    answer = '<h1>NainJi-Lite</h1><br>You have 18 unapplied migration(s).Your project may not work properly until you apply the migrations' 
    
    return HttpResponse(answer)
    
