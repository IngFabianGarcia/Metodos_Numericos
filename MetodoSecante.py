from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("{:^120}".format("Metodo de la Secante"))

def secant(x0, x1, e, N):

    it = 1
    Condicion = True
    while Condicion:
        if f(x0) == f(x1):
            print('No se puede dividir por 0 >:c')
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        print("{:^30} {:^30} {:^30} ".format(it, x2, f(x2)))

        x0 = x1
        x1 = x2
        it = it + 1

        if it > N:
            print('No converge!')
            break

        Condicion = abs(f(x2)) > e
    print("{:^30} ".format('\n La raiz es: %0.8f' % x2))


x = symbols("x")
funcion = sympify(input("Ingresa tu funcion: "))
f = lambdify(x, funcion)

print("")
x0 = float(input('Ingresa tu primer valor: '))
print("")
x1 = float(input('Ingresa tu segundo valor: '))
print("")
e = float(input('Error Tolerable: '))
print("")
N = int(input('Maximas iteraciones: '))
print("")
print("{:^30} {:^30} {:^30}  ".format("i", "X", "F(x)"))

secant(x0,x1,e,N)