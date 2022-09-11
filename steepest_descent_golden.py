import numpy as np 
import sympy as sym 
import math 
from matplotlib import pyplot as plt 
import csv 

#* Creating symbolic parameters 
x1, x2, x3 = sym.symbols('x1, x2, x3')
# function to minimize
f = x1**2 + 2*(x2**2) + 2*(x3**2) + 2*x1*x2 + 2*x2*x3
# initiation
xi = [2, 4, 10]
k = 0
# initial golden section search direction
a_0 = 0.1587
# convergence parameter
sigma = 0.005
# golden section initial step size 
lamda_i = 0.05
# accuracy of golden section
accuracy = 0.0001

while sigma > 0.005:
    #* first steepest descent 
    c = [sym.diff(f, x1), sym.diff(f, x2), sym.diff(f, x3)]
    c_k = [c[0].subs([(x1, xi[0]), (x2, xi[1]), (x3, xi[2])]), 
            c[1].subs([(x1, xi[0]), (x2, xi[1]), (x3, xi[2])]), 
            c[2].subs([(x1, xi[0]), (x2, xi[1]), (x3, xi[2])])]

    if np.linalg.norm(c_k) <= sigma:
        break
    # steepest descent direction
    d_k = -c_k
    #* Calculate the step direction to minimize f(alpha) = f(x_0 + alpha*d_k) 
    

        


