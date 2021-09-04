import operaciones as op
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

suma = op.suma(num1, num2)
print(f"La suma: {suma}")

resta = op.resta(num1, num2)
print(f"La resta: {resta}")

multi = op.multiply(num1, num2)
print(f"La multiplicacion: {multi}")

div = op.divide(num1, num2)
print(f"La division es: {div}")
