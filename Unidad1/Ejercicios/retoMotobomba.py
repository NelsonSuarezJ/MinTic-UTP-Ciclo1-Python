largo = int(input("Ingrese largo: "))
ancho = int(input("Ingrese ancho: "))
alto = int(input("Ingrese alto: "))


def calcular_tiempo(largo, ancho, alto):
    metroscubicos = largo*ancho*alto
    minutos = int((metroscubicos/0.5)*3)
    horas = (minutos/60)
    mensaje = "La motobomba llenará el tanque en " + str(minutos) + " minutos, equivalente a " + str(horas) + " horas."
    return mensaje


print(calcular_tiempo(largo, ancho, alto))
