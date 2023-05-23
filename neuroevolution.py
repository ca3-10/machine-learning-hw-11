from numpy import random
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
        
        for parent in parents:
            self.incoming_weights.append(parent.children_weights[position])
            sum += (parent.value * parent.children_weights[position])
        
        value = self.tanh(sum)

        return value 

    def tanh(self, x): 
        return  ((math.e ** (x)) - (math.e ** (-x))) / ((math.e ** (x)) + (math.e ** (-x)))
    
class BiasNode: 
    def __init__(self, num_weights): 
        self.value = 1
        self.num_weights = self.generate_children_weights(num_weights)
    
    def generate_children_weights(self, num_weights): 
        self.children_weights = [1 for i in range(num_weights)]

class NeuralNet: 
    def __init__(self, mutation_rate,input_point):
        self.mutation_rate = mutation_rate
        self.input_node = Node(input_point[0])
        self.bias_node = BiasNode(10)
        self.actual_output = input_point[1]
    
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
    
    def build_net(self): 
        self.input_layer = [self.input_node, self.bias_node]

        self.first_hidden_layer = self.build_layer(self.input_layer, 10)      

        self.second_hidden_layer = self.build_layer(self.first_hidden_layer, 6)

        self.third_hidden_layer = self.build_layer(self.second_hidden_layer, 3)

        self.output_layer = self.build_layer(self.third_hidden_layer, 1)
    

        print(self.output_layer[0].value)
            
        
        
        
            

net = NeuralNet(0.05, [0,0])
net.build_net()

