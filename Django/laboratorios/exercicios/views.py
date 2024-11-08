from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def ex1(request):
    frase = 'Olá, Mundo!'
    data = {
        'titulo': 'Exercicio 1. Olá Mundo.',
        'descricao_exercicio' : 'Faça um programa que mostre a frase Ola Mundo',
        'frase' : frase
    }
    return render (request, 'ex1.html', data)

def ex2(request):
    data = {
        'titulo': 'Exercicio 2. Calculo de total.',
        'descricao_exercicio' : 'Faça um programa que receba 2 numeros do usuario e calcule o total.',
    }

    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int (num2)

        data['total'] = total
    return render (request, 'ex2.html', data)

def ex3(request):
    data = {
        'titulo': 'Exercicio 3. Nome e Idade.',
        'descricao_exercicio' : 'Faça um programa que imprima o nome e idade.',
    }

    if request.method =='POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        frase = f'Seu nome é {nome} e sua idade é {idade}'

        data['frase'] = frase
    return render (request, 'ex3.html', data)

def ex4(request):
    data = {
        'titulo': 'Exercicio 4. Soma de dois Números.',
        'descricao_exercicio' : 'Faça um programa que faça a soma de dois números.',

    }
    if request.method =='POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int(num2)
        
        data['total'] = total
    return render (request, 'ex4.html', data)

def ex5(request):
    data = {
        'titulo': 'Exercicio 5. Caracteres de uma Palavara.',
        'descricao_exercicio' : 'Faça um programa que imprima a quantidade de caracteres de uma palavra.',
    }

    if request.method =='POST':
        palavra = request.POST.get('palavra')
        caracteres = f'{len(palavra)}'

        data['caracteres'] = caracteres
    return render (request, 'ex5.html', data)

def ex6(request):
    data = {
        'titulo': 'Exercicio 6. Formar frases com 5 palavras .',
        'descricao_exercicio' : 'Faça um programa que imprima palavras como se fossem frases.',
    }
    if request.method =='POST':
        palavra1 = request.POST.get('palavra1')
        palavra2 = request.POST.get('palavra2')
        palavra3 = request.POST.get('palavra3')
        palavra4 = request.POST.get('palavra4')
        palavra5 = request.POST.get('palavra5')
        total = (palavra1) + (palavra2) + (palavra3) + (palavra4) + (palavra5)

        data['total'] = total

    return render (request, 'ex6.html', data)

def ex7(request):
    data = {
        'titulo': 'Exercicio 7. Número Somado dele mesmo.',
        'descricao_exercicio' : 'Faça um programa que imprima um numero somado dele mesmo.',

    }
    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + int(valor)
        data['soma'] = soma

    return render (request, 'ex7.html', data)

def ex8(request):
    data = {
        'titulo': 'Exercicio 8. Número somado mais 1.',
        'descricao_exercicio' : 'Faça um programa que facça a soma de uma numero mais o numero 1.',

    }

    if request.method == 'POST':
        valor = request.POST.get("valor") 
        soma = int(valor) + 1
        data['soma'] = soma
        
    return render(request, 'ex8.html', data)

def ex9(request):
    data = {
        'titulo': 'Exercicio 9. Olá (nome).',
        'descricao_exercicio' : 'Crie um programa que declare uma variável nome com o seu nome e, exiba a mensagem "Olá, [nome]!".',
    }

    if request.method =='POST':
        nome = request.POST.get('nome')
        frase = f'Olá, {nome}!'

        data['frase'] = frase
    return render (request, 'ex9.html', data)

def ex10(request):
    data = {
        'titulo': 'Exercicio 10. Duas Variáveis Inteiras e Somar esses Valores.',
        'descricao_exercicio' : 'Crie um programa que tenha duas variáveis inteiras, some esses valores e imprima o resultado da soma.'

    }

    if request.method =='POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int(num2)
        
        data['total'] = total
    return render (request, 'ex10.html', data)

def ex11(request):
    data = {
        'titulo' : 'Exercicios 11. Quantidades de Caracteres de uma frase.',
        'descricao_exercicios' : 'Desenvolva um programa que tenha uma variável do tipo string com uma frase qualquer e que mostre a quantidade de caracteres dessa frase.',

    }

    if request.method =='POST':
        frase = request.POST.get('frase')
        caracteres = f'{len(frase)}'

        data['caracteres'] = caracteres
    return render (request, 'ex11.html', data)

