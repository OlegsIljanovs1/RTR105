>>> #-*- coding: utf-8 -*-
from math import sin
# a0, a1 , a2 , a3
# s0, S1, S2, S3 -> S
# (1.) * (2) = (2.) - float * int = float
# (1.) * (2.)= (2.) - float * float = float
# float(input()) -> float
x= float(input("Lietotāj, lūdzu, ievadi argumentu (x): "))
#print type(x)

y = sin(x)
print("sin(%.2f) = %.2f"%(x,y))

a0 = (-1)**0*x**1/(1)
s0 = a0
print("a0= %.2f s0 = %.2f"%(a0,s0))

#a1 = (-1)**1*x**3/(1*2*3)
#a1 = a0* (-1)*x*x/(2*3)
a = a*(-1)*x*x/(2*3)
#S = S + a1
S = S + a
print("a1=%.2f S1 = %.2f"%(a1,S1))

#a2 = (-1)**2*x**5/(1*2*3*4*5)
#a2 = a1* (-1)*x*x/(4*5)
a = a * (-1)*x*x/(4*5)
#S = S + a2
S = S + a
print("a2= %.2f S2 = %.2f"%(a2,S2))

#a3 = (-1)**3*x**7/(1*2*3*4*5*6*7)
#a3 = a2 * (-1)*x*x/(6*7)
a = a* (-1)*x*x/(6*7)
S = S + a3

print("a3 = %.2f S3 = %.2f"%(a3,S3))