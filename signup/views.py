from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def signup(request):
    return HttpResponse("Welcome to our website!")