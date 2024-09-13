lista_entrada = [ 
    (1),
    (2),
    (3),
    (4),
    (5),
    (6),
    (7),
    (8),
    (9)
]

for par in range(0, len(lista_entrada)):
    numero = lista_entrada[par]
    if numero %2 == 0:
        print(str(numero))