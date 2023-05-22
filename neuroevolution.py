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
    def __init__(self): 
        self.value = 1
    
    def generate_children_weights(self, num_weights): 
        self.children_weights = [1 for i in range(num_weights)]

class NeuralNet: 
    def __init__(self, mutation_rate,input_point):
        self.mutation_rate = mutation_rate
        self.input_node = Node(input_point[0])
        self.bias_node = BiasNode(10)
        self.actual_output = input_point[1]
    
    def build_layer(self, incoming_layer, next_layer_num): 

        for nodes in incoming_layer: 
            nodes.generate_children_weights(next_layer_num)
        
        next_layer = [Node(0) for i in range(next_layer_num)]

        for i in range(len(next_layer)): 
            current_node = next_layer[i]
            current_node.value = current_node.calc_value(incoming_layer, i)
        
        

        
    
    def build_net(self): 
        self.input_layer = [self.input_node, self.bias_node]

        for nodes in self.input_layer: 
            self.input_node.generate_children_weights(10)

        self.first_hidden_layer = [Node(0) for i in range(10)]        

        for i in range(len(self.first_hidden_layer)): 
            current_node = self.first_hidden_layer[i]
            current_node.value = current_node.calc_value(self.input_layer, i)
            current_node.generate_children_weights(6)
        
        self.first_hidden_layer.append(BiasNode(6))
        self.second_hidden_layer = [Node(0) for i in range(6)]

        for i in range(len(self.second_hidden_layer)): 
            current_node = self.second_hidden_layer[i]
            current_node.value = current_node.calc_value(self.first_hidden_layer,i)
            current_node.generate_children_weights(3)
        
        self.second_hidden_layer.append(BiasNode(3))
        self.third_hidden_layer = [Node(0) for i in range(3)]

        for i in range(len(self.third_hidden_layer)): 
            current_node = self.third_hidden_layer[i]
            current_node.value = current_node.calc_value(self.second_hidden_layer, i)
            current_node.generate_children_weights(1)
        
        self.third_hidden_layer.append(BiasNode(1))
        self.output_layer = [Node(0)]

        for i in range(len(self.output_layer)): 
            current_node = self.output_layer[i]
            current_node.value = current_node.calc_value(self.third_hidden_layer, i)
        
        print(current_node.value)
            
        
        
        
            

net = NeuralNet(0.05, [0,0])
net.build_net()

