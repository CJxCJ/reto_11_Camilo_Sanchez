#función para sumar los elementos de la misma posición en cada fila
def suma_columna(matriz, columna):
  suma = 0
  for fila in matriz:
    #verifica si la columna seleccionada para su respectiva fila.
    if columna < len(fila):
      suma += fila[columna]
    return suma

#ingresa el número de filas y columnas
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

#ingresa los valores la matriz fila por fila
matriz = []
for i in range(filas):
  fila = input(f"Ingrese los elementos de la fila {i + 1} separados por espacios: ").split()
  fila = [int(x) for x in fila]
  matriz.append(fila)

#se pide la columna que se desea sumar
columna_a_sumar = int(input(f"Ingrese el número de la columna que desea sumar (0 - {columnas - 1}): "))

#resultado
resultado = suma_columna(matriz, columna_a_sumar)
print(f"La suma de la columna {columna_a_sumar} es: {resultado}")
 