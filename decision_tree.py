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

        self.pure = False
        if self.shortbread_counts == self.num_data_points or self.sugar_counts == self.num_data_points:
            self.pure = True
            return
        
        self.g_before = self.gini_impurity_before()

        self.best_split = self.best_split()

        #left = points greater than equal to the best split
        self.left_data = self.point_counts(self.best_split[1], self.best_split[0], '<=')

        #right = points less than the best split
        self.right_data = self.point_counts(self.best_split[1], self.best_split[0], '>')

        self.children = []
        self.parent = None
    
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
    def __init__(self, data_points):
        self.data_points = data_points
        self.root = Node(data_points)
        
    
    def build_tree(self):
        stack = Stack()
        stack.push(self.root)
        node_splits = {}
        while len(stack.elements) != 0:
            current_node = stack.elements[-1]
            if current_node.pure == True: 
                continue
            node_splits[current_node] = current_node.best_split
            stack.pop()

            children = [Node(current_node.left_data), Node(current_node.right_data)]

            for child in children: 
                current_node.children.append(child)
                child.parent = current_node
                if child.pure == True: 
                    continue
                stack.push(child)
        return node_splits

data = [['Shortbread',0.15,0.2],
        ['Shortbread',0.15,0.3],
        ['Shortbread',0.2,0.25],
        ['Shortbread',0.25,0.4],
        ['Shortbread',0.3,0.35],
        ['Sugar',0.05,0.25],
        ['Sugar',0.05,0.35],
        ['Sugar',0.1,0.3],
        ['Sugar',0.15,0.4],
        ['Sugar',0.25,0.35]]

node = Node(data)
tree = DecisionTree(data)
p= tree.build_tree()