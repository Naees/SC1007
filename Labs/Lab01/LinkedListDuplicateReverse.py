# Write a function duplicateReverse() that creates a duplicate of a linked
# list with the nodes stored in reverse. The function prototype is given below:
# def duplicateReverse(head, ptrNewHead):
# The function should return 0 if the operation was successful and -1 otherwise.
# newHeadPtr should point to the first node of the reversed duplicate list.
# Sample output:
# Current list: 1 3 5 2 4 6
# Reversed list: 6 4 2 5 3 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data, index):
        new_mode = Node(data)
        
        if self.head is None or index == 0:
            new_mode.next = self.head
            self.head = new_mode
            return True
        
        current = self.head
        count = 0
        
        while current and count < index - 1:
            current = current.next
            count += 1
        
        if not current:
            print("Index out of range")
            return False
        
        new_mode.next = current.next
        current.next = new_mode
        
        return True
    
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
            
            
    def findNode(self, index):
        if self.head is None or index < 0:
            return None
        current = self.head
        while index > 0:
            current = current.next
            if current is None:
                return None
            index -= 1
        return current
    
    def deleteList(self):
        current = self.head
        while current:
            temp = current.next
            current.next = None
            current = temp
        self.head = None
        
    def duplicateReverse(self):
        newReverseLL = LinkedList()
        current = self.head
        while current is not None:
            newReverseLL.insert(current.data, 0)
            current = current.next
        return newReverseLL
        
if __name__ == "__main__":
     # Create main linked list
    linked_list = LinkedList()
    
    print("Enter a list of numbers, terminated by any non-digit character:")
    print("Enter any non-digit character to finish input:")
    try:
        while True:
            item = int(input())
            if linked_list.insert(item, 0):
                print(f"Successfully inserted {item}")
            else:
                print(f"Failed to insert {item}")
    except ValueError:
        pass

    print("\nBefore duplicateReverse() is called:")
    print("The original list:", end=" ")
    linked_list.printList()
    
    # Create reversed duplicate list
    reversed_list = linked_list.duplicateReverse()
    
    print("\nAfter duplicateReverse() was called:")
    print("The original list:", end=" ")
    linked_list.printList()
    print("\nThe duplicated reverse list:", end=" ")
    reversed_list.printList()
    
    # Clean up both lists
    linked_list.deleteList()
    reversed_list.deleteList()