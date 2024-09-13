lista_listas = [2,4,6,8,10]

def menor(lista):
    menor = lista[0]

    for numero in lista_listas:
        if numero < menor:
            menor = numero

    return menor
        
res = menor(lista_listas)
print(res)