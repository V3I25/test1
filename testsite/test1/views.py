from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения")

def new(request):
    return HttpResponse("<h5>HI</h5>")