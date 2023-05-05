import numpy as np
import math

class BackProp: 
    def __init__(self, A, b, point): 
        self.x = np.array([point[0]])
        self.y = np.array([point[1]])

        self.A = A
        self.b = b
        self.input = [self.x]
        self.h = [self.x]

    def sigmoid(self,input): 
    
        new = [[1/ (1 + math.e ** (-float(value[0])))] for value in input]
        return np.array(new)
    
    def sigmoid_prime(self,input): 
        one = np.array([[1] for i in range(np.shape(input)[0])])

        return self.sigmoid(input) * (one - self.sigmoid(input))
    
    def outer_product(self, matrix_1, matrix_2): 
        return np.array(matrix_1 @ matrix_2.transpose())
    
    def forward_prop(self):

        for i in range(3): 
            self.input.append(0)
    
            if len(self.h[i]) == 1: 
                self.input[-1] += ((self.A[i] * self.h[i]) + self.b[i])
            else: 
                self.input[-1] += ((self.A[i] @ self.h[i]) + self.b[i])
            self.h.append(self.sigmoid(self.input[-1]))
        
        self.predication = self.h[-1]

        return self.h[-1] 

    def back_prop(self): 
        self.forward_prop()

        
        self.rss_h = [2 *(self.h[3] -self.y)]

        for i in range(2, 0, -1): 
        
            self.rss_h.append(self.A[i].transpose() @ (self.rss_h[2-i] * self.sigmoid_prime(self.input[i+1])))
        
        self.rss_h.reverse()

    def weight_gradients(self): 
        self.back_prop()

        self.rss_b = []
        self.rss_A = []


        for i in range(3): 
            self.rss_b.append(self.rss_h[2-i] * self.sigmoid_prime(self.input[3-i]))
            self.rss_A.append(self.outer_product(self.rss_b[i], self.h[2-i]))
        
            #print('b',self.rss_b[i])
            #print('a', self.rss_a[i])
            #print()
        return {'rss_A' : self.rss_A, 'rss_b' : self.rss_b}

class GradientDescent: 

    def __init__(self, points, intial_A, intial_b): 
        self.points = points
        self.A = intial_A
        self.b = intial_b
        self.y_values = [point[1] for point in points]
        self.predications = [] 

        self.alpha = np.array([[0.01]])

    def gradient_sums(self): 
        summed_rss_A = []
        summed_rss_b = []


        for i in range(len(self.points)): 

            prop = BackProp(self.A, self.b, self.points[i])
            prop.weight_gradients()
            
            self.predications.append(prop.predication)

            if i == 0: 
                for i in range(len(prop.rss_A)): 
                    summed_rss_A.append(prop.rss_A[i])
                    summed_rss_b.append(prop.rss_b[i])

                continue
        
            for j in range(len(prop.A)): 
                summed_rss_A[j] += prop.rss_A[j]
                summed_rss_b[j] += prop.rss_b[j]
        
        return summed_rss_A, summed_rss_b
    
    def gradient_descent(self):
        weight_A, weight_b = self.gradient_sums()
        weight_A.reverse()
        weight_b.reverse()
        
        updated_A = []
        updated_b = []

        new_weight = np.array([[weight_A[0][i]] for i in range(4)])
        weight_A[0] = new_weight

        for i in range(len(weight_A)):
            updated_b.append(self.b[i] - (self.alpha * weight_b[i]))
            updated_A.append(self.A[i] - self.alpha * weight_A[i])
        
        self.A = updated_A
        self.b = updated_b
    
    def calc_rss(self): 
        rss = sum([(self.predications[i] - self.y_values[i]) ** 2 for i in range(len(self.predications))])
        return rss
    
    def iterations(self, num_interations): 
        self.all_rss = []
        self.all_predictions = []
        for i in range(num_interations):
           
            self.gradient_descent()
            rss = self.calc_rss()

            self.all_rss.append(rss)
            self.all_predictions.append(self.predications)

            #print(rss)
            #print(self.predications)

            #reset predications
            self.predications = []
        

        return self.all_predictions[-1]
    



points = [[0,0], [0.25, 1], [0.5, 0.5], [0.75, 1], [1,0]]
A = [np.array([[5], [-5], [5], [-5]]), np.array([[10,10,0,0], [0,0,10,10]]), np.array([[10,10]])]
B = [np.array([[-0.75], [1.75], [-3.25], [4.25]]), np.array([[-12.5], [-12.5]]), np.array([[-2.5]])]

grad = GradientDescent(points, A, B)
print(grad.iterations(100))



