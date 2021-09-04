import operaciones as op

print("Seleccione una opcion:\n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division")
incorrecto = True
while incorrecto:
    try:
        opcion = int(input("Seleccion: "))
    except:
        print("Error: no ingreso un numero")
    else:
        incorrecto = False

while opcion < 1 or opcion > 4:
    print("Error: el numero ingresado no es una opcion")
    opcion = int(input("Seleccion: "))

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

if opcion == 1:
    resultado = op.suma(num1, num2)
    print("La suma es:", resultado)
elif opcion == 2:
    resultado = op.resta(num1, num2)
    print("La resta es:", resultado)
elif opcion == 3:
    resultado = op.multiply(num1, num2)
    print("La multiplicacion es:", resultado)
elif opcion == 4:
    resultado = op.divide(num1, num2)
    print("La division es: ", resultado)
