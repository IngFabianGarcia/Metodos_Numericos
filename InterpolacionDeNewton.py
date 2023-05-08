from sympy import *
init_printing()
print("{:^120}".format("Método de interpolacion de newton"))
# Pedir al usuario los datos de entrada
g = int(input("Ingrese el grado del polinomio: "))
print("")

valor = float(input("Ingrese el valor de F: "))

print("")

x = []
y = []

for i in range(g+1):
    x.append(float(input("Ingrese el valor de x{}: ".format(i))))
    print("")
for i in range(g+1):
    y.append(float(input("Ingrese el valor de y{}: ".format(i))))
    print("")

# Calcular las diferencias divididas
dif_div = []
for i in range(g+1):
    dif_div.append([0] * (g+1))
for i in range(g+1):
    dif_div[i][0] = y[i]
for j in range(1, g+1):
    for i in range(g-j+1):
        dif_div[i][j] = (dif_div[i+1][j-1] - dif_div[i][j-1]) / (x[i+j] - x[i])

# Calcular el valor de f(x) usando el método de Newton
resultado = dif_div[0][0]
for j in range(1, g+1):
    termino = 1
    for i in range(j):
        termino *= (valor - x[i])
    resultado += dif_div[0][j] * termino
    print(resultado)

# Imprimir el resultado
print("El valor de f(x) para F = {} es {}".format(valor, resultado))
