import numpy as np 
import sympy as sym 
import math 
from matplotlib import pyplot as plt 
import csv 

# TODO Golden Section determines the step size for the search 
# TODO Steepest Descent determines the search direction 
# TODO This code combines the two together to accomplish optimization 

#* Creating symbolic parameters 
x1, x2, x3 = sym.symbols('x1, x2, x3')
x = [x1, x2, x3]
# function to minimize
def function(x):
    # defining the function to minimize
    f = x[0]**2 + 2*(x[1]**2) + 2*(x[2]**2) + 2*x[0]*x[1] + 2*x[1]*x[2]
    return f
# initiation
xi = [2, 4, 10]
k = 0
# convergence parameter
sigma = 0.005
# golden section initial step size 
lamda = 0.05
# initial golden section search direction
a_0 = lamda
# accuracy of golden section
accuracy = 0.0001

# defining n for number of max iterations
n = 1000
for i in np.arange(0, n):
    x_k = xi
    #* first steepest descent 
    c = [sym.diff(function(x), x1), sym.diff(function(x), x2), sym.diff(function(x), x3)]
    c_k = [c[0].subs([(x1, x_k[0]), (x2, x_k[1]), (x3, x_k[2])]), 
            c[1].subs([(x1, x_k[0]), (x2, x_k[1]), (x3, x_k[2])]), 
            c[2].subs([(x1, x_k[0]), (x2, x_k[1]), (x3, x_k[2])])]

    if np.linalg.norm(c_k) <= sigma:
        break
    # steepest descent direction
    d_k = -c_k
    #* Calculate the step direction to minimize f(alpha) = f(x_0 + alpha*d_k) 
    # Phase I 
    # 1) calculate f(0), f(a_0), f(a_1) where ai = summation(lamda * 1.618**j) where j is loop iteration number
    # initiate x + alpha*d as val
    x_k1 = xi + a_0*d_k
    # evaluate function value at f(val_k)
    f_k = function(x).subs([(x[0], x_k[0]), (x[1], x_k[1]), (x[2], x_k[2])])
    # calculate gradient at the current point x_k1
    c_k1 = [c[0].subs([(x1, x_k1[0]), (x2, x_k1[1]), (x3, x_k1[2])]), 
            c[1].subs([(x1, x_k1[0]), (x2, x_k1[1]), (x3, x_k1[2])]), 
            c[2].subs([(x1, x_k1[0]), (x2, x_k1[1]), (x3, x_k1[2])])]
    
    if np.linalg.norm(c_k1) <= sigma:
        break
    
    # steepest descent direction updated 
    d_k1 = -c_k1
    



        


