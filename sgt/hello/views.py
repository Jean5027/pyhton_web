from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("olá pessoal")

def brian(request):
    return HttpResponse("olá brian")

def david(request):
    return HttpResponse("olá david")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name
    })

def index(request):
    return HttpResponse("<h1 style=\"color:blue\">Hello, world!</h1>")

def index(request):
    return render(request, "hello/index.html")
