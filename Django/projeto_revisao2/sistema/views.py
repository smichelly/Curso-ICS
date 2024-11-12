from django.shortcuts import render

def homepage(request):
    dados = {
        'titulo_pagina': 'Bem Vindo ao curso do ICS',
        'subtitulo_pagina': 'Curso de Programacao com Python e o Django',
        'visitas': 123,
        'lista_visitas': [
            'Gustavo',
            'Kaique',
            'Luiz',
            'Sarah L',
            'Sarah M',
            'Maria Clara',
            'Ana Ju',
            'Ana',
            'Gregory',
        ]

    }
    return render (request, 'index.html', dados)

def clientes(request):
    return render(request, 'cliente.html')

def produtos(request):
    return render(request, 'produtos.html')