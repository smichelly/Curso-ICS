from django.shortcuts import render
from aluguelcarros.models import Carros, Aluguelcarros
from cadastros.models import Cadastro
from feedbacks.models import Feedback

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
        inicio_reserva = request.POST.get('inicio_reserva')
        fim_reserva = request.POST.get('fim_reserva')
        carro_id = request.POST.get('carro_id')
        reserva = Aluguelcarros(
            carro=carro, 
            nome=nome, 
            cpf=cpf, 
            forma_pagamento=forma_pagamento, 
            inicio_reserva= inicio_reserva, 
            fim_reserva= fim_reserva)
        reserva.save()

        dados = {
            'mensagem': 'Seu carro foi reservado com sucesso!'
        }

        return render(request, 'form_reserva_carro_confirmacao.html', dados)
    else:
        return render(request, 'form_reserva_carro.html', {'carro': carro})


def lazerbemestar(request):
    return render(request, 'lazerbemestar.html')

def cadastro(request):
    return render(request, 'cadastro.html')


def fazer_cadastro(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        endereco = request.POST.get('endereco')
        telefone = request.POST.get('telefone')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        tipo_documento = request.POST.get('tipo_documento')
        documento = request.POST.get('documento')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        cadastro = Cadastro(
            nome_completo=nome_completo, 
            telefone= telefone, 
            cidade= cidade, 
            estado= estado, 
            tipo_documento=tipo_documento, 
            documento= documento, 
            checkin = checkin, 
            checkout= checkout,
            endereco=endereco )
        cadastro.save()
        dados = {
            "mensagem": "Sua reserva foi concluída com sucesso!"
        }
        return render(request, "cadastro_confirmacao.html", dados)

    else:
        return render(request, "cadastro.html")

def feedback(request):
    return render(request, 'feedback.html')

def coletar_feedback(request):
    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        classificar = request.POST.get('classificar')
        feedback = Feedback(
            comentario = comentario,
            classificar =classificar)
        feedback.save()
        return render(request, "feedback_confirmacao.html")

    else:
        return render(request, "feedback.html")


