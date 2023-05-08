import sympy as sp
print("{:^120}".format("Metodo de newton"))

a = int(input("Ingrese el numero de a = "))


for i in range(a+1):
    a.append(float(input("Ingrese el valor de a{}: ".format(i))))
    print("")
def horner(a,x):#implementa metodo de horner
        if len(a)==1: #En la lista estan los coeficientes del polinomio
            return a[0] #Y en X el valor a evaluar
        else:
            return a[0] + x * horner(a[1:],x)
x = 1
print(horner(a,x))