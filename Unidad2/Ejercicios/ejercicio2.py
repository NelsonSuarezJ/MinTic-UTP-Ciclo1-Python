# Leer un número entero y determinar si tiene 3 dígitos
numero = int(input("Ingrese un numero: "))

if numero >= 100 and numero <= 999:
    print("El numero tiene 3 cifras")
else:
    print("El numero no tiene 3 cifras")
