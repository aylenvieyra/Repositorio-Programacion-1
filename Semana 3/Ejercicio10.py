def buscar_primera_aparicion(array, valor):
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return -1

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
valor = int(input("Ingrese el número a buscar: "))

posicion = buscar_primera_aparicion(numeros, valor)

if posicion != -1:
    print(f"El número se encuentra en la posición {posicion}")
else:
    print("El número no se encuentra en el array")

