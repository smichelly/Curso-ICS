'''Verificação de Chaves em um Dicionário*
   - Escreva um programa que verifique se um determinado país está presente no dicionário.
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
def pais(presente, lista):
    for item in lista:
        if item == presente: return 'Existe'
    
    return 'Nao existe'

print(pais('Brasil', dados))