from os import *
from sys import *
from collections import *
from math import *

class ComplexNumbers:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def addcomplex(self):
        z1 = complex(self.a, self.b)
        z2 = complex(self.c, self.d)
        add_com = complex(z1 + z2)
        return(add_com)

    def mulcomplex(self):
        z3 = complex(self.a, self.b)
        z4 = complex(self.c, self.d)
        mul_com = complex(z3 * z4)
        return(mul_com)

# Driver's code goes here.

x, y = input().split()
a, b = input().split()
x = int(x)
y = int(y)
a = int(a)
b = int(b)

# Class attribute- Object
cox = ComplexNumbers(x, y, a, b)
g = input()
G = int(g)
if G == 1:
    r1 = cox.addcomplex()
    print("{0}+i{1}".format(int(r1.real),int(r1.imag)))
elif G == 2:
    r2 = cox.mulcomplex()
    print("{0}+i{1}".format(int(r2.real),int(r2.imag)))
else:
    pass
