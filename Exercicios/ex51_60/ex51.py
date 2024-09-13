numeros_impares= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def impares(lista):
    valor = len(lista) -1
    auxilio = []
    for valor in range(0, len(numeros_impares)):
        numero = numeros_impares[valor]
        if numero %2 == 1:
            auxilio.append(numero)
            print(str(numero))
impares(numeros_impares) 