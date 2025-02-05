from django.shortcuts import render
from aluguelcarros.models import Carros, Aluguelcarros, Forma_pagamento
from cadastros.models import Cadastro

def home(request):
    return render(request, 'home.html')

def aluguelcarro(request):
    carros = Carros.objects.all()

    return render(request, 'aluguelcarro.html', { 'carros': carros })


def fazer_reserva(request, carro_id):
    carro = Carros.objects.get(id=carro_id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        forma_pagamento = request.POST.get('forma_pagamento')
        imagem = request.FILES.get('imagem')
        forma_pagamento_id = Forma_pagamento.objects.get(nome=forma_pagamento)
        carro_id = request.POST.get('carro_id')
        carro = Carros.objects.get(id=carro_id)
        reserva = Aluguelcarros(carro=carro, nome=nome, cpf=cpf, forma_pagamento=forma_pagamento_id, imagem=imagem)
        reserva.save()

        dados = {
            'mensagem': 'Seu carro foi reservado com sucesso!'
        }

        return render(request, 'form_reserva_carro_confirmacao.html', {'carro': carro}, dados)
    else:
        return render(request, 'form_reserva_carro.html', {'carro': carro})


def lazerbemestar(request):
    return render(request, 'lazerbemestar.html')

def cadastro(request):
    return render(request, 'cadastro.html')


def fazer_cadastro(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        telefone = request.POST.get('telefone')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        tipo_documento = request.POST.get('tipo_documento')
        documento = request.POST.get('documento')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        cadastro = Cadastro(nome_completo = nome_completo, telefone= telefone, cidade= cidade, estado= estado, tipo_documento= tipo_documento, documento= documento, checkin = checkin, checkout= checkout )
        cadastro.save()
        dados = {
            "mensagem": "Sua reserva foi concluída com sucesso!"
        }
        return render(request, "cadastro_confirmacao.html", dados)

    else:
        return render(request, "cadastro.html")

def feedback(request):
    
        return render(request, 'feedback.html')
