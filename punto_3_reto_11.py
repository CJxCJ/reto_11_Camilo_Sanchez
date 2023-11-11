#función para imprimir una matriz
def matriz(matriz):
  for fila in matriz:
    for elemento in fila:
      print(elemento, end="\t")
        #genera el salto entre filas   
    print()  

#funcion para obtener la matriza transpuesta
def transpuesta(matriz):
  #verifica si la matriz esta vacia
  if not matriz:
    return []
  #obtener el numero de filas y columnas
  filas = len(matriz)
  columnas = len(matriz[0])
  #inicia una matriz vacia para ivertir las dimenciones
  transpuesta = [[0] * filas for _ in range(columnas)]
  #transpone a la matriz ingresada
  for i in range(filas):
    for j in range(columnas):
            #intercambia las posisciones
            transpuesta[j][i] = matriz[i][j]

  return transpuesta
#pide la cantidad de filas, nosotros definimos las columnas
filas = int(input("Ingrese el número de filas de la matriz: "))

#una matriz vacía
m = []


print("Ingrese los elementos de la matriz fila por fila: ")
for i in range(filas):
  fila = input(f"Ingrese los elementos de la fila {i + 1} separados por espacios: ").split()
  fila = [int(elemento) for elemento in fila]
  m.append(fila)
#imprime la matriz transpuesta
resultante = transpuesta(m)
for fila in resultante:
  print(fila)








