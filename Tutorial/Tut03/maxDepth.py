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

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.data, end=" ")
    inOrderTraversal(node.right)

def maxDepth(node):
    if node is None:
        return -1
    
    leftHeight = maxDepth(node.left)
    rightHeight = maxDepth(node.right)
    
    return 1 + max(leftHeight,rightHeight)

def createTree():
    stk = Stack()
    root = None

    print("Input an integer that you want to add to the binary tree. Any Alpha value will be treated as NULL.")
    try:
        item = input("Enter an integer value for the root: ")
        root = BSTNode(int(item))
        stk.push(root)
    except ValueError:
        return None

    # Use a loop to process nodes in a level-order fashion using the stack.
    while not stk.is_empty():
        temp = stk.pop()
        # Prompt for the left child
        try:
            item = input(f"Enter an integer value for the Left child of {temp.data}: ")
            temp.left = BSTNode(int(item))
            stk.push(temp.left)
        except ValueError:
            temp.left = None

        # Prompt for the right child
        try:
            item = input(f"Enter an integer value for the Right child of {temp.data}: ")
            temp.right = BSTNode(int(item))
            stk.push(temp.right)
        except ValueError:
            temp.right = None

    return root

if __name__ == '__main__':
    root = None

    while True:
        print("\n1: Create a binary tree.")
        print("2: Find the maximum depth of the binary tree.")
        print("0: Quit;")
        choice = input("Please input your choice(1/2/0): ")

        if choice == '1':
            root = createTree()
            if root is None:
                print("No valid root value entered; binary tree is empty.")
            else:
                print("The resulting binary tree is:", end=" ")
                inOrderTraversal(root)
                print()

        elif choice == '2':
            if root is None:
                print("Binary tree is not created yet. Please create the tree first.")
            else:
                depth = maxDepth(root)
                print("Find the maximum depth of the binary tree:", depth)

        elif choice == '0':
            print("Exiting program.")
            break