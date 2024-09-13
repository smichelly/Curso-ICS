from django.shortcuts import render


def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')
