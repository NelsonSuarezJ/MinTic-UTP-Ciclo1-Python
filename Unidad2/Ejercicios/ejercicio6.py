# Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
numero = int(input("Ingrese un numero de 2 digitos: "))

if numero < 0:
    numero = numero*-1

if numero >= 10 and numero < 100:
    decenas = numero//10
    unidades = numero % 10
    if decenas == unidades:
        print("Los 2 digitos son iguales")
    else:
        print("Los 2 digitos son diferentes")
else:
    print("El numero no es de 2 digitos")
