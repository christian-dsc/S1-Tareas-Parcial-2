# La sala tiene 3 filas y 4 columnas.
# 0 = asiento libre
# 1 = asiento reservado

# Crear la matriz de asientos con 3 filas y 4 columnas
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y la columna del asiento
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Reservar el asiento seleccionado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")

# Recorrer la matriz utilizando bucles anidados
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
