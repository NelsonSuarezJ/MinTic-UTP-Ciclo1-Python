def calculo_descuentos(cliente: dict) -> dict:
    descuentos = dict(nombre=cliente['nombre'], agujas=0.0, escolares=0.0, hogar=0.0)
    compraAcumulada = cliente["agujas"] + cliente["escolares"] + cliente["hogar"]
    
    def asignarDesc(desc):
        descuentos["agujas"] = float(desc)
        descuentos["escolares"] = float(desc)
        descuentos["hogar"] = float(desc)

    if cliente["nacional"]:
        if compraAcumulada >= 200000000:
            asignarDesc(10)
        elif cliente["agujas"] > 70000000 and cliente["escolares"] > 30000000 and cliente["hogar"] > 40000000:
            asignarDesc(7)
        else:
            if cliente["agujas"]> 70000000:
                descuentos["agujas"] = float(5)
            if cliente["escolares"]> 30000000:
                descuentos["escolares"]= float(5)
            if cliente["hogar"]>40000000:
                descuentos["hogar"]= float(5)
    else:
        if compraAcumulada >= 100000:
            asignarDesc(8)
        elif cliente["agujas"] > 25000 and cliente["escolares"] > 10000 and cliente["hogar"] > 15000:
            asignarDesc(5)
        else:
            if cliente["agujas"]> 25000:
                descuentos["agujas"] = float(3)
            if cliente["escolares"]> 10000:
                descuentos["escolares"]= float(3)
            if cliente["hogar"]>15000:
                descuentos["hogar"]= float(3)
    return descuentos


compras = {
    "nombre": "Nelson Suarez",
    "nacional": False,
    "agujas": 20000,
    "escolares": 10000,
    "hogar": 20000,
}

print(calculo_descuentos(compras))
