import random
class Stack:
    def __init__(self):
        self.elements = []

    def print(self):
        print(self.elements)

    def push(self, value):
        self.elements.append(value)

    def pop(self):
        self.elements.pop()

class Node: 
    def __init__(self, data_points): 
        self.data_points = data_points
        self.num_data_points = len(data_points)

        self.shortbread_counts = self.get_shortbread_counts(self.data_points)
        self.sugar_counts = self.num_data_points - self.shortbread_counts

        self.prediction = 'Sugar' 
        if self.shortbread_counts > self.sugar_counts:
            self.prediction = 'Shortbread'

        self.children = []
        self.parent = None

        self.path = []
        self.depth = 1

        self.pure = False
        if self.shortbread_counts == self.num_data_points or self.sugar_counts == self.num_data_points:
            self.pure = True
            return
        
        self.g_before = self.gini_impurity_before()

        self.best_split = self.best_split()

        #left = points less than equal to the best split
        self.left_data = self.point_counts(self.best_split[1], self.best_split[0], '<=')

        #right = points greater than the best split
        self.right_data = self.point_counts(self.best_split[1], self.best_split[0], '>')

    def get_shortbread_counts(self, array):
        shortbread_counts = 0
        for data_point in array: 
            if data_point[0] == 'Shortbread':
                shortbread_counts += 1
        return shortbread_counts
    
    def gini_impurity(self, p):
        return 2 * p * (1 - p)
    
    def gini_impurity_before(self): 
        return self.gini_impurity(self.shortbread_counts/self.num_data_points)
    
    def splits(self, array):
        splits = []
        for i in range(len(array)-1):
            splits.append((array[i] + array[i+1])/2)
        return splits
    
    def point_counts(self,point_value, point_classification, point_inequality): 

        if point_classification == 'x':
            if point_inequality == '<=':
                x_less_than_equal_points = [data_point for data_point in self.data_points if data_point[1] <= point_value]
                return x_less_than_equal_points
            
            else:
                x_greater_than_points = [data_point for data_point in self.data_points if data_point[1] > point_value]
                return x_greater_than_points

        else: 
            if point_inequality == '<=':
                y_less_than_equal_points = [data_point for data_point in self.data_points if data_point[2] <= point_value]
                return y_less_than_equal_points
            
            else:
                y_greater_than = [data_point for data_point in self.data_points if data_point[2] > point_value]
                return y_greater_than

    def best_split(self):

        x_splits = self.splits(sorted((list(dict.fromkeys([data_point[1] for data_point in self.data_points])))))
        y_splits = self.splits(sorted((list(dict.fromkeys([data_point[2] for data_point in self.data_points])))))

        x_impurities = {}
        y_impurities = {}

        for x in x_splits: 
            if len(x_splits) == 0: 
                break
            points_less_than_equal = self.point_counts(x, 'x', '<=')
            points_greater_than = self.point_counts(x, 'x', '>')

            p_less_than_equal = len(points_less_than_equal)/self.num_data_points
            p_greater_than = len(points_greater_than)/self.num_data_points

            g_less_than_equal = self.gini_impurity(self.get_shortbread_counts(points_less_than_equal)/len(points_less_than_equal))
            g_greater_than = self.gini_impurity(self.get_shortbread_counts(points_greater_than)/len(points_greater_than))


            g_after = p_less_than_equal * g_less_than_equal + p_greater_than * g_greater_than

            x_impurities[x] = self.g_before - g_after
            
        for y in y_splits: 
            if len(y_splits) == 0: 
                break
            points_less_than_equal = self.point_counts(y, 'y', '<=')
            points_greater_than = self.point_counts(y, 'y', '>')

            p_less_than_equal = len(points_less_than_equal)/self.num_data_points
            p_greater_than = len(points_greater_than)/self.num_data_points

            g_less_than_equal = self.gini_impurity(self.get_shortbread_counts(points_less_than_equal)/len(points_less_than_equal))
            g_greater_than = self.gini_impurity(self.get_shortbread_counts(points_greater_than)/len(points_greater_than))


            g_after = p_less_than_equal * g_less_than_equal + p_greater_than * g_greater_than

            y_impurities[y] = self.g_before - g_after


        if len(x_splits) == 0:
            best_y_split = max(y_impurities, key=y_impurities.get)
            return ('y', best_y_split)
        elif len(y_splits) == 0:
            best_x_split = max(x_impurities, key=x_impurities.get)
            return ('x', best_x_split)
        else: 
            best_x_split = max(x_impurities, key=x_impurities.get)
            best_y_split = max(y_impurities, key=y_impurities.get)
            
            if x_impurities[best_x_split] > y_impurities[best_y_split]:
                return ('x', best_x_split)
            else:
                return ('y', best_y_split)
                    
class DecisionTree:
    def __init__(self, data_points, max_depth, min_split_size):
        self.max_depth = max_depth
        self.min_split_size = min_split_size
        self.data_points = data_points
        self.root = Node(data_points)

        self.nodes = self.build_tree()
           
    def build_tree(self):
        stack = Stack()
        stack.push(self.root)
        nodes = {self.root: []}

        if self.root.pure == True:
            return nodes

        if self.max_depth == 1: 
            return nodes
    
        while len(stack.elements) != 0:
 
            current_node = stack.elements[-1]
            if current_node.pure == True: 
                continue
            if current_node.depth == self.max_depth:
                continue
            if len(current_node.data_points) <= self.min_split_size:
                stack.pop()
                continue

            stack.pop()

            #path
            left_node = Node(current_node.left_data)
            left_node.path = current_node.path.copy()
            left_node.path.append([current_node.best_split[0],'<=',current_node.best_split[1]])
            nodes[left_node] = left_node.path

            #depth
            left_node.depth = current_node.depth + 1

            #path
            right_node = Node(current_node.right_data)
            right_node.path = current_node.path.copy()
            right_node.path.append([current_node.best_split[0],'>',current_node.best_split[1]])
            nodes[right_node] = right_node.path

            #depth
            right_node.depth = current_node.depth + 1

            children = [left_node, right_node]

            for child in children: 
                current_node.children.append(child)
                child.parent = current_node

                if child.pure == True: 
                    continue
                if child.depth == self.max_depth:
                    continue
                if len(current_node.data_points) <= self.min_split_size:
                    continue
                stack.push(child)
            
        return nodes
    
    def predict(self, point):
        x= point[0]
        y = point[1]
        current_node = self.root
        while True:
            
            if current_node.pure == True:
                return current_node.prediction
            if current_node.children == []:
                return current_node.prediction

            if type(current_node.best_split) == tuple:
                
                if current_node.best_split[0] == 'x':
                    if current_node.best_split[1] >= x:
                        current_node = current_node.children[0]
                    elif current_node.best_split[1] < x:
                        current_node = current_node.children[1]
                    else:
                        return current_node.prediction

                elif current_node.best_split[0] == 'y':
                    if current_node.best_split[1] >= y:
                        current_node = current_node.children[0]
                    elif current_node.best_split[1] < y:
                        current_node = current_node.children[1]
                    else:
                        return current_node.prediction
                else:
                    return current_node.prediction

