from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')

def sobrealoja(request):
    return render(request, 'sobrealoja.html')

def contato(request):
    return render(request, 'contato.html')