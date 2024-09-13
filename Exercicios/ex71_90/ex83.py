'''
- Dado um dicionário, crie um novo dicionário invertendo as chaves e valores do dicionário original.
'''
valores = {
    'sabonete': 10,
    'ovo': 12,
    'banana': 10,
    'biscoito': 4,
    'sal': 5
}
inverter = {}
for valor in valores:

    res = valores[valor]
    
    inverter[res] = valor

print(inverter)    