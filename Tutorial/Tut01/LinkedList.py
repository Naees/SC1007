class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert (self, data, index):
        new_node = Node(data)
        if self.head is None or index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        current = self.head
        count = 0
        
        while current and count < index - 1:
            current = current.next
            count += 1
            
        if not current:
            print("Index out of range")
            return False
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        return True
    
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
            
    def deleteList(self):
        current = self.head
        while current:
            temp = current.next
            current.next = None
            current = temp
        self.head = None
        self.size = 0
        
    def removeNode(self, index):
        # check if index invalid or LL is empty
        if index < 0 or self.head is None:
            return False
        # edge case removal from the start of the list
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        if not current or current.next:
            return 0;
        current.next = current.next.next
        self.size -= 1
        return True
    
    def removeNode2(self, index):
        # check if index invalid or LL is empty
        if self.head is None or index < 0:
            return False
        # edge case: removal from the start of the list
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        count = 0
        prev = None
        
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        if not current or not current.next:
            return False
        prev.next = current.next
        self.size -= 1
        return True
    
def move_even_items_to_back(ll: LinkedList):
    oddDummy = Node(0)
    evenDummy = Node(0)
    evenTail = evenDummy
    oddTail = oddDummy
    
    current = ll.head
    while current:
        # make a copy and detach the current node
        next_node = current.next
        current.next = None
        if current.data % 2 != 0:
            oddTail.next = current
            oddTail = oddTail.next
        else:
            evenTail.next = current
            evenTail = evenTail.next
        current = next_node
    oddTail.next = evenDummy.next
    if oddDummy.next:
        ll.head = oddDummy.next
    else:
        ll.head = evenDummy.next
    # ll.head = oddDummy.next if oddDummy.next else evenDummy.next
    
def move_max_to_front(ll: LinkedList):
    current = ll.head
    previousNodeOfMax = None
    maxNode = ll.head
    previousNode = None
    
    while current:
        if current.data > maxNode.date:
            max_node = current
            previousNodeOfMax = previousNode
        previousNode = current
        current = current.next
        
    if max_node == ll.head:
        return
    
    if previousNodeOfMax is not None:
        previousNodeOfMax.next = max_node.next
        
    max_node.next = ll.head
    ll.head = max_node
    
def removeDuplicatesSortedLL(ll: LinkedList):
    # empty linked list:
    if ll.head is None:
        return False
    
    current = ll.head
    
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
            
if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\n1: Insert an integer to the linked list")
        print("2: Move the node with the largest stored value to the front")
        print("3: Move even-valued items to the back")
        print("4: Remove duplicates (assumes sorted list)")
        print("5: Print the linked list")
        print("0: Quit")
        choice = input("Please input your choice (1/2/3/4/5/0): ")

        if choice == "1":
            try:
                data = int(input("Input an integer to add: "))
                index = int(input("Insert at index (0 for front): "))
                if ll.insert(data, index):
                    print(f"Inserted {data} at index {index}.")
                else:
                    print("Insertion failed.")
                ll.printList()
            except ValueError:
                print("Invalid input. Please enter integers only.")
        
        elif choice == "2":
            move_max_to_front(ll)
            print("Linked List after moving max to front:")
            ll.printList()
        
        elif choice == "3":
            move_even_items_to_back(ll)
            print("Linked List after moving even items to the back:")
            ll.printList()
        
        elif choice == "4":
            removeDuplicatesSortedLL(ll)
            print("Linked List after removing duplicates (sorted only):")
            ll.printList()
        
        elif choice == "5":
            print("Current Linked List:")
            ll.printList()
        
        elif choice == "0":
            print("Exiting...")
            ll.deleteList()
            break
        
        else:
            print("Invalid choice. Please try again.")