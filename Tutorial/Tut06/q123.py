class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.first_child = None
        self.next_sibling = None
        self.is_end_of_word = False

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # Add to the end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        return None

    def is_empty(self):
        return len(self.items) == 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _find_child(self, node, char):
        current = node.first_child
        while current:
            if current.char == char:
                return current
            current = current.next_sibling
        return None

    def _add_child(self, node, char):
        new_node = TrieNode(char)
        new_node.next_sibling = node.first_child
        node.first_child = new_node
        return new_node

    def insert(self, word):
        node = self.root
        for char in word:
            child = self._find_child(node, char)
            if not child:
                child = self._add_child(node, char)
            node = child
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            node = self._find_child(node, char)
            if not node:
                return False
        return node.is_end_of_word

    def collect_all_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
            
        child = node.first_child
        while child:
            self.collect_all_words(child, prefix + child.char, results)
            child = child.next_sibling
    
    def find_words_with_prefix(self, prefix): #question 2
        #Traverse the Trie to the node matching the prefix, e.g., “ca”
        #Perform dfs to collect all complete words
        #Put the words in the list: results
        #add your implementations

        results = []
        node = self.root
        
        # 1. Traverse the trie until the last character of *prefix*
        for char in prefix:
            node = self._find_child(node, char)
            if node is None:
                return []
            
        # 2. DFS from that node to collect complete words.
        self.collect_all_words(node, prefix, results)
        return results

    def count_words(self, node): #question 1
        #add you implementations
        if node.is_end_of_word:
            total = 1
        else:
            total = 0
        child = node.first_child
        while child:
            total += self.count_words(child)
            child = child.next_sibling
        return total
        

    def find_shortest_word_with_prefix(self, prefix):#question 3
        # Step 1: Traverse to the end of the prefix

        # Step 2: Perform bfs from the ending node of the prefix
        #The first complete word will be the shortest one
        #add your implementations
        # Put the words in the list: shortest_words

        node = self.root
        for char in prefix:
            node = self._find_child(node, char)
            if not node:
                return None
        queue = Queue()
        queue.enqueue((node, prefix, 0))
        shortest_words = []
        min_depth = None
        
        while not queue.is_empty():
            node, word, depth = queue.dequeue()
            
            if node.is_end_of_word:
                if min_depth is None:
                    min_depth = depth
                if depth == min_depth:
                    shortest_words.append(word)
                elif depth > min_depth:
                    break
            
            if min_depth is not None and depth >= min_depth:
                continue
            
            child = node.first_child
            while child:
                queue.enqueue((child, word + child.char, depth + 1))
                child = child.next_sibling
                
        return shortest_words
        


# Create a new Trie instance
trie = Trie()

# Insert words into the Trie
trie.insert("cat")
trie.insert("car")
trie.insert("care")
trie.insert("camera")
trie.insert("campus")
trie.insert("camp")
trie.insert("dog")
trie.insert("dot")

# 1. Count total words in the Trie
print("Total words in Trie:", trie.count_words(trie.root))  # Output: 8

# 2. Find all words that start with a given prefix
prefix1 = "ca"
print(f"Words starting with '{prefix1}':", trie.find_words_with_prefix(prefix1))
# Output: ['cat', 'car', 'care', 'camera', 'campus', 'camp']

prefix2 = "do"
print(f"Words starting with '{prefix2}':", trie.find_words_with_prefix(prefix2))
# Output: ['dog', 'dot']

prefix3 = "z"
print(f"Words starting with '{prefix3}':", trie.find_words_with_prefix(prefix3))
# Output: []

# 3. Find the shortest word with a given prefix
print(f"Shortest word starting with '{prefix1}':", trie.find_shortest_word_with_prefix(prefix1))
# Output: "car"

print(f"Shortest word starting with '{prefix2}':", trie.find_shortest_word_with_prefix(prefix2))
# Output: "dog"

print(f"Shortest word starting with '{prefix3}':", trie.find_shortest_word_with_prefix(prefix3))
# Output: None
