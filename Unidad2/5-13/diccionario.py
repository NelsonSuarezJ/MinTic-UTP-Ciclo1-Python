
marcasCarro = {0: 'Audi', 2: 'Mercedez', 3: 'BMW', 4: 'Tesla'}

marcaCorta = len(marcasCarro[0])
for i in marcasCarro:
    if len(marcasCarro[i]) < marcaCorta:
        marca = marcasCarro[i]
        marcaCorta = len(marcasCarro[i])
print("La marca de carro mas corta es:", marca)


diccionario1 = dict(nombre="nelson", edad=39, profesional=True, altura=1.74)
diccionario2 = dict(nombre="juan", edad=39, profesional=False, altura=1.74)

for i in diccionario1:
    if diccionario1[i] == diccionario2[i]:
        print(f"La clave {i} es igual")
