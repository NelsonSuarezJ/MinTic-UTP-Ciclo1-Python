edad = 55
semanas = 100
salario = 1000000
genero = "F"


def calculoPension(edad, semanas, salario, genero):
    if semanas >= 250:
        if genero == "M":
            if edad >= 63:
                pension = salario*0.90
                print(f"La pension es de: {pension} pesos")
            else:
                edadpend = 63-edad
                print(f"Le faltan {edadpend} años para pensionarse")
        else:
            if edad >= 58:
                pension = salario*0.90
                print(f"La pension es de: {pension} pesos")
            else:
                edadpend = 58-edad
                print(f"Le faltan {edadpend} años para pensionarse")
    else:
        semanaspend = 250-semanas
        print(f"Le faltan {semanaspend} semanas para pensionarse")


def calculoPension2(edad, semanas, salario, genero):
    if genero == "M" and edad >= 63 and semanas >= 250:
        pension = salario*0.90
        print(f"La pension es de: {pension} pesos")
    elif genero == "M" and edad >= 63:
        semanaspend = 250-semanas
        print(f"Le faltan {semanaspend} semanas para pensionarse")
    elif genero == "M":
        semanaspend = 250-semanas
        edadpend = 63-edad
        print(f"Le faltan {semanaspend} semanas y {edadpend} años para pensionarse")
    elif genero == "F" and edad >= 58 and semanas >= 250:
        pension = salario*0.90
        print(f"La pension es de: {pension} pesos")
    elif genero == "F" and edad >= 58:
        semanaspend = 250-semanas
        print(f"Le faltan {semanaspend} semanas para pensionarse")
    elif genero == "F":
        semanaspend = 250-semanas
        edadpend = 58-edad
        print(f"Le faltan {semanaspend} semanas y {edadpend} años para pensionarse")


calculoPension2(edad, semanas, salario, genero)
