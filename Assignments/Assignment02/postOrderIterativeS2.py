# postOrderIterativeS2

#(postOrderIterativeS2) Write an iterative Python function postOrderIterativeS2() that prints the post-order traversal of a binary search tree using no more and no less than two temporary stacks inside the postOrderIterativeS2()function. Note that you should only use push() or pop() operations when you add or remove integers from the stacks.

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

def postOrderIterativeS2(root):
# Implement the iterative in-order traversal here.
# Use the following statement to print the in-order traversal:
# print(XXXX.data, end=" ") 
# where XXXX represents the appropriate node, e.g., 'current'.
    stk = Stack()
    resultStk = Stack()
    
    if root:
        push(stk, root)
    
    while not is_empty(stk):
        node = pop(stk)
        push(resultStk, node)
        
        if node.left:
            push(stk, node.left)
        if node.right:
            push(stk, node.right)
        
    while not is_empty(resultStk):
        node = pop(resultStk)
        print(node.data, end=" ")

if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Print the post-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("Post-order traversal: ", end="")
           postOrderIterativeS2(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")