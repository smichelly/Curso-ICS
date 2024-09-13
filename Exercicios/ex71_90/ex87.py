'''
*Transformação de Dados*
   - Dado um dicionário de alunos e suas notas, escreva um programa que transforme
    as notas em conceitos (A, B, C, etc.) com base em uma tabela de conversão.

'''
dados = {
    'Lara': 5,
    'Adrian': 7,
    'Mariana': 8,
    'felipe': 2,
    'lorena': 9

}
def nota(aluno, nota, conversao):
    if aluno in nota:
        nota[aluno] = conversao
        print('A nota de', aluno, 'é', nota)

res = nota(dados)
print(res)