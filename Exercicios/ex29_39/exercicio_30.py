num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

if int(num1) > int(num2):
    print("O primeiro é o maior:" + num1)
    
elif int(num2) > int(num1):
    print("O segundo é o maior:" + num2)

else: 
    print("Eles são iguais")
