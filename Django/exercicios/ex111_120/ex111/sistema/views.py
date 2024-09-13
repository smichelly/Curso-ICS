from django.shortcuts import render

def produtos_eletronicos(request):
    return render(request, 'produtos_eletronicos.html')

def produtos_moveis(request):
    return render(request, 'produtos_moveis.html')

def todos_os_produtos(request):
    return render(request, 'todos_os_produtos.html')


