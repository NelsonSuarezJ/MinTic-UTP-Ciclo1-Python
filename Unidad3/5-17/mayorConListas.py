numeros = [55, 2, 64, 2323, 453, 269, 578, 565]

mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El numero mayor es", mayor)
