# Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.

from funciones import decenasUnidades

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))
numero3 = int(input("Ingrese tercero numero: "))

decenas1, unidades1 = decenasUnidades(numero1)
decenas2, unidades2 = decenasUnidades(numero2)
decenas3, unidades3 = decenasUnidades(numero3)

digitoMayor = decenas1
mayor = numero1

if decenas1 > digitoMayor:
    digitoMayor, mayor = decenas1, numero1
if unidades1 > digitoMayor:
    digitoMayor, mayor = unidades1, numero1
if decenas2 > digitoMayor:
    digitoMayor, mayor = decenas2, numero2
if unidades2 > digitoMayor:
    digitoMayor, mayor = unidades2, numero2
if decenas3 > digitoMayor:
    digitoMayor, mayor = decenas3, numero3
if unidades3 > digitoMayor:
    digitoMayor, mayor = unidades3, numero3

print(f"El digito mayor es:{digitoMayor} y esta en el numero: {mayor}")
