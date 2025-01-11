from django.shortcuts import render
from aluguelcarros.models import Carros, Aluguelcarros, Forma_pagamento

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
        forma_pagamento_id = Forma_pagamento.objects.get(nome=forma_pagamento)
        carro_id = request.POST.get('carro_id')
        carro = Carros.objects.get(id=carro_id)
        reserva = Aluguelcarros(carro=carro, nome=nome, cpf=cpf, forma_pagamento=forma_pagamento_id)
        reserva.save()
        return render(request, 'form_reserva_carro_confirmacao.html', {'carro': carro})
    return render(request, 'form_reserva_carro.html', {'carro': carro})

def lazerbemestar(request):
    return render(request, 'lazerbemestar.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def feedback(request):
    return render(request, 'feedback.html')
