import random

nums = random.sample(range(1000), 100)
print(nums)

class node():
    def __init__(self) -> None:
        self.value = None
        self.left_child = None
        self.right_child = None
    
    def set_value(self, value = int):
        self.value = value
    
    def create_child(self, value = int):
        if value < self.value:
            if self.left_child != None:
                self.left_child.create_child(value)
            else:
                self.left_child = node().set_value(value)
        elif self.right_child != None:
            self.right_child.create_child(value)
        else:
            self.right_child = node().set_value(value)

def order_by_binary_tree(nums = list):
    tree = node()
    [tree.create_child(num) if tree.value != None else tree.set_value(num) for num in nums]
    return tree

def inorden(tree = node):
    if(tree.value != None):
        if(tree.left_child != None):
            inorden(tree.left_child)
        else:
            print(f"{tree.value} ")
            inorden(tree.right_child)

tree = order_by_binary_tree(nums)
inorden(tree)