numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))

valor = int(input("Ingrese el número a buscar: "))
encontrado = False

for i in range(10):
    if numeros[i] == valor:
        print(f"El número se encuentra en la posición {i}")
        encontrado = True
        break

if not encontrado:
    print("El número no se encuentra en el array")
