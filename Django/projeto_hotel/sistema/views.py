from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def hospedagem(request):
    return render(request, 'hospedagem.html')

def aluguelcarro(request):
    return render(request, 'aluguelcarro.html')

def lazerbemestar(request):
    return render(request, 'lazerbemestar.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def feedback(request):
    return render(request, 'feedback.html')
