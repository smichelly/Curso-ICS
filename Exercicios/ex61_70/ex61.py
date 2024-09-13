numeros_pares = (2,4,6,8,10,12,14,16,18,20)

Lista_pares = []

for numero in numeros_pares:
    if numero %2 == 0:
        Lista_pares.append(numero)

        print(Lista_pares)