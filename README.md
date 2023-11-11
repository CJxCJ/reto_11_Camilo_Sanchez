# reto_11_Camilo_Sanchez

## Punto 1:
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

````python
#funcion para validar que ambas matrices tienen el mismo tamañaño
def validar(m1, m2):
    #se comparan 
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    return False
  return True

#funcion para sumar matrices
def suma(m1, m2):
  if validar(m1, m2):
    resultado = []
    #si la primera funcion retorna True procede a sumar el valor de ambas matrices desde la coordenadas (0,0)
    for i in range(len(m1)):
      fila = []
      for j in range(len(m1[0])):
        fila.append(m1[i][j] + m2[i][j])
        #se añade el nuevo valor al resultado    
        resultado.append(fila)
    return resultado
  else:
    return None

#funcion para restar matrices
def resta(m1, m2):
  if validar(m1, m2):
    resultado = []
    #mismo procedimiento que en la suma pero restando los valores.
    for i in range(len(m1)):
      fila = []
      for j in range(len(m1[0])):
        fila.append(m1[i][j] - m2[i][j])
        #se añade el nuevo valor al resultado    
        resultado.append(fila)
    return resultado
  else:
    return None
    

#EJEMPLO
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[18, 16, 14], [12, 10, 8], [6, 4, 2]]

resultado_suma = suma(m1, m2)
resultado_resta = resta(m1, m2)

if resultado_suma:
  print("Suma de matrices:")
  for fila in resultado_suma:
    print(fila)

if resultado_resta:
  print("Resta de matrices:")
  for fila in resultado_resta:
    print(fila)

````

## Punto 2:
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

````python
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



````

Punto 3:
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

````python
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

````

Punto 4:
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

````python
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
 
````


