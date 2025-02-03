# Write a function removeNode() that accepts a reference to the head of a linked list
# (ptrHead) and an integer index. The function should remove the node at the specified
# index and return 1 if the deletion is successful, and 0 otherwise. You should ensure the
# correct handling of the head pointer when deleting the first node.
# The function definition is as follows:
# def removeNode(ptrHead, index):

class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
    
class LinkedList:
    def __init__(self):
        self.head = None;
    
    # Create a new node with the given data
    def insert(self, data, index):
        new_node = Node(data)
        
        # If list is empty or inserting at head
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            return True
        
        current = self.head
        count = 0
        
        while current and count < index - 1:
            current = current.next
            count+= 1
            
        if not current:
            print("Invalid out of range")
            return 0
        
        new_node.next = current.next
        current.next = new_node
        return True
    
    def removeNode(self, index):
        # (edgecase) check to see if the index is a valid number or if the linked list is empty
        if index < 0 or self.head is None:
            return 0;
        
        # (edgecase) check case 0
        if index == 0:
            self.head = self.head.next
            return 1;
        
        current = self.head
        count = 0
        # prev = None
        
        
        while current and count < index -1:
            prev = current
            current = current.next
            count += 1
            
        if not current or not current.next:
            return 0
        
        current.next = current.next.next
        return 1
        
    def printList(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print()
        
# Test the implementation
if __name__ == "__main__":
    linked_list = LinkedList()
    size = 0
    
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    while True:
        try:
            item = int(input())
            if linked_list.insert(item, size) == 1:
                size += 1
                print("Node successfully inserted")
            else:
                print("Insertion failed")
            print("Current list:", end=" ")
            linked_list.printList()
        except ValueError:
            break
    
    while True:
        try:
            index = int(input("Enter the index of the node to be removed:"))
            print()
            if linked_list.removeNode(index) == 1:
                size -= 1
                print("Node successfully removed")
            else:
                print("Removal Failed")
            print("After the removal operation:")
            linked_list.printList()
        except ValueError:
            break
    print("Final List:", end=" ")
    linked_list.printList()