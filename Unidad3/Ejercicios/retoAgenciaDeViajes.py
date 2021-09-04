def presupuesto(datos: list, identificacion: int) -> dict:
    respuesta = dict(nombre='', apellido='', cantidad_personas='', presupuesto=0, habitaciones=0)
    for cliente in datos:
        if cliente['id'] == identificacion:
            respuesta['nombre'] = cliente['nombre']
            respuesta['apellido'] = cliente['apellido']
            cantidad_personas = cliente['adultos']+cliente['niños']+cliente['bebes']
            respuesta['cantidad_personas'] = cantidad_personas
            habitaciones = int(cantidad_personas/4) if cantidad_personas % 4 == 0 else int(cantidad_personas/4)+1
            respuesta['habitaciones'] = habitaciones

            def calculoPresupuesto(precio):
                adultos = cliente['adultos']*precio
                ninos = (cliente['niños']*precio)*0.8
                presupuesto = adultos+ninos
                respuesta['presupuesto'] = presupuesto

            if cliente['estrellas'] == 1:
                calculoPresupuesto(40000)
            elif cliente['estrellas'] == 2:
                calculoPresupuesto(70000)
            elif cliente['estrellas'] == 3:
                calculoPresupuesto(110000)
            elif cliente['estrellas'] == 4:
                calculoPresupuesto(180000)
            else:
                calculoPresupuesto(220000)
            return respuesta

    return f'Ningun cliente con id {identificacion}'


datos = [{'id': 8533644, 'nombre': 'Nelson', 'apellido': 'Charris', 'adultos': 2, 'niños': 2, 'bebes': 0, 'estrellas': 3},
         {'id': 32774589, 'nombre': 'Marina', 'apellido': 'Meléndez', 'adultos': 2, 'niños': 0, 'bebes': 0, 'estrellas': 3},
         {'id': 32569874, 'nombre': 'Liliana', 'apellido': 'Obredor', 'adultos': 2, 'niños': 1, 'bebes': 1, 'estrellas': 4},
         {'id': 8547963, 'nombre': 'Alejandro', 'apellido': 'Pérez', 'adultos': 3, 'niños': 3, 'bebes': 1, 'estrellas': 4},
         {'id': 32478159, 'nombre': 'Ana', 'apellido': 'Cantillo', 'adultos': 1, 'niños': 0, 'bebes': 0, 'estrellas': 2},
         {'id': 80545851, 'nombre': 'Nelson', 'apellido': 'Suarez', 'adultos': 1, 'niños': 1, 'bebes': 0, 'estrellas': 5}]

print(presupuesto(datos, 80545851))
