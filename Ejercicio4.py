def buscar_mayor(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        if n2 >= n3:
            return n1, n2, n3
        else:
            return n1, n3, n2
    elif n2 >= n1 and n2 >= n3:
        if n1 >= n3:
            return n2, n1, n3
        else:
            return n2, n3, n1
    else:
        if n1 >= n2:
            return n3, n1, n2
        else:
            return n3, n2, n1
        
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))    

ordenados = buscar_mayor(n1, n2, n3)

print("Los números ordenados de mayor a menor son:", ordenados)
    