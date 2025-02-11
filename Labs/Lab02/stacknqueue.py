class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    #Insert function
    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
            return -1
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
            prev = self.findNode(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
        return 0
    
    # Remove function
    def remove_node(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
            return -1
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
                # Don't need to remove self.head as self.head.next will nullify if the next is None
        else:
            prev = self.findNode(index - 1)
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
        return 0
    
    def append(self, data):
        self.insert(self.size, data)
        
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        
class Stack:
    def __init__(self):
        self.ll = LinkedList()
        
    def push(self, data):
        self.ll.insert(0, data)
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data
    
    def pop(self):
        if self.isEmpty():
            return None
        item = self.ll.head.data
        self.ll.remove_node(0)
        return item
    
    def isEmpty(self):
        return self.ll.size == 0
    
    def size(self):
        return self.ll.size
    
class Queue:
    def __init__(self):
        self.ll = LinkedList()
        
    def isEmpty(self):
        return self.ll.size == 0
    
    def getFront(self):
        if self.isEmpty():
            return None
        return self.ll.head.data
    
    def enqueue(self, data):
        self.ll.insert(self.ll.size, data)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("\nThe queue is empty")
            return None
        item = self.ll.head.data
        self.ll.remove_node(0)
        return item
    
    def get_size(self):
        return self.ll.size
    
    
# 1. Write a function removeUntil() that removes all values from a stack of integers until but
# not including the first occurrence of a given value. The function accepts two parameters: a
# reference to the stack and the value to stop at. The function definition is as follows:
# def removeUntil(stack, value):
# Given a stack [1 2 3 4 5 6 5 4 3 2 1] with the topmost number displayed on the left, calling
# removeUntil() with value = 5 will produce the stack [5 6 5 4 3 2 1]

def removeUntil(stack, value):
    while not stack.isEmpty() and stack.peek() != value:
        stack.pop()
        
# 2. Write a recursive function recursiveReverse() that reverses the order of items stored in a
# queue of integers. The function accepts a single parameter: a reference to the queue. The function
# definition is as follows:
# def recursiveReverse(queue):

def recursiveReverse(queue):
    if queue.isEmpty():
        return
    firstItem = queue.dequeue()
    recursiveReverse(queue)
    queue.enqueue(firstItem)

# 3. Write a function palindrome() that determines whether a given string is a palindrome. The
# function accepts a single parameter: the word (a string). The function should return 0 if the string
# is a palindrome and -1 otherwise. The function should ignore whitespace, case, and punctuation.
# The function definition is as follows:
# def palindrome(word):

# C style
def palindrome(word):
    cleaned = ""
    rev = ""
    for i in range(0, len(word)):
        ch = word[i]
        if ch.isalnum():
            cleaned += ch.lower()
            
    for i in range(len(cleaned) -1, -1, -1):
        rev += cleaned[i]
        
    if cleaned == rev: #cleaned == cleaned[::-1]
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
        
def palindromeVersion2(word):
    cleaned = ''.join(ch.lower() for ch in word if ch.isalnum())
    if cleaned == cleaned[::-1]:
        print("The string is a palindrome.")
        return 0
    else:
        print("The string is not a palindrome.")
        return -1
        
# 4. Write a function balanced() that determines if an expression comprised of the characters
# ()[]{} is balanced. The function accepts a single parameter: the expression (a string). The function
# should return 0 if the expression is balanced and -1 otherwise. The function definition is as
# follows:
# def balanced(expression)

def balanced(expression):
    stack = Stack()
    matchingDict = {')':'(', ']':'[', '}':'{'}
    
    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.isEmpty():
                return -1
            else:
                if stack.pop() != matchingDict[ch]:
                    return -1
    if stack.isEmpty():
        print("The expression is balanced.")
        return 0
    else:
        print("The expression is not balanced.")
        return -1
    
# ---------------------------
# Main Function to Test Everything
# ---------------------------
def main():
    # Test 1: removeUntil() for Stack
    print("Test removeUntil():")
    s = Stack()
    # Push sample values: [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    for v in [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]:
        s.push(v)
    print("Stack before removeUntil(5):", s)
    removeUntil(s, 5)
    print("Stack after removeUntil(5):", s)
    print()

    # Test 2: recursiveReverse() for Queue
    print("Test recursiveReverse():")
    q = Queue()
    for i in range(1, 7):
        q.enqueue(i)
    print("Queue before recursiveReverse:", q)
    recursiveReverse(q)
    print("Queue after recursiveReverse:", q)
    print()

    # Test 3: palindrome() and palindromeVersion2()
    test_str = "A man a plan a canal Panama"
    print("Test palindrome() on:", test_str)
    res1 = palindrome(test_str)
    res2 = palindromeVersion2(test_str)
    print("palindrome() returned:", res1)
    print("palindromeVersion2() returned:", res2)
    if res1 == 0:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    print()

    # Test 4: balanced() for Expressions
    expressions = ["()", "([])", "{[]()[]}", "{{)]", "[({{)])"]
    print("Test balanced() on various expressions:")
    for expr in expressions:
        res = balanced(expr)
        if res == 0:
            print(f"Expression {expr} is balanced.")
        else:
            print(f"Expression {expr} is not balanced.")

if __name__ == "__main__":
    main()