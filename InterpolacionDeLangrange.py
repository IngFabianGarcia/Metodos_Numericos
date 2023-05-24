import numpy as np
import sympy as sympys

print("{:^120}".format("Metodo de Lagrange"))

#   0 ,  -3,    4
#   -2,   7,    14

print("X")
filas = int(input("Cuantas filas tendra:"))
columnas = int(input("Cuantas columnas tendra:"))
print("Escribe tu matriz en una linea y separala por espacios: ")
#Aqui se crea el array
datos = list(map(int, input().split()))
#Se crea la matriz principal
xi = np.array(datos)
print(xi)

print("")
print("")

#Pide al usuario la matriz
print("Y")
filas = int(input("Cuantas filas tendra:"))
columnas = int(input("Cuantas columnas tendra:"))
print("Escribe tu matriz en una linea y separala por espacios: ")
#Aqui se crea el array
datos = list(map(int, input().split()))
#Se crea la matriz principal
fi = np.array(datos)
print(fi)

print(f'Su matris x es:{xi} y la matris y es: {fi}')

n = len(xi)
x = sympys.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype=float)
for i in range(0, n, 1):

    # Termino de Lagrange
    numerador = 1
    denominador = 1
    for j in range(0, n, 1):
        if (j != i):
            numerador = numerador * (x - xi[j])
            denominador = denominador * (xi[i] - xi[j])
    terminoLi = numerador / denominador

    polinomio = polinomio + terminoLi * fi[i]
    divisorL[i] = denominador

# simplifica el polinomio
polisimple = polinomio.expand()

# para evaluación numérica
px = sympys.lambdify(x, polisimple)
print('')
print('')
print('valores de fi: ', fi)
print('divisores en L(i): ', divisorL)
print()
print('Polinomio de Lagrange, expresiones: ')
print(polinomio)
print()
print(f'Polinomio de Lagrange: {polisimple}')
