import sympy as sp
print("{:^120}".format("Metodo de newton"))

x=sp.symbols("x")

f = input("Escriba su funcion: ")

print("")
#Esto calcula la derivada de la funcion

df = sp.diff(f)

#Esto cambia el string a funcion matematica

f = sp.lambdify(x, f)
df = sp.lambdify(x, df)

n = int(input("Ingrese el numero de iteraciones que desea realizar: "))

x0 = float(input('Escribe el valor inicial: '))

tol = 1e-6

print("{:^30} {:^30} {:^30} {:^30}".format("Iteracion", "F(p[n])", "f'(P)[n]", "Raiz"))


for k in range(n):
        x1 = x0 - f(x0)/df(x0)
        if(abs(x1-x0)<tol):
                print("{:^30} {:^30} {:^30} {:^30}".format(k+1, f(x0), df(x0), x1))
        x0=x1
        print("{:^30} {:^30} {:^30} {:^30}".format(k+1, f(x0), df(x0), x1))




