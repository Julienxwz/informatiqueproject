import math as m
import matplotlib.pyplot as plt
import numpy as np

def function_droite(x,a1, b1) :
    return a1*x+b1

print(function_droite(4,1,-2))


def function_parabole(x, a2, b2, C2) :
    return a2*x**2+b2*x+C2

print(function_parabole(4, 6, 7, 15))

def function_hyperbole(x, a3, b3, c3):
    return a3/(b3*x+c3)

print(function_hyperbole(1, 578, 4, 3.5))

def function_expo_x2(x, a4, b4) :
    return a4*(m.exp(b4*x**2))

print(function_expo_x2(2, 6, 7))

#X=np.arange(-5,5,0.1)
#Y=function_droite(X,1,3)
#plt.plot(X,Y)
#plt.show()


fig, ax = plt.subplots()
#ax.set_xlim(-5,5)
#ax.set_ylim(-5,5)
ax.plot(np.arange(-5,5,0.1)),[function_droite(x,1,3) for x in np.arange(-5,5,0.1)]
plt.show()
