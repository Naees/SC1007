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
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def removeNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre.next is not None:
            pre.next = pre.next.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end="  ")
            cur = cur.next
        print("")

class Stack:
    def __init__(self):
        self.ll = LinkedList()
       
    def push(self, data):    
        try:
            self.ll.insertNode(data, 0)
        except ValueError as e:
            print(e)
       
    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        try:
            self.ll.removeNode(0)
        except ValueError as e:
            print(e)
            return None
        return data
       
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data    
       
    def isEmpty(self):
        return self.ll.size == 0
   
    def getSize(self):
        return self.ll.size
       
    def printStack(self):
        self.ll.printList()

def deleteMiddleElement(s):
    temp = []
    n = 0

    # 1. Find size n by popping everything into temp
    while not s.isEmpty():
        temp.append(s.pop())
        n += 1
    
    # Push them back to restore the original stack
    while temp:
        s.push(temp.pop())

    if n <= 1:
        return  # No middle to remove if 0 or 1 item

    # 2. The middle index is n//2 for both odd and even
    mid_index = n // 2  # 'lower' middle for even, exact middle for odd

    # 3. Remove the middle item
    # pop mid_index items into temp
    for _ in range(mid_index):
        temp.append(s.pop())
    
    # pop the middle item from s (discard)
    s.pop()
    
    # push everything from temp back to s
    while temp:
        s.push(temp.pop())
if __name__ == "__main__":
    s = Stack()
   
    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()
   
    counter = 0
    for num in numbers:
        try:
            s.push(int(num))
        except ValueError:
            break
   
    print("\nBefore:", end=" ")
    s.printStack()
   
    deleteMiddleElement(s)
   
    print("After:", end=" ")
    s.printStack()