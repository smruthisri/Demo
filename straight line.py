import numpy as np
from sympy import symbols,Eq,solve
import matplotlib.pyplot as plt

a,b=symbols('a,b')
x=list(map(float,input("Enter the X values : ").split()))
x=np.array(x)

y=list(map(float,input("Enter the Y values : ").split()))
y=np.array(y)

xy=sum(np.array(x*y))
x2=sum(np.array(x**2))
sy=sum(np.array(y))
sx=sum(np.array(x))

n=len(x)

eq1=Eq((n*a+b*sx),sy)
eq2=Eq((sx*a+x2*b),xy)
d=solve((eq1,eq2),(a,b))
print("Y =",round(d[a],2),"+",round(d[b],2),"X")

plt.scatter(x,y)
plt.show()
