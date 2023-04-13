import sympy as sp
print("{:^90}".format("Metodo de newton"))

x =sp.symbols('x')

f = input('Ingrese la funcion: ')

df = sp.diff(f)

f = sp.lambdify(x, df)

df = sp.lambdify(x, df)

x0 = float(input('Escribe el valor inicial: '))
print("")

n = int(input('Cuantas iteraciones desea realizar?: '))

print("")

tol = input('Escriba el error maximo permitido: ')

print("")

tol = float(tol)

print("{:^15} {:^15}".format("Iteracion" , "X") )
for k in range(n):
        x1 = x0 - (f(x0) / df(x0))
        if (abs(x1 - x0) < tol):
                print("{:^15} {:^15}".format(k + 1, x1, end=' '))
        x0=x1
        print("{:^15} {:^15}".format(k+1, x1))




