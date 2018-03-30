from django.shortcuts import render
from Home.models import examp
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html",{})

#login view
def login(request):
    return render(request,"login.html",{})