def ex12(request):
    data = {
        'titulo' : 'Exercicio 12. Unir duas Variáveis em uma Terceira Variável e Imprimir Resultado.',
        'descricao_exercicio' : ' Faça um programa que contenha duas variáveis string, parte1 e parte2, atribua valores a elas, una as duas em uma terceira variável e imprima o resultado.'
    }

    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        parte3 = str(parte1) + " " + str(parte2)
        data['parte3'] = parte3
    return render (request, 'ex12.html', data)

def ex13(request):
    data = {
        'titulo' : 'Exercicio 13. Variável com o Ano Atual e outra com o Ano de Nascimento.',
        'descricao_exercicio' : ' Crie um programa que tenha uma variável com o ano atual e outra com o ano de nascimento de uma pessoa e imprima a idade dessa pessoa.',

    }

    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex13.html', data)

def ex14(request):
    data = {
        'titulo' : 'Exercicio 14. Trocar Valores.',
        'descricao_exercicio' : ' Escreva um programa que tenha duas variáveis a e b com valores numéricos, troque os valores entre elas e, em seguida, imprima os novos valores de a e b.' 
    }
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex14.html', data)

def ex15(request):
    data = {
      'titulo' : 'Exercicios 15.  Imprimir Variável 3 Vezes',
      'descricao_exercicio' : 'Desenvolva um programa que crie uma variável frase e atribua a ela uma string qualquer. Imprima essa string três vezes seguidas.',
    }
    if request.method == 'POST':
        frase = request.POST.get("frase") 
        frase1 = str(frase) + ' ' + str(frase) + ' ' + str(frase)
        data['frase1'] = frase1
    return render(request, 'ex15.html', data)

def ex16(request):
    data = {
        'titulo' : 'Média de quatro variáveis inteiras.',
        'descricao_exercicio' : 'Faça um programa que declare quatro variáveis inteiras, realize a média desses valores e imprima o resultado.',

    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex16.html', data)

def ex17(request):
    data = {
        'titulo' : 'Exercicio 17. Imprimir Frase com 2 Variáveis com Objeto e uma Cor.',
        'descricao_exercicio' : 'Crie um programa que tenha uma variável com uma string representando o nome de uma cor e outra variável com um objeto (por exemplo, "carro"). Imprima uma frase que combine essas informações, como "carro azul".',
    }

    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra1) + " " + str(palavra2) + " " 
        data['frase'] = frase
    return render (request, 'ex17.html', data)

def ex18(request):
    data = {
        'titulo' : 'Exercicio 18.  Escreva um Programa que Declare Duas Variáveis com Nomes de Cidades.',
        'descricao_exercicio' : 'Escreva um programa que declare duas variáveis com nomes de cidades, para exibir uma frase que diga que uma está a leste da outra, por exemplo, "Paris está a leste de Londres'
    }
    
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra2) + " está a leste de " + str(palavra1)
        data['frase'] = frase
    return render(request, 'ex18.html', data)

def ex19(request):
    data = {
        'titulo': 'Exercicio 19. Olá, [nome]!.',
        'descricao_exercicio' : ' Escreva uma função chamada saudacao que aceite um nome como argumento e imprima "Olá, [nome]!.',
    }

    if request.method =='POST':
        nome = request.POST.get('nome')
        saudacao = f'Olá, {nome}!'

        data['saudacao'] = saudacao
    return render (request, 'ex19.html', data)

def ex20(request):
    data = {
        'titulo': 'Exercicio 20. Soma de dois Números.',
        'descricao_exercicio' : ' Crie uma função chamada soma que receba dois números como parâmetros e retorne a soma desses dois números..',

    }
    if request.method =='POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        total = int(num1) + int(num2)
        
        data['total'] = total
    return render (request, 'ex20.html', data)

def ex21(request):
    data = {
        'titulo' : 'Exercicios 21. Caracteres de uma frase.',
        'descricao_exercicio' : ' Desenvolva uma função conta_caracteres que receba uma string como argumento e retorne o número de caracteres na string.',

    }

    if request.method =='POST':
        frase = request.POST.get('frase')
        conta_caracteres = f'{len(frase)}'

        data['conta_caracteres'] = conta_caracteres
    return render (request, 'ex21.html', data)

def ex22(request):
    data = {
        'titulo' : 'Exercicio 22. Unir duas Variáveis em uma Nova Strings e Imprimir Resultado.',
        'descricao_exercicio' : 'Faça uma função chamada concatena que receba duas strings, parte1 e parte2, como parâmetros, una-as em uma nova string e retorne essa nova string.'
    }

    if request.method == 'POST':
        parte1 = request.POST.get("parte1") 
        parte2 = request.POST.get("parte2")
        nova_string = str(parte1) + " " + str(parte2)
        data['nova_string'] = nova_string
    return render (request, 'ex22.html', data)

