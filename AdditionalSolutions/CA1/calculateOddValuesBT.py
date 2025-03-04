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

def cout_even_node(node):
    # base case
    if node is None:
        return 0    
    
    # run throught the tree
    # I need the values of the left
    leftTotal = cout_even_node(node.left)
    # I need the values of the right substree
    rightTotal = cout_even_node(node.right)
    
    # Now condition to check and count the values
    currentCount = 1 if node.data % 2 == 0 else 0
    
    # return the value
    return currentCount + leftTotal + rightTotal

def cout_even_values_node(node):
    # base case
    if node is None:
        return 0
    
    # traversal/retrieveal of values
    leftValue = cout_even_values_node(node.left)
    rightValue = cout_even_values_node(node.right)
    
    # condition to validate the value
    currentValue = node.data if node.data % 2 == 0 else 0
    
    return currentValue + leftValue + rightValue
    
    # add the value and return the value
    

def cout_odd_nodes(node):
    if not node:
        return 0
    
    left_count = cout_odd_nodes(node.left)
    right_count = cout_odd_nodes(node.right)
    
    count = 1 if node.data % 2 != 0 else 0
    
    return count + right_count + left_count

def cout_odd_value_nodes(node):
    if not node:
        return 0
    
    totalLeft = cout_odd_value_nodes(node.left)
    totalRight = cout_odd_value_nodes(node.right)
    
    current_count = node.data if node.data % 2 != 0 else 0
    
    return current_count + totalLeft + totalRight

if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Calculate total odd of the binary search tree")
   print("3: Calculate total odd value of the binary search tree")
   print("4: Calculate total even of the binary search tree")
   print("5: Calculate total even value of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/3/4/5/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
        # Calculate the number of odd numbers in the tree.
        odd_count = cout_odd_nodes(root)
        print("Number of odd numbers in the binary tree:", odd_count)
       elif choice == 3:
        # Calculate the number of odd numbers in the tree.
        odd_count = cout_odd_value_nodes(root)
        print("Total value of odd numbers in the binary tree:", odd_count)
       elif choice == 4:
        # Calculate the number of odd numbers in the tree.
        odd_count = cout_even_node(root)
        print("Number of even numbers in the binary tree:", odd_count)
       elif choice == 5:
        # Calculate the number of odd numbers in the tree.
        odd_count = cout_even_values_node(root)
        print("Total value of even numbers in the binary tree:", odd_count)
       elif choice == 0:
           break
       else:
           print("Choice unknown")