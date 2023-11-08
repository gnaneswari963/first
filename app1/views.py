from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jampandu(request):
    return HttpResponse("hi jampandu how r u")

def jspider(request):
    return HttpResponse("hlo students")