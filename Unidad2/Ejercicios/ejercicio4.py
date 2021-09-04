# Leer un número entero de dos dígitos menor que 20 y determinar si es primo
numero = int(input("Ingrese un numero de dos digitos menor que 20: "))

c = 0
if numero >= 10 and numero <= 99:
    if numero < 20:
        for i in range(2, numero):
            if numero % i == 0:
                c += 1
        if c > 0:
            print(f"El numero {numero} no es primo")
        else:
            print(f"El numero {numero} es primo")
    else:
        print("El numero no es menor de 20")
else:
    print("El numero no es de dos digitos")
