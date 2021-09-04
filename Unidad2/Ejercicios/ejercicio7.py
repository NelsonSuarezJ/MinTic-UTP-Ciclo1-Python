# Leer dos números enteros y determinar cuál es el mayor.
numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

if numero1 > numero2:
    print("El numero mayor es", numero1)
elif numero2 > numero1:
    print("El numero mayor es", numero2)
else:
    print("Los numeros son iguales")
