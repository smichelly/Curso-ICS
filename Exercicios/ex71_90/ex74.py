'''
Removendo Itens de um Dicionário*
   - Remova um dos países do dicionário criado e exiba o dicionário atualizado.
'''

dados = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasília',
    'Haiti': 'Porto príncipe',
    'Estados Unidos': 'Washington',
    'Peru': 'Lima',
    'França' : 'Paris',
    'Portugal': 'Lisboa',
    'Itália': 'Roma',
}

item_removido = dados.pop('Haiti')
print(dados)
print(item_removido)