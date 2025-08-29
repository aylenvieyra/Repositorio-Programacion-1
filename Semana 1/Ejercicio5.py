def es_par(numero):
    if (numero // 2) * 2 == numero:
        return True
    else:
        return False
    
num = int(input("Ingrese un número: "))

if es_par(num):
    print("El número", num, "es par.")
else:
    print("El número", num, "es impar.")
