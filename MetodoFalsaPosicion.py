import sympy as sp
print("")
print("")
print("{:^120}".format("Metodo de falsa posicion"))

x=sp.symbols("x")

f = input("Escriba su funcion: ")

print("")


iteraciones = int(input("Ingrese el numero de iteraciones que desea realizar: "))
print("")
a = float(input("Ingrese el valor inicial de F(xi): "))
print("")
b = float(input("Ingrese el valor inicial de F(xF): "))
print("")
tol = 1e-6
print("")
#Esto se utiliza para no sobrecargar la memoria
max_iter = 100
#Esto cambia el string a funcion matematica
f = sp.lambdify(x, f)

fa = f(a)
fb = f(b)

#este if revisa que el intervalo inicial contenga una raiz
if fa * fb >= 0:
    raise ValueError("El intervalo inicial no contiene una raíz.")

print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format("Iteracion", "a", "b", "c", "fa", "fb", "fc"))

for k in range(iteraciones):

    # Calculamos el nuevo punto c y el valor de la función en c
    c = (a * fb - b * fa) / (fb - fa)
    fc = f(c)

    # Verificamos si c es la raíz exacta
    if fc == 0:
        raiz = c
        break
    # Actualizo el intervalo
    if fa * fc < 0:
        b = c
        fb = fc
    else:
        a = c
        fa = fc

    # Verificamos si se ha alcanzado la convergencia
        if abs(b - a) <= tol:
            raiz = c
            break
    print("{:^30} {:^30} {:^30} {:^30} {:^30} {:^30} {:^30}".format(k+1, a, b, c, fa, fb, fc))

# Verificamos si se alcanzó la convergencia
if abs(b - a) <= tol:
    print(f"\nLa raíz aproximada de la función es: {raiz}")
    print(f"Se necesitaron {iteraciones+1} iteraciones para alcanzar la convergencia.")
    print(f"Los valores de la función en los extremos del intervalo final son: f(a) = {fa}, f(b) = {fb}")
else:
    print("")
    print("No se pudo alcanzar la convergencia.")

