import random

nums = random.sample(range(1000), 1000)
print(nums)

class Root():
    def __init__(self) -> None:
        self.root = None
        pass

class Node():
    def __init__(self, value = int) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None
        pass

def insert_child(node = Node, value = int):
    if value < node.value():
        if node.left_child is not None:
            insert_child(node.left_child, value)
        else:
            node.left_child = Node(value)
    elif node.right_child is not None:
        insert_child(node.right_child, value)
    else:
        node.right_child = Node(value)

raiz = Root()
raiz.root = Node(20)
insert_child(raiz.root, 30)
insert_child(raiz.root, 10)

print(raiz.root.value)