from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import RegForm

# Create your views here.

def index(request):
    return HttpResponse("View: registration index")

def reg_view(request):
    context = {}
    context['form'] = RegForm()
    return render(request, "reg.html", context)

