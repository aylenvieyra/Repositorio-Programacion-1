numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input(f"Ingrese el numero: {i+1}: "))

suma = 0
for i in range(10):
    suma += numeros[i]

print("La suma de todos los elementos es:", suma)
