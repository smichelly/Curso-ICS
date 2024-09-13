from django.shortcuts import render


def servicos_web(request):
    return render(request, 'servicos_web.html')

def servicos_marketing(request):
    return render(request, 'servicos_marketing.html')

def todos_os_servicos(request):
    return render(request, 'todos_os_servicos.html')