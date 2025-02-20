'''2. (reverseFirstKItems) Write a Python function reverse_first_k_items() that reverses
the order of the first k elements of a queue using a stack, leaving the other elements in the
same relative order for a given integer k and a queue of integers. Note that the
reverse_first_k_items() function only uses push() and pop() when adding or
removing integers from the stack, and only uses enqueue() and dequeue() when adding
or removing integers from the queue.'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def findNode(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if self.head is None:
            raise ValueError("List is empty")
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def insert_node(self, index,data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.findNode(index-1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
        return 0
    
    def remove_node(self, index):
        '''if index < 0 or index >= self.size:
            raise IndexError("Index out of range")'''
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        pre = self.findNode(index-1)
        if pre is not None and pre.next is not None:
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
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")
        
class Stack:
    def __init__(self):
        self.ll = LinkedList()
        
    def push(self, data):
        self.ll.insert_node(0, data)
    
    def pop(self):
        if self.isEmpty():
            return None
        topData = self.ll.head.data
        self.ll.remove_node(0)
        return topData
    
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
        
class Queue:
    def __init__(self):
        self.ll = LinkedList()
        
    def enqueue(self, data):
        self.ll.insert_node(self.ll.size, data)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from an empty queue")
        data = self.ll.head.data
        self.ll.remove_node(0)
        return data
    
    def isEmpty(self):
        return self.ll.size == 0
    
    def getSize(self):
        return self.ll.size
    
    def printQueue(self):
        self.ll.printList()
        
def reverse_first_k_items(queue, k):
    if queue.isEmpty() or k <= 0:
        return
    n = queue.getSize()
    if k > n:
        k = n
        
    tempStack = Stack()
    
    for _ in range(k):
        tempStack.push(queue.dequeue())
    
    while not tempStack.isEmpty():
        queue.enqueue(tempStack.pop())
    
    for _ in range(n - k):
        queue.enqueue(queue.dequeue())
        
def main():
    q = Queue()
    while True:
        print("\n1: Insert an integer into the queue;")
        print("2: Reverse the elements of the queue until the given number;")
        print("0: Quit;")
        choice = input("Please input your choice(1/2/0): ").strip()
        if choice == "0":
            print("Exiting...")
            break
        elif choice == "1":
            num = input("Input an integer that you want to insert into the queue: ").strip()
            try:
                q.enqueue(int(num))
            except ValueError:
                print("Invalid input, please enter an integer.")
                continue
            print("The resulting queue is:", end=" ")
            q.printQueue()
        elif choice == "2":
            k_str = input("Enter an integer to reverse the queue until that number: ").strip()
            try:
                k = int(k_str)
            except ValueError:
                print("Invalid input, please enter an integer.")
                continue
            reverse_first_k_items(q, k)
            print("The resulting queue after reversing first {} elements is:".format(k), end=" ")
            q.printQueue()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
