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
def moveOdditemstoback(head):
    # If the list is empty or has only one node, nothing to do.
    if head is None or head.next is None:
        return head

    # Create a dummy node for the odd list.
    oddLL = Node(0)
    odd_tail = oddLL

    # Traverse the original list.
    current = head
    prev = None
    while current:
        # Check if current node is odd.
        if current.data % 2 != 0:
            # Remove current from the original list.
            if prev:
                prev.next = current.next
            else:
                # current is the head.
                head = current.next

            # Append current to the odd list.
            odd_tail.next = current
            odd_tail = current

            # Advance current.
            temp = current.next  # Save pointer to next node.
            current.next = None  # Detach current from the original list.
            current = temp       # Continue traversal.
        else:
            # Node is even; move forward normally.
            prev = current
            current = current.next

    # At this point, the original list (starting at head) contains only even nodes.
    # If head is None, then all nodes were odd.
    if head is None:
        return oddLL.next

    # Otherwise, find the tail of the even list.
    tail = head
    while tail.next:
        tail = tail.next

    # Append the odd list (which starts at odd_dummy.next) to the end.
    tail.next = oddLL.next

    return head

        
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
   linked_list.head = moveOdditemstoback(linked_list.head)
   print("After:", end=" ")
   linked_list.printList()