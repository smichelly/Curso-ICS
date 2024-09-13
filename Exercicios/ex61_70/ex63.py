lista = [5,6,7,8,9]

def produto_lista(produto):
    valor = 1
    for numero in produto:
        valor *= numero

    return produto

res = produto_lista(lista)
print(res)  