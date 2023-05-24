from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("{:^120}".format("Bienvenido a la calculadora de metodo de biseccion"))

x = symbols("x")
funcion = sympify(input("Ingresa tu funcion: "))
f = lambdify(x, funcion)

print("")

a = float(input("Ingresa el valor de a: "))
print("")
b = float(input("Ingresa el valor de b: "))
print("")
crit = 0.00001

i = 0
ea = 1
x_anterior = 0
if f(a) * f(b) < 0:
    print("")
    print("{:^150}".format("Metodo de biseccion"))
    print("")
    print("{:^30} {:^30} {:^30} {:^30} {:^30}".format("i", "a", "b", "xr", "ea(%)"))

    while ea > crit:
        xr = (a + b) / 2
        ea = abs((xr - x_anterior) / xr)

        if f(xr) * f(a) < 0:
            b = xr
        else:
            a = xr

        x_anterior = xr

        print("{:^30} {:^30} {:^30} {:^30} {:^30}".format(i, a, b, xr, round(ea * 100, 9)))
        i = i + 1

    print("")
    print("El valor de x es ", round(xr, 9), " con error de ", round(ea * 100, 9), "%")
else:
    print(" ")
    print("La funcion no tiene una raiz en el intervalo de " + "x =" + str(a) + " ax= " + str(b))
