"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con 
un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 
mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""
lista1 = []
lista2 = []
contador = 1
contador2 = 0
cantidad = 5
while contador <= cantidad:
    entrada1 = int(input(f"Ingrese numero {contador} de la lista 1: "))
    entrada2 = int(input(f"Ingrese numero {contador} de la lista 2: "))
    lista1.append(entrada1)
    lista2.append(entrada2)
    contador += 1

sumaLista1 = 0
sumaLista2 = 0
while contador2 < cantidad:
    sumaLista1 += lista1[contador2]
    sumaLista2 += lista2[contador2]
    contador2 += 1

if sumaLista1 > sumaLista2:
    print("Lista 1 mayor")
elif sumaLista2 > sumaLista1:
    print("Lista 2 mayor")
else:
    print("Listas iguales")
