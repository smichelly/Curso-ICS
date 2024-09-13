'''*Contagem de Ocorrências*
- Escreva um programa que conte a ocorrência de cada palavra em uma 
lista de palavras e armazene
o resultado em um dicionário.
'''
lista = ['Brinco','Pulseira','colar','Relógio','Brinco']
ocorrencia = {}

for palavra in lista:
    if palavra in ocorrencia:
        ocorrencia[palavra] += 1
    else:
        ocorrencia[palavra] = 1

print(ocorrencia)        

conta_ocorrecia = len(ocorrencia)
print(conta_ocorrecia)