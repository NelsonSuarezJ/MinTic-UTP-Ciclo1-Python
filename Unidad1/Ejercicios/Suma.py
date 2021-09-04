# utilizando la funcion de phyton
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = sum(numeros)
print('La suma de los numeros es: ' + str(suma))

# utilizando una funcion creada
num1 = 6
num2 = 7


def sumas(a, b):
    res = a+b
    return res


llamadafun = sumas(num1, num2)
print(llamadafun)
