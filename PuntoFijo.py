import numpy as np
print(" {:^30} {:^30} ".format("iteracion", "X"))
def g(x):
    return 0.5*pow(10.0-x*x*x,0.5)

p0= 0.5
tol= 1.0e-6
n0=1000
i=1


while i<=n0:
    p=g(p0)
    if np.abs(p0-p)<tol:
        break
    print(" {:^30} {:^30} ".format(i, p))
    i +=1
    p0=p