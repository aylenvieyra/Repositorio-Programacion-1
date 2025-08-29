def  convertir_minutos(minutos):
    horas = minutos // 60
    sobrante = minutos - (horas * 60)
    return horas, sobrante

minutos_totales = int(input("Ingrese la cantidad de minutos: "))

horas, minutos_sobrantes = convertir_minutos(minutos_totales)

print(f"{minutos_totales} minutos son {horas} hora(s) y {minutos_sobrantes} minuto(s).")
