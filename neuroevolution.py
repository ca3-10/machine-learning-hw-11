import random
import math

class Node: 
    def __init__(self, value, parent_nodes): 

        self.parent_nodes = parent_nodes

        if value != 0: 
            self. value = value
        else: 
            self.value = self.calc_value()
        self.weight =  round(random.uniform(-0.2, 0.2), 2)
    
    def calc_value(self): 
        sum = 0
        for parents in self.parent_nodes:
            sum += (parents.value * parents.weight)
        
        value = self.tanh(sum)
        return value 
    
    def tanh(self, x): 
        return  ((math.e ** (x)) - (math.e ** (-x))) / ((math.e ** (x)) + (math.e ** (-x)))

input = Node(1, None)
input_2 = Node(2, None)
print(input.weight)
print(input_2.weight)

hidden = Node(0, [input, input_2])

print(hidden.value)