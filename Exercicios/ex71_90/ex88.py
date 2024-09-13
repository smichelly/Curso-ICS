'''
*Removendo Itens com Base em Condição*
   - Dado um dicionário de funcionários e seus salários, escreva um 
   programa que remova todos os funcionários que ganham abaixo de um certo valor.
'''
empresa = {
    'funcionario1': 2000,
    'funcionario2': 1200,
    'funcionario3': 1200,
    'funcionario4': 2000,
    'funcionario5': 1500,
}
def salario(valor):
    for item in valor:
        if item >= 1500:
            print(item)
res = salario(empresa)
print(res)        