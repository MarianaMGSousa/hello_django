from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade): #os parametros do hello nome e idade
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, sum1, sum2):
    soma = sum1 + sum2
    return HttpResponse('<h1>O valor da soma é {} </h1>'.format(soma))

def subtracao(request, sum1, sum2):
    subtracao = sum1 - sum2
    return HttpResponse('<h1>O valor da subtraçãso é {} </h1>'.format(subtracao))

def multiplicacao(request, sum1, sum2):
    multiplicacao = sum1 * sum2
    return HttpResponse('<h1>O valor da multiplicação é {} </h1>'.format(multiplicacao))

def divisao(request, sum1, sum2):
    divisao = sum1 / sum2
    return HttpResponse('<h1>O valor da divisão é {} </h1>'.format(divisao))