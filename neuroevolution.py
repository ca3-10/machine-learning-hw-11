import numpy as np
from numpy import random
from copy import deepcopy
import random
import math

class Node: 
    def __init__(self, value): 
        self.value = value
    
    def generate_children_weights(self, num_weights): 

        self.children_weights = [round(random.uniform(-0.2, 0.2), 2) for i in range(num_weights)]
    
    def calc_value(self, parents, position):

        sum = 0
        self.parents = parents
        self.incoming_weights = []
        self.position = position
        
        for parent in parents:
            sum += (parent.value * parent.children_weights[position])

        value = self.tanh(sum)

        return value 
    
    def recalc_value(self, parents, position, alpha):
        sum = 0
        for parent in parents:
            weight = parent.children_weights[position] + (alpha * np.random.normal(0,1,1)[0])
            sum += (parent.value * weight)

        value = self.tanh(sum)

        return value 
    
    def update_children_weights(self, alpha): 
        updated_weights = []
    
        for weights in self.children_weights: 
            if weights == 1: 
                updated_weights.append(weights)
                continue
            updated_weights.append(weights + (alpha * np.random.normal(0,1,1)[0]))

        self.children_weights = updated_weights

    def tanh(self, x): 
        return  ((math.e ** (x)) - (math.e ** (-x))) / ((math.e ** (x)) + (math.e ** (-x)))
    
class BiasNode: 
    def __init__(self, num_weights): 
        self.value = 1
        self.num_weights = self.generate_children_weights(num_weights)
        self.incoming_weights = None
    
    def generate_children_weights(self, num_weights): 
        self.children_weights = [1 for i in range(num_weights)]
    
    def update_children_weights(self, mutation_rate): 
        return 

    def recalc_value(self, a, b, c): 
        return 1

class NeuralNet: 
    def __init__(self, mutation_rate,input_point):
        self.mutation_rate = mutation_rate
        self.input_node = Node(input_point[0])
        self.bias_node = BiasNode(10)
        self.total_num_weights = (2 * 10) +  (11 * 6) + (7 * 3) + (4 * 3)

        self.child_mutation_rate = self.mutation_rate * (math.e ** (np.random.normal(0,1,1)[0]/ math.sqrt(2 * math.sqrt(self.total_num_weights)))) 
    
    def build_layer(self, incoming_layer, next_layer_num):
        
        #create the layer 
        next_layer = [Node(0) for i in range(next_layer_num)]

        #generate parent weights
        for nodes in incoming_layer: 
            nodes.generate_children_weights(next_layer_num)
        
        #calculate values
        for i in range(len(next_layer)): 
            current_node = next_layer[i]
            current_node.value = current_node.calc_value(incoming_layer, i)
            current_node.generate_children_weights(next_layer_num)
        
        #add bias node
        if next_layer_num != 1:
            next_layer.append(BiasNode(next_layer_num))

        return next_layer
    
    def update_layer(self, incoming_layer, layer):
        
        for i in range(len(layer)): 
            current_node = layer[i]
            current_node.value = current_node.recalc_value(incoming_layer, i, self.child_mutation_rate)

        return layer

    def build_net(self): 
        self.input_layer = [self.input_node, self.bias_node]

        self.first_hidden_layer = self.build_layer(self.input_layer, 10)      

        self.second_hidden_layer = self.build_layer(self.first_hidden_layer, 6)

        self.third_hidden_layer = self.build_layer(self.second_hidden_layer, 3)

        self.output_layer = self.build_layer(self.third_hidden_layer, 1)

        self.layers = [self.input_layer, self.first_hidden_layer, self.second_hidden_layer, self.third_hidden_layer, self.output_layer]

        return self.output_layer[0].value
    
    def update_net(self): 
        self.update_layer(self.input_layer, self.first_hidden_layer)
        self.update_layer(self.first_hidden_layer, self.second_hidden_layer)
        self.update_layer(self.second_hidden_layer, self.third_hidden_layer)
        self.update_layer(self.third_hidden_layer, self.output_layer)

        return self.output_layer[0].value





net = NeuralNet(0.05, [0,0])
print(net.build_net())
#print(net.parent_value)
print(net.update_net())
#print(net.child_value)