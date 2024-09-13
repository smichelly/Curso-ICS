'''
*Dicionário de Dicionários*
   - Crie um dicionário onde cada chave é o nome de um estudante e 
   o valor é outro dicionário com as matérias e suas respectivas notas. Escreva um programa para calcular
    a média das notas de cada estudante e exibir o resultado.
'''
valor = {
    'guilherme': {
        'fisica': 3,
        'matematica': 7,
        'historia': 5,
        'geografia': 10
    },
    'marcela': {
        'fisica': 8,
        'matematica': 3,
        'historia': 5,
        'geografia': 2
    },
    'joaquim': {
        'fisica': 10,
        'matematica': 2,
        'historia': 6,
        'geografia': 4
    },
    'carol': {
        'fisica': 5,
        'matematica': 7,
        'historia': 10,
        'geografia': 3
    },
}
for estundante,materia in valor.items():
    notas = materia.values()
    media = len(notas) / len(estundante)
    print(media)