from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello Sergey")

def intro(request):
    return HttpResponse("This is my first time using Django")

def todo(request):
    return render(request, 'todo.html')