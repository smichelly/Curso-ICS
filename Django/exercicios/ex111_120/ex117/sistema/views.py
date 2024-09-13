from django.shortcuts import render

def testemunhos_clientes(request):
    return render(request, 'testemunhos_clientes.html')

def testemunhos_funcionarios(request):
    return render(request, 'testemunhos_funcionarios.html')

