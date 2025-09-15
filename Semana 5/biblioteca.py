#Sistema de catálogo de biblioteca

def cargar_titulos (titulos, ejemplares, cantidad_libros):
    while cantidad_libros < 20:
        titulo = input ("Ingrese título (o FIN para terminar): ")
        if titulo == "FIN":
            break
        copias = int(input("Ingrese cantidad de ejemplares: "))
        titulos [cantidad_libros] = titulo
        ejemplares [cantidad_libros] = copias
        cantidad_libros += 1
    return cantidad_libros

def mostrar_catalogo (titulos, ejemplares, cantidad_libros):
    if cantidad_libros == 0:
        print ("El catálogo está vacío.")
        return
    for i in range (cantidad_libros):
        print (titulos[i], ":", ejemplares[i], "copias")

def consultar_disponibilidad (titulos, ejemplares, cantidad_libros):
    titulo = input("Ingrese el título a consultar: ")
    for i in range (cantidad_libros):
        if titulos[i] == titulo:
            print (titulos[i], "tiene", ejemplares[i], "copias")
            return
    print("Ese libro no está en el catálogo.")

def listar_agotados (titulos, ejemplares, cantidad_libros):
    agotados = False
    for i in range (cantidad_libros):
        if ejemplares[i] == 0:
            print (titulos[i], "está agotado")
            agotados = True
    if not agotados:
        print("No hay títulos agotados.")

def agregar_titulo (titulos, ejemplares, cantidad_libros):
    if cantidad_libros >= 20:
        print("No se pueden agregar más títulos (máximo 20).")
        return cantidad_libros
    titulo = input("Ingrese nuevo título: ")
    copias = int(input("Ingrese cantidad de ejemplares: "))
    titulos [cantidad_libros] = titulo
    ejemplares [cantidad_libros] = copias
    cantidad_libros += 1
    return cantidad_libros

def actualizar_ejemplares (titulos, ejemplares, cantidad_libros):
    titulo = input("Ingrse el título a actualizar: ")
    for i in range(cantidad_libros):
        if titulos [i] == titulo:
            print("Actualmente tiene", ejemplares[i], "copias")
            nuevo = int(input("Ingrese la nueva cantidad de ejemplares: "))
            ejemplares [i] = nuevo
            print("Actualizado correctamente.")
            return
    print("Ese libro no está en el catálogo.")
