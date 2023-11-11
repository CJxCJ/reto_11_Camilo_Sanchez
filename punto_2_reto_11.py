#funcion para validar que ambas matrices tienen el mismo tamañaño
def validar(m1, m2):
  num_columnas_m1 = len(m1[0])
  num_filas_m2 = len(m2)

  return num_columnas_m1 == num_filas_m2

 
#función para multiplicar matrices
def producto(m1, m2):
  if validar(m1, m2):
    resultado = []

    for i in range(len(m1)):
      fila = []
      #recorremos las columnas de la segunda matriz.
      for j in range(len(m2[0])):
        punto = 0
        #ahora las columnas 
        for k in range(len(m2)):
          #operamos y añadimos a la fila el resultado para luego añadirlo a la respuesta
          punto += m1[i][k] * m2[k][j]
        fila.append(punto)
      resultado.append(fila)
    return resultado
  else:
    return None
    
#EJEMPLO    
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

resultado_producto = producto(m1, m2)

if resultado_producto:
    print("producto de matrices:")
    for fila in resultado_producto:
        print(fila)


