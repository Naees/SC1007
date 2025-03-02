class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek: Empty Stack")
        return self.top.data
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop: Empty Stack")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data
    
    def is_empty(self):
        return self.top is None
    
    def get_size(self):
        return self.size

def preOrderIterative(root):
    if not root:
        return
    
    stack = Stack()
    stack.push(root)
    
    while not stack.is_empty():
        current = stack.pop()
        print(current.data, end=" ")
        if current.right:
            stack.push(current.right)
        if current.left:
            stack.push(current.left)
            
def preOrderIterativeLecture(node):
    if node:
        print(node.data, end=" ")
        preOrderIterativeLecture(node.left)
        preOrderIterativeLecture(node.right)
        

def insert(data, current_node):
    if current_node is None:
        return Node(data)
    if data < current_node.data:
        if current_node.left is None:
            current_node.left = Node(data)
        else:
            insert(data, current_node.left)
    if data > current_node.data:
        if current_node.right is None:
            current_node.right = Node(data)
        else:
            insert(data, current_node.right)
            
if __name__ == "__main__":
    
    # Creating a sample Binary Tree:
    #        20
    #       / \
    #    15     50
    #   / \     / \
    #10   18   25  80

    root = BSTNode(20)
    root.left = BSTNode(15)
    root.right = BSTNode(3)
    root.left.left = BSTNode(10)
    root.left.right = BSTNode(18)
    root.right = BSTNode(50)
    root.right.left = BSTNode(25)
    root.right.right = BSTNode(80)

    print("Pre-Order Traversal:")
    preOrderIterative(root)
    print("Pre-Order Traversal with Lecture method:")
    preOrderIterative(root)