from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("olá pessoal")

def brian(request):
    return HttpResponse("olá brian")

def david(request):
    return HttpResponse("olá david")

