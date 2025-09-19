numeros = [0] * 6

for i in range(6):
    numeros[i] = int(input(f"Ingrese el número {i+1}: "))

mayor = numeros[0]
posicion = 0

for i in range(1, 6):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i

print("El número mayor es:", mayor)
print("Se encuentra en la posición:", posicion)
