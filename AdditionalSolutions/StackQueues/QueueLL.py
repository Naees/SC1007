class ListNode:
   def __init__(self, data):    
       self.data = data        
       self.next = None

class LinkedList:
   def __init__(self):
       self.size = 0
       self.head = None
       self.tail = None

   def find_node(self, index):
       if index < 0 or index >= self.size:
           return None
       temp = self.head
       for _ in range(index):
           temp = temp.next
       return temp

   def remove_node(self, index):
       if index < 0 or index >= self.size:
           return -1
       if index == 0:
           self.head = self.head.next
           if self.size == 1:
               self.tail = None
       else:
           prev = self.find_node(index - 1)
           prev.next = prev.next.next
           if index == self.size - 1:
               self.tail = prev
       self.size -= 1
       return 0
   
   def insert_node(self, index, value):
       if index < 0 or index > self.size:
           return -1
       new_node = ListNode(value)
       if index == 0:
           new_node.next = self.head
           self.head = new_node
           if self.size == 0:
               self.tail = new_node
       elif index == self.size:
           self.tail.next = new_node
           self.tail = new_node
       else:
           prev = self.find_node(index - 1)
           new_node.next = prev.next
           prev.next = new_node
       self.size += 1
       return 0
   
class Queue:
   def __init__(self):
       self.ll = LinkedList()

   def enqueue(self, data):    
       self.ll.insert_node(self.ll.size, data)

   def dequeue(self):
       if self.isEmpty():
           return None
       data = self.ll.head.data    
       self.ll.remove_node(0)
       return data

   def getFront(self):
       if self.isEmpty():
           raise IndexError("Peek from empty queue")
       return self.ll.head.data    

   def getSize(self):           
       return self.ll.size

   def isEmpty(self):
       return self.ll.size == 0
if __name__ == "__main__":
   
   queue = Queue()

   queue.enqueue(10)
   queue.enqueue(20)
   queue.enqueue(30)
 

   print("Front element before dequeue:", queue.getFront())

   print("Size before dequeue:", queue.getSize())

   print("Dequeued element:", queue.dequeue())

   print("Front element after dequeue:", queue.getFront())

   print("Size after dequeue:", queue.getSize())