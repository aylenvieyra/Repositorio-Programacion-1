numeros = [0] * 8

for i in range(8):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))

contador = 0
for i in range(8):
    if numeros[i] > 100:
        contador += 1

print("Numeros mayores a 100: ", contador)
