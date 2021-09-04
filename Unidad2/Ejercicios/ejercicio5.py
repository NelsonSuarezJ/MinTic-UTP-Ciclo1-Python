# Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.
from funciones import esPrimo

numero = int(input("Ingrese un numero de 2 digitos: "))
negativo = False

if numero < 0:
    numero = numero*-1
    negativo = True


if numero >= 10 and numero < 100:
    if esPrimo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")
    if negativo:
        print("El numero es negativo")
    else:
        print("El numero no es negativo")
else:
    print("El numero no es de 2 digitos")
