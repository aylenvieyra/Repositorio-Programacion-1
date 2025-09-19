numeros = [0] * 6

for i in range(6):
    numeros[i] = int(input(f"ingrese un numero {i+1}: "))

print("array invertido:")
for i in range(5, -1, -1):
    print(numeros[i])
