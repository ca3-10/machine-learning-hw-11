import numpy as np
import math

class BackProp: 
    def __init__(self, point): 
        self.x = np.array([point[0]])
        self.y = np.array([point[1]])

        self.A_1 = np.array([[5], [-5], [5], [-5]])
        self.A_2 = np.array([[10,10,0,0], [0,0,10,10]])
        self.A_3 = np.array([[10,10]])

        self.b_1 = np.array([[-0.75], [1.75], [-3.25], [4.25]])
        self.b_2 = np.array([[-12.5], [-12.5]])
        self.b_3 = np.array([[-2.5]])

        self.A = [self.A_1, self.A_2, self.A_3]
        self.b = [self.b_1, self.b_2, self.b_3]
        self.input = [self.x]
        self.h = [self.x]
    
    def sigmoid(self,input): 
    
        new = [[1/ (1 + math.e ** (-float(value[0])))] for value in input]
        return new
    
    def sigmoid_prime(self,input): 
        one = np.array([[1] for i in range(np.shape(input)[0])])

        return self.sigmoid(input) * (one - self.sigmoid(input))
    
    def forward_prop(self):

        for i in range(3): 
            self.input.append(0)
            self.input[-1] += ((self.A[i] @ self.h[i]) + self.b[i])
            self.h.append(self.sigmoid(self.input[-1]))

        return self.h[-1] 

    def back_prop(self): 
        self.forward_prop()
        
        self.rss = [2 * (self.h[3] - self.y)]
        for i in range(2, 0, -1): 
        
            self.rss.append(self.A[i].transpose() @ (self.rss[2-i] * self.sigmoid_prime(self.input[i+1])))
        
        print(self.rss)


        
        



prop = BackProp([0,0])
prop.back_prop()
