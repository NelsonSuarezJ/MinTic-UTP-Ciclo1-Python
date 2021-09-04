# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar
# un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
# cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
# informar el importe que gasta la empresa en sueldos al personal.
sueldo = int(input("Ingrese sueldo del empleado entre 100 y 500 (0 para terminar): "))
cuentaSueldoMen = 0
cuentaSueldoMay = 0
sumaSueldos = 0
while sueldo != 0:
    if sueldo > 300:
        cuentaSueldoMay += 1
    else:
        cuentaSueldoMen += 1
    sumaSueldos += sueldo
    sueldo = int(input("Ingrese sueldo del empleado entre 100 y 500 (0 para terminar): "))
print("La cantidad de empleados con sueldo entre 100 y 300: ", cuentaSueldoMen)
print("La cantidad de empleados con sueldo mayor a 300: ", cuentaSueldoMay)
print("El importe total de los sueldos es: ", sumaSueldos)
