class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
   def __init__(self):
       self.head = None
       self.size = 0  
      
   def findNode(self, index):
       if index < 0 or index >= self.size:
           raise ValueError("Invalid position")
       if self.head is None:
           raise ValueError("List is empty")
          
       cur = self.head
       while index > 0:
           cur = cur.next
           index -= 1
       return cur
  
   def insertNode(self, data, index):
       if index < 0 or index > self.size:
           raise ValueError("Invalid position")
          
       new_node = Node(data)
      
       if index == 0:
           new_node.next = self.head
           self.head = new_node
           self.size += 1
           return True
      
       prev_node = self.findNode(index - 1)
       if prev_node is not None:
           new_node.next = prev_node.next
           prev_node.next = new_node
           self.size += 1
           return True
       return False

   def removeNode(self, index):
       if index < 0 or index >= self.size:
           raise ValueError("Invalid position")
          
       if self.head is None:
           return False
          
       if index == 0:
           cur = self.head
           self.head = cur.next
           self.size -= 1
           return True
          
       pre = self.findNode(index - 1)
       if pre is not None and pre.next is not None:
           cur = pre.next
           pre.next = cur.next
           self.size -= 1
           return True
       return False

   def printList(self):
       cur = self.head
       if cur is None:
           print("Empty")
           return
       while cur is not None:
           print(cur.data, end=" -> ")
           cur = cur.next
       print("None")
       
def sortSublist(head, start, end):
    if head is None:
        return None
    current = head
    sublist = Node(0)
    subTail = sublist
    for _ in range(start):
        prev = current
        current = current.next
    prev.next = None
    subHead = current
    subTail.next = current
    for _ in range(end - start):
        prev = current
        current = current.next
    
    endlist = Node(0)
    endlist.next = current.next
    prev.next = None
    
    # Sort the subhead
    for _ in range(end - start):
        current = subHead
        while current and current.next:
            if current.data > current.next.data:
                subHead = current.next.next
                temp = current.next.next
                current.next.next = current
                current.next = temp
            current = current.next
    
    current = head
    
    while current:
        current = current.next
        
    current.next = subHead
    while current:
        current = current.next
        
    if endlist.next:
        current.next = endlist.next
    # Join the list together
    
    
    
    
    
    
    
        
if __name__ == "__main__":
   linked_list = LinkedList()
  
   print("Enter a list of numbers, terminated by any non-digit character: ", end="")
   input_string = input()
   numbers = input_string.split()
  
   counter = 0
   for num in numbers:
       try:
           linked_list.insertNode(int(num), counter)
           counter += 1
       except ValueError:
           break
  
   print("\nBefore:", end=" ")
   linked_list.printList()
   linked_list.head = sortSublist(linked_list.head, 2, 4)
   print("After:", end=" ")
   linked_list.printList()