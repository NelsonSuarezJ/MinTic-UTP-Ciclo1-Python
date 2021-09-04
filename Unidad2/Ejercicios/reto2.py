def entregar_dinero(valor):
    try:
        valor = int(valor)
        if valor > 1200000:
            respuesta = (
                f"El cajero solo puede entregar 1200000, {valor} supera esa cantidad"
            )
        elif valor % 10000 != 0:
            respuesta = f"Digita una cantidad valida, {valor} no es aceptado"
        else:
            billetes = dict(Cien=100000, Cincuenta=50000, Veinte=20000, Diez=10000)
            respuesta = "Se entrega"
            if valor >= billetes["Cien"]:
                cantidad1 = valor // billetes["Cien"]
                valor = valor % billetes["Cien"]
                respuesta = f"{respuesta}, {cantidad1} billete(s) de 100.000"
            if valor >= billetes["Cincuenta"]:
                cantidad2 = valor // billetes["Cincuenta"]
                valor = valor % billetes["Cincuenta"]
                respuesta = f"{respuesta}, {cantidad2} billete(s) de 50.000"
            if valor >= billetes["Veinte"]:
                cantidad3 = valor // billetes["Veinte"]
                valor = valor % billetes["Veinte"]
                respuesta = f"{respuesta}, {cantidad3} billete(s) de 20.000"
            if valor >= billetes["Diez"]:
                cantidad4 = valor // billetes["Diez"]
                valor = valor % billetes["Diez"]
                respuesta = f"{respuesta}, {cantidad4} billete(s) de 10.000"
    except:
        respuesta = f"Parece que hay un error con el parámetro enviado"
    return respuesta


print(entregar_dinero("Hola"))
print(entregar_dinero(25000))
print(entregar_dinero(880000))
print(entregar_dinero(1550000))
