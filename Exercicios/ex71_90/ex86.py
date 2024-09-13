'''
Mesclando Dicionários
   - Dado dois dicionários, mescle-os em um único dicionário. Se houver chaves 
   duplicadas, some os valores correspondentes.
'''

valores = {
    'sabonete': 10,
    'ovo': 12,
    'banana': 10,
    'biscoito': 4,
    'sal': 5
}

dicionario = {
        1: 'arroz',
        2: 'aveia',
        4: 'trigo',
        5: 'feijão',
        6: 'lentilha'

}
valores.update(dicionario)
print(valores)