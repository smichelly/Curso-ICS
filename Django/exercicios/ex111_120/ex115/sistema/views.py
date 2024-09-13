from django.shortcuts import render

def artigos_tecnologia(request):
    return render(request, 'artigos_tecnologia.html')

def artigos_saude(request):
    return render(request, 'artigos_saude.html')

def todos_os_artigos(request):
    return render(request, 'todos_os_artigos.html')