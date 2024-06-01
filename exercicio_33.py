nota1 = input("Digite  a primeira nota:")
nota2 = input("Digite  a segunda nota:")
nota3 = input("Digite  a terceira nota:")
nota4 = input("Digite  a quarta nota:")

media = int(nota1 + nota2 + nota3 + nota4)/4

if media >= 7:
    print("Aprovado")

elif  5 <= media <7:   
    print("Em recuperação")
else:
    print("Reprovado")