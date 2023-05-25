import math
import sympy as np

IteracionesMaximas = 100

def Muller(a, b, c):
    res = 0
    i = 0
    it = -1

    while (True):
        f1 = f(a)
        f2 = f(b)
        f3 = f(c)
        d1 = f1 - f3
        d2 = f2 - f3
        h1 = a - c
        h2 = b - c
        a0 = f3
        a1 = (((d2 * pow(h1, 2)) -
               (d1 * pow(h2, 2))) /
              ((h1 * h2) * (h1 - h2)))
        a2 = (((d1 * h2) - (d2 * h1)) /
              ((h1 * h2) * (h1 - h2)))
        x = ((-2 * a0) / (a1 +
                          abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))
        y = ((-2 * a0) / (a1 -
                          abs(math.sqrt(a1 * a1 - 4 * a0 * a2))))

        if (x >= y):
            it += 1
            res = x + c
            print("{:^30} {:^30}".format(it+1, res))
        else:
            res = y + c
            it += 1
            print("{:^30} {:^30}".format(it+1, res))
        m = res * 100
        n = c * 100
        m = math.floor(m)
        n = math.floor(n)
        it += 1
        print("{:^30} {:^30}".format(it+1, res))
        if (m == n):
            break
        a = b
        b = c
        c = res
        if (i > IteracionesMaximas):
            print("No se puede encontrar la respuesta con este metodo >:c")
            break
        i += 1
    if (i <= IteracionesMaximas):
        print("")
        print(f"el valor de la raiz es: {res}")



x = np.symbols("x")
f = input("Ingrese su funcion: ")
print("")
f = np.lambdify(x, f)
a = float(input("Ingrese el valor de x0: "))
print("")
b = float(input("Ingrese el valor de x1: "))
print("")
c = float(input("Ingrese el valor de x2: "))
print("")

print("{:^30} {:^30}".format("Iteracion", "Raiz"))
Muller(a, b, c)