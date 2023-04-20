import numpy as np
import math
def forward_prop(point):

    x = np.matrix([point[0]])

    A_1 = np.matrix([[5], [-5], [5], [-5]])
    A_2 = np.matrix([[10,10,0,0], [0,0,10,10]])
    A_3 = np.matrix([[10,10]])

    b_1 = np.matrix([[-0.75], [1.75], [-3.25], [4.25]])
    b_2 = np.matrix([[-12.5], [-12.5]])
    b_3 = np.matrix([[-2.5]])

    A = [A_1, A_2, A_3]
    b = [b_1, b_2, b_3]
    input = [x]
    h = [x]

    for i in range(3): 
        input.append(0)
        input[-1] += (np.matmul(A[i], h[i]) + b[i])
        h.append(sigmoid(input[-1]))
    
    return h[-1]

def sigmoid(input): 
    
    new = [[1/ (1 + math.e ** (-float(value[0])))] for value in input]
    return new
    

forward_prop([0,0])
