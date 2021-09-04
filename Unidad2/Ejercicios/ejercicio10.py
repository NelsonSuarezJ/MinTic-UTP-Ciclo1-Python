# Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

from funciones import centenasDecenasUnidades

numero = int(input("Ingrese un numero de 3 digitos: "))

if numero >= 100 and numero < 1000:
    centenas, decenas, unidades = centenasDecenasUnidades(numero)
    multiplo = False
    if centenas % decenas == 0:
        print(f"El numero {centenas} es multiplo de {decenas}")
        multiplo = True
    if centenas % unidades == 0:
        print(f"El numero {centenas} es multiplo de {unidades}")
        multiplo = True
    if decenas % centenas == 0:
        print(f"El numero {decenas} es multiplo de {centenas}")
        multiplo = True
    if decenas % unidades == 0:
        print(f"El numero {decenas} es multiplo de {unidades}")
        multiplo = True
    if unidades % centenas == 0:
        print(f"El numero {unidades} es multiplo de {centenas}")
        multiplo = True
    if unidades % decenas == 0:
        print(f"El numero {unidades} es multiplo de {decenas}")
        multiplo = True

    if not(multiplo):
        print("No hay multiplos")

else:
    print("El numero no es de 3 digitos")
