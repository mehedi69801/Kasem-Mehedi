def add(*numbers):
    suma = 0
    for i in numbers:
        suma += i
    return suma


def even(x):

    lista = []
    for i in range(1, x+1):
        if i % 2 == 0:
            lista.append(i)
    return lista
