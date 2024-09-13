'''
*Filtrando Valores*
- Dado um dicionário de produtos e seus preços, escreva um programa 
que filtre e exiba apenas os produtos que custam mais de um determinado valor.
'''

valores = {
    'sabonete': 10,
    'ovo': 12,
    'banana': 10,
    'biscoito': 4,
    'sal': 5
}

    
preco = 10
for produto in valores:
    valor = valores[produto]
    if valor >= preco:
        print(produto, valor)