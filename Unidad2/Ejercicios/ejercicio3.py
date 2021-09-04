# Leer un número entero de dos dígitos y determinar si ambos dígitos son pares
numero = int(input("Ingrese un numero de 2 cifras: "))

if numero >= 10 and numero <= 99:
    unidad = numero % 10
    decena = numero//10
    if unidad % 2 == 0 and decena % 2 == 0:
        print("Los dos digitos son pares")
    else:
        print("Alguno de los numeros no es par")
else:
    print("El numero no tiene 2 cifras")
