from django.shortcuts import render


def blog(request):
    return render(request, 'blog.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')