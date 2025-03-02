class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = 0
    
    def enqueue(self, data):
        new_node = QueueNode(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
    def dequeue(self):
        if self.head is not None:
            node = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return node
        return None

    def is_empty(self):
        return self.head is None
    
    def remove_all(self):
        self.head = None
        self.tail = None
        
def levelOrderTraversal(root):
    if not root:
        return
    
    queue = Queue()
    queue.enqueue(root)
    
    while not queue.is_empty():
        current = queue.dequeue()
        print(current.data, end=" ")
        if current.left:
            queue.enqueue(current.left)
        if current.right:
            queue.enqueue(current.right)
            
if __name__ == "__main__":
    # Creating a sample Binary Tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = BSTNode(20)
    root.left = BSTNode(15)
    root.right = BSTNode(3)
    root.left.left = BSTNode(10)
    root.left.right = BSTNode(18)
    root.right = BSTNode(50)
    root.right.left = BSTNode(25)
    root.right.right = BSTNode(80)

    print("Level-Order Traversal:")
    levelOrderTraversal(root)