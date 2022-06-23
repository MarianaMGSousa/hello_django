from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade): #os parametros do hello nome e idade
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))