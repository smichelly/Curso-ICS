from django.shortcuts import render

def fale_conosco(request):
    return render(request, 'fale_conosco.html')

def localizacao(request):
    return render(request, 'localizacao.html')

