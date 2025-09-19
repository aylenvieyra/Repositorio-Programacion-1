numeros = [0, 0, 0, 0, 0]

for i in range(5):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))

print("Contenido del array:")
for i in range(5):
    print(f"Posición {i}: {numeros[i]}")
