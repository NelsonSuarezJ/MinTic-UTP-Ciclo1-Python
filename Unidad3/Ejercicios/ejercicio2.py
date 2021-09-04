# Se ingresan un conjunto de n alturas de personas por teclado.
# Mostrar la altura promedio de las personas.
# Ingresar el numero 0 para terminar
altura = float(input("Ingrese la altura: "))
c = 0
suma = 0
while altura != 0:
    suma += altura
    c += 1
    altura = float(input("Ingrese la altura: "))

promedio = suma/c
print("El promedio de las alturas ingresadas es:", promedio)
