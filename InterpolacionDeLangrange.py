from sympy import *
init_printing()

# Pedir al usuario los datos de entrada
print("{:^120}".format("Método de interpolacion de Lagrange"))
g = int(input("Ingrese el grado del polinomio: "))
print("")

valor = float(input("Ingrese el valor de x: "))

print("")

x = []
y = []

for i in range(g+1):
    x.append(float(input("Ingrese el valor de X{}: ".format(i))))
    print("")
for i in range(g+1):
    y.append(float(input("Ingrese el valor de Y{}: ".format(i))))
    print("")

# Calcular el valor de f(x) usando el método de Lagrange

resultado = 0

print("{:^30}" "{:^60}".format("Operacion", "x"))

for i in range(g+1):
    termino = y[i]
    for j in range(g+1):
        if i != j:
            termino *= (valor - x[j]) / (x[i] - x[j])
    resultado += termino
    print("{:^30}" "{:^60}".format(i+1, resultado))

# Imprimir el resultado
print("")
print("")
print("")
print("El valor de f(x) para x = {} es {}".format(valor, resultado))
