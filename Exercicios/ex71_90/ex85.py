'''
*Agrupando Dados*
   - Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e 
   sua idade, escreva um programa que agrupe essas pessoas por idade em um dicionário.
'''
lista = [
    ('Adalberto', 74),
    ('Enzo', 12),
    ('ester', 73),
    ('Ana', 4),
]
tupla = {}

tupla = dict.fromkeys(lista)
tupla.setdefault('valor')
print(tupla)