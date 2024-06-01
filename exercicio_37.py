anos_bissextos = [1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052]

ano = input("digite um ano para checar: ")

if int(ano) in anos_bissextos:
    print("O ano é bissexto")

else:
    print("O ano não é bissexto")