def ex23(request):
    data = {
        'titulo' : 'Calcular idade que receba o ano atual(2024) e o ano de nascimento, e retorne a idade da pessoa.',
        'descricao_exercicio' : ' Escreva uma função chamada calcula_idade que receba o ano atual e o ano de nascimento, e retorne a idade da pessoa.',
    }
    if request.method == 'POST':
        Ano_de_nascimento = request.POST.get("ano_de_nascimento") 
        ano_atual = 2024
        data_de_nascimento = int(ano_atual) - int(Ano_de_nascimento)
        data['data_de_nascimento'] = data_de_nascimento
    return render(request, 'ex23.html', data)

def ex24(request):
    data = {
        'titulo' : 'Exercicio 24. Trocar Valores.',
        'descricao_exercicio' : ' Crie uma função chamada troca_valores que receba dois valores a e b como parâmetros, troque os valores entre eles e retorne ambos.',
    }
    if request.method == 'POST':
        a = request.POST.get("a")
        b = request.POST.get("b")
        troca = a, b = b, a
        data['troca'] = troca
    return render(request, 'ex24.html', data)

def ex25(request):
    data = {
        'titulo': 'Exercicio 25. Repetir string.',
        'descricao_exercicio' : ' Desenvolva uma função chamada repete_string que receba uma string frase e um número inteiro n, e retorne a string repetida n vezes.',

    }

    if request.method == 'POST':
        string = request.POST.get("string") 
        repete_string = str(string) * 3
        data['repete_string'] = repete_string
        
    return render(request, 'ex25.html', data)

def ex26(request):
    data = {
        'titulo' : 'Exercicio 26. Média de Quatro Números.',
        'descricao_exercicio' : ' Faça uma função chamada media que receba quatro números como argumentos e retorne a média desses números.',
    }

    if request.method == 'POST':
        valor1 = request.POST.get("valor1") 
        valor2 = request.POST.get("valor2")
        valor3 = request.POST.get("valor3") 
        valor4 = request.POST.get("valor4")
        media = (int(valor1) + int(valor2) + int(valor3) + int(valor4))/4
        data['media'] = media
    return render (request, 'ex26.html', data)


def ex27(request):
    data = {
        'titulo' : 'Exercicio 27. Objeto e Cor.',
        'descricao_exercicio' : ' Crie uma função chamada descreve_cor que receba duas strings, cor e objeto, e retorne uma descrição do tipo "objeto cor".',
    }
    if request.method == 'POST':
        palavra1 = request.POST.get("palavra1") 
        palavra2 = request.POST.get("palavra2")
        frase = str(palavra1) + " " + str(palavra2) + " " 
        data['frase'] = frase
    return render (request, 'ex27.html', data)

def ex28(request):
    data = {
        'titulo' : 'Exercicio 28. Posição Geografica',
        'descricao_exercicio' : 'Escreva uma função chamada posicao_geografica que receba os nomes de duas cidades e retorne uma frase indicando que a primeira cidade está a leste da segunda.',
    }
    if request.method == 'POST':
        cidade1 = request.POST.get('cidade1') 
        cidade2 = request.POST.get('cidade2')
        frase = (cidade1) + ' está a leste de ' + (cidade2)
        data['frase'] = frase

    return render(request, 'ex28.html', data)

def ex29(request):
    data = {
        'titulo' : 'Exercicio 29. Calculadora Simples',
        'descricao_exercicio' : 'Peça ao usuário que digite dois números e então pergunte qual operação ele deseja realizar (adição, subtração, multiplicação ou divisão). Realize a operação e mostre o resultado.'
    }

    if request.method == 'POST':
        num1 = request.POST.get('num1') 
        num2 = request.POST.get('num2')
        operacao = input("Digite qual operaação você deseja : + - * / ")

    elif operacao == '+':
        soma = int(num1) + int(num2)
        data['soma'] = soma

    elif operacao == '-':
        subtracao = int(num1) - int(num2)
        data['subtracao'] = subtracao

    elif operacao == '*':
        multiplicacao = int(num1) * int(num2)
        data['multiplicacao'] = multiplicacao

    elif operacao == '/':
        divisao = int(num1) / int(num2)
        data['divisao'] = divisao

    return render(request, 'ex29.html', data, operacao)

    #if operacao == '+':
    #soma = int(num1) + int(num2)
    #print(soma)

    #elif operacao == '-':
    #subtracao = int(num1) - int(num2)
    #print(subtracao)

    #elif operacao == '*':
    #multiplicacao = int(num1) * int(num2)
    #print(multiplicacao)

    #elif operacao == '/':
    #divisao = int(num1) / int(num2)
    #print(divisao)


