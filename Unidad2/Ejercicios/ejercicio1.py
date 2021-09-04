# Leer un número entero y determinar si es un número terminado en 4
numero = int(input("Ingrese un numero: "))
ultimoDigito = numero % 10

if ultimoDigito == 4:
    print("El numero termina en 4")
else:
    print("El numero no termina en 4")
