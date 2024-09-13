def maior_menor(lista):
    contador = len(lista) -1
    res = []
    

    while contador >= 0:
        temperatura_menor = contador <= 0
        temperatura_maior = contador >= 0

        res.append(temperatura_menor, temperatura_maior)
        contador = contador-1
        
        return res
    
    temperaturas = maior_menor([1, 2, 3, 4, 5])
    print(temperaturas)
