from django.shortcuts import render

def galeria_urbanas(request):
    return render(request, 'galeria_urbanas.html')

def galeria_natureza(request):
    return render(request, 'galeria_natureza.html')