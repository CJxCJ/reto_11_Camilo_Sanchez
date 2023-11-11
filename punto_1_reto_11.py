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
