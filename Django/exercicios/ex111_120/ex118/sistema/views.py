from django.shortcuts import render

def portfolio_design(request):
    return render(request, 'portfolio_design.html')

def portfolio_desenvolvimento(request):
    return render(request, 'portfolio_desenvolvimento.html')

def portfolio_completo(request):
    return render(request, 'portfolio_completo.html')
