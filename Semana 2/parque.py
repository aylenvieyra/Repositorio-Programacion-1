def mostrar_atracciones():
    print("Autitos chocadores (edad minima 10)")
    print("Tazas giratorias (edad minina 5)")
    print("Montaña rusa (edad minima 12)")

def puede_subir(edad, atraccion):
    if atraccion == "Autitos chocadores" and edad >= 10:
        return True
    elif atraccion == "Tazas giratorias" and edad >= 5:
        return True
    elif atraccion == "Montaña rusa" and edad >= 12:
        return True
    return False

def calcular_precio(atraccion):
    if atraccion == "Autitos chocadores":
        return 8
    elif atraccion == "Tazas giratorias":
        return 5
    elif atraccion == "Montaña rusa":
        return 15
    else:
        return 0
    
def registrar_visita():
    nombre = input("Ingrese nombre del visitante: ")
    edad = int(input("Ingrede edad del visitante: "))
    mostrar_atracciones()
    
def registrar_visita():
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    
    mostrar_atracciones()
    
    atraccion = input("¿A qué atracción queres subir? ")

    if puede_subir(edad, atraccion):
        precio = calcular_precio(atraccion)
        mensaje = ""
    else:
        precio = 0
        mensaje = "No puedes subir a esta atracción"
    return nombre, edad, precio, atraccion, mensaje

def mostrar_resumen(nombre, edad, atraccion, precio, mensaje):
    print("\n--- Resumen de la Visita ---")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Atracción elegida:", atraccion)
    if precio > 0:
        print("Precio: $", precio)
    else:
        print(mensaje)
        
               

        

