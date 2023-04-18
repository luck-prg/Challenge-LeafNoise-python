
""""
1) Desarrollar una función que reciba una lista de números y devuelva una lista con los números ordenados 
(no se podrán usar funciones para ordenar listas).

"""


def ordenar_list(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1):
            if lista[j] > lista[j+1]:
                valor = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = valor
    print(lista)
    return lista


ordenar_list([5, 3, 2, 6, 1])
ordenar_list([4, 6, 12, 5])
ordenar_list([48, 97, 16, 31])

""""
2) Desarrollar una función que reciba un número y devuelva el factorial de 
ese número.

"""


def factorial(number):
    cant = 0
    carga = 1
    while cant < number:
        carga *= (number - cant)
        cant += 1
    print(carga)


""""Ejemplos resueltos:"""

factorial(3)
factorial(5)
factorial(7)


""""
3) Desarrollar una función que reciba un número "N" 
y devuelva una lista con "N" términos de la serie de Fibonacci.

"""


def fibonacci(number):
    lista_fibonacci = list(range(number))
    pos = 2
    while pos < number:
        lista_fibonacci[pos] = lista_fibonacci[pos-2] + \
            lista_fibonacci[pos-1]
        pos += 1
    print(lista_fibonacci)


""""Ejemplos resueltos:"""

fibonacci(10)
fibonacci(12)
fibonacci(15)
