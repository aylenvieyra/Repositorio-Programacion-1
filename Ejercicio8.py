def calcular_edad(año_nacimiento):
    return 2025 - año_nacimiento

anio = int(input("Ingrese su año de nacimiento: "))
edad = calcular_edad(anio)
print("Tu edad aproximada es:", edad)
