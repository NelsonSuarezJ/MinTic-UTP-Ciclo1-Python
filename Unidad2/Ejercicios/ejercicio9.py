# Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito.
from funciones import mayorDeTresNumeros
from funciones import centenasDecenasUnidades

numero = int(input("Ingrese un numero de 3 digitos: "))

if numero >= 100 and numero < 1000:
    centenas, decenas, unidades = centenasDecenasUnidades(numero)
    nmayor, pos = mayorDeTresNumeros(centenas, decenas, unidades)
    print(f"El numero mayor es {nmayor} y esta en la posicion {pos}")

else:
    print("El numero no es de 3 digitos")
