def calcular_cargamento(toneladas):
    kilos = toneladas*1000
    aguacates = int(kilos/0.25)
    arboles = int(aguacates/40)
    mensaje = "Para completar "+str(toneladas)+" toneladas del cargamento se recogieron " + str(
        aguacates) + " aguacates de "+str(arboles)+" arboles."
    return mensaje


print(calcular_cargamento(1))
print(calcular_cargamento(5))
print(calcular_cargamento(23))
print(calcular_cargamento(123))
print(calcular_cargamento(1254))
