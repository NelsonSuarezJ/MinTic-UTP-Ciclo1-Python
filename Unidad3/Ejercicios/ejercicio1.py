# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.
i = 1
c1 = 0
c2 = 0
while i <= 10:
    nota = int(input(f"Ingrese la nota {i}: "))
    if nota >= 7:
        c1 += 1
    else:
        c2 += 1
    i += 1

print("Los alumnos con nota igual o superior a 7 son:", c1)
print("Los alumnos con nota inferior a 7 son:", c2)
