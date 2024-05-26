lista = list(range(1, 101))
print(lista)


def dobro(x):
    return 2 * x


lista_dobro = list(map(dobro, lista))
print(lista_dobro)

lista_dobro = list(map(lambda x: x * 2, lista))
print(lista_dobro)