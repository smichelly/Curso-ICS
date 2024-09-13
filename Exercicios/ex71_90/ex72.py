'''
 *Acessando Valores em um Dicionário*
 - Usando o dicionário criado no exercício anterior, escreva um programa 
que pergunte ao usuário o nome de um país e exiba a capital correspondente
'''

dados = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasília',
    'Haiti': 'Porto príncipe',
    'Estados Unidos': 'Washington',
    'Espanha': 'Madrid'
}

pais = input('Digite um país:')


if pais in dados:
        print(dados[pais])
else:
        print('Não sei a capital')
