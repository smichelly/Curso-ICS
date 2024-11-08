from django.shortcuts import render

def home(request):
    data = { 'menssage' : 'Ola a partir da view'}
    return render(request, 'home.html', data)