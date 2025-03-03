# inorderIterative

# (inorderIterative)Write an iterative Python function inorderIterative() that prints the in-order traversal of a binary search tree using only one temporary stack inside the inorderIterative()function. 
# Note that you should only use push() or pop() operations when you add or remove integers from the stack.

class BSTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class StackNode:
   def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
   def __init__(self):
       self.top = None

def insert(root, data):
   if root is None:
       return BSTNode(data)
   
   if data < root.data:
       root.left = insert(root.left, data)
   else:
       root.right = insert(root.right, data)
       
   return root

def push(stack, node):
   temp = StackNode(node)
   if stack.top is None:
       stack.top = temp
       temp.next = None
   else:
       temp.next = stack.top
       stack.top = temp

def pop(stack):
   if stack.top is not None:
       temp = stack.top
       stack.top = temp.next
       return temp.data
   return None

def is_empty(stack):
   return stack.top is None
def inorderIterative(root):
# Implement the iterative in-order traversal here.
# Use the following statement to print the in-order traversal:
# print(XXXX.data, end=" ") 
# where XXXX represents the appropriate node, e.g., 'current'.
    stk = Stack()
    current = root
    while True:
        while current:
            push(stk,current)
            current = current.left
        if is_empty(stk):
            break
        current = pop(stk)
        print(current.data, end=" ")
        current = current.right

if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Print the in-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("In-order traversal: ", end="")
           inorderIterative(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")