def calculadora_impar_par(numero):
    lista_numeros_impar = "1,3,5,7,9"
    ultimo_numero = [-1]

    if ultimo_numero in lista_numeros_impar:
        print("impar")
    else:
        print("par")

while True:
    valor = input("Digite um número para descobrir se é impar ou par:")
    calculadora_impar_par(valor)