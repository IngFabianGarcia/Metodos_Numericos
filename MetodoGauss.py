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
""""
datos = int(input("Ingrese la cantidad de datos que tendra su matriz: "))

datoscons = int(input("Ingrese la cantidad de datos que tendra la constante: "))

variable1 = []
variable2 = []
variable3 = []

constante1 = []
constante2 = []
constante3 = []


#Ingresa los datos de los 3 vectores
for i in range(datos):
    variable1.append(int(input("Ingrese el valor {} de la primera fila: ".format(i+1))))
    print("")
for i in range(datos):
    variable2.append(int(input("Ingrese el valor {} de la segunda fila: ".format(i+1))))
    print("")
for i in range(datos):
    variable3.append(int(input("Ingrese el valor {} de la tercera fila: ".format(i+1))))
    print("")

#Ingresa los 3 datos de la constante
for i in range(datoscons):
    constante1.append(int(input("Ingrese el valor {} de la constante 1: ".format(i+1))))
    print("")
for i in range(datoscons):
    constante2.append(int(input("Ingrese el valor {} de la constante 2: ".format(i+1))))
    print("")
for i in range(datoscons):
    constante3.append(int(input("Ingrese el valor {} de la constante 3: ".format(i+1))))
    print("")

#Convertir los Matriz ya funcionales al igual que la constante
Matriz = np.array([[variable1], [variable2], [variable3]])
ConstanteFuncional = np.array([[constante1], [constante2], [constante3]])

print(Matriz)
print(ConstanteFuncional)

#Se cambia lo que se trabaja desde el codigo ya que los inputs tienen error ya que no coinciden en tamaño las matrices
#a pesar de que se pongan del mismo tamaño :c
"""

Matriz = np.array([[2, 6, 1], [1, 2, -1], [5, 7, -4]])
ConstanteFuncional= np.array([[7], [-1], [9]])

MetodoGauss(Matriz, ConstanteFuncional)

