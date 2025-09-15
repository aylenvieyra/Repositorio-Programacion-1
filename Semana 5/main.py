from biblioteca import *

def main():
    titulos = ["CENICIENTA", "CREPUSCULO", "ROMEO Y JULIETA"] + [""] * 17
    ejemplares = [3, 4, 7] + [0] * 17
    cantidad_libros = 3
    opcion = 0

    while opcion != 7:
        print("--- Menú Biblioteca ---")
        print("1. Cargar títulos y ejemplares")
        print("2. Mostrar catálogo completo")
        print("3. Consultar disponibilidad")
        print("4. Listar títulos agotados")
        print("5. Agregar nuevo título")
        print("6. Actualizar ejemplares")
        print("7. Salir")

        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            cantidad_libros = cargar_titulos (titulos, ejemplares, cantidad_libros)
        elif opcion == 2:
            mostrar_catalogo (titulos, ejemplares, cantidad_libros)
        elif opcion == 3:
            consultar_disponibilidad (titulos, ejemplares, cantidad_libros)
        elif opcion == 4:
            listar_agotados (titulos, ejemplares, cantidad_libros)
        elif opcion == 5:
            cantidad_libros = agregar_titulo (titulos, ejemplares, cantidad_libros)
        elif opcion == 6:
            actualizar_ejemplares (titulos, ejemplares, cantidad_libros)
        elif opcion == 7:
            print("Saliendo del sistema...")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()