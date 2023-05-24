import numpy as np
def MetodoGauss(a,b):
    #Revision de entrada pa ver si fabian los escribio bien :v
    if a.shape[0] != a.shape[1]:
        print("No diste una Matriz cuadrada bro")
        return
    if b.shape[1] > 1 or b.shape[0] != a.shape[0]:
        print("Los tamaños de las Matrices no coinciden ._.")
        return

    #Aqui se inicia las variables que se van a utilizar :v
    n = len(b)
    m = n -1
    i = 0
    j = i - 1
    x = np.zeros(n)
    nuevaLinea = "\n"

    #Se muestra la matriz ya junta con las constantes bro
    Matriz_Aumentada = np.concatenate((a, b), axis= 1 , dtype= float)
    print(f"La matriz inicial es: {nuevaLinea}{Matriz_Aumentada}")
    print("")
    print("")
    print("Resultado de la matris ↓")

    #Aplicando la eliminacion de gauss
    while i < n:
        #Esto evita que el programa explote
        if Matriz_Aumentada[i][i] == 0.0:
            print("Se dividio dentro de 0 error :c")
            return

        for j in range (i + 1, n):
            factorEscalado = Matriz_Aumentada[j][i] / Matriz_Aumentada[i][i]
            Matriz_Aumentada[j] = Matriz_Aumentada[j] - (factorEscalado * Matriz_Aumentada[i])
            print(Matriz_Aumentada)
            print("")
            print("  ↓")
        i = i + 1

    #Sustitucion de variables
    x[m] = Matriz_Aumentada[m][n] / Matriz_Aumentada[m][m]

    for k in range(n - 2, -1, -1):
        x[k] = Matriz_Aumentada[k][n]

        for j in range(k + 1, n):
            x[k] = x[k] - Matriz_Aumentada[k][j] * x[j]
        x[k] = x[k] / Matriz_Aumentada[k][k]

    #Mostrando el resultado
    print(f"La  Matriz Ingresada obtiene este resultado")
    for respuesta in range(n):
        print(f"X{respuesta} es {x[respuesta]}")

# Pedir al usuario los datos de entrada
print("{:^120}".format("Método de Gauss"))

#Pide al usuario la matriz
filas = int(input("Cuantas filas tendra:"))
columnas = int(input("Cuantas columnas tendra:"))

print("Escribe tu matriz en una linea y separala por espacios: ")

#Aqui se crea el array
datos = list(map(int, input().split()))

#Se crea la matriz principal
Matriz = np.array(datos).reshape(filas, columnas)

#Matriz de constantes
filas = int(input("Cuantas filas tendra:"))
columnas = int(input("Cuantas columnas tendra:"))

print("Escribe tu matriz en una linea y separala por espacios: ")
datos = list(map(int, input().split()))

ConstanteFuncional = np.array(datos).reshape(filas, columnas)


'''
Matriz = np.array([[2, 6, 1], [1, 2, -1], [5, 7, -4]])
ConstanteFuncional= np.array([[7], [-1], [9]])
'''
MetodoGauss(Matriz, ConstanteFuncional)

