# Q2 Implement an open addressing hash table with linear probing to perform
# insertion, deletion, and key searching. The function prototype is given below:
# You need to specify the number of hash slots at the beginning. Each slot has
# two fields, one for key, and the other to indicate whether the key is deleted. If
# a key is deleted, it will be marked as deleted and it can be replaced by other
# keys. The hash function H(k,i) =(H’(k) + i) mod h, where H’(k) = k mod h.

class HashTableNode:
    def __init__(self, key=None):
        self.key = key
        self.deleted = False

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None
        self.count = 0

    def _hash(self, key, i):
        return (key + i) % self.size  # Linear probing function

    def hash_insert(self, key):
        #add your implementations
        
        for i in range(self.size):
            # Compute the index using the hash function with probe i.
            index = self._hash(key, i)

            # if the slot is empty or marked as deleted, we can insert here.
            if self.table[index] is None or self.table[index].deleted:
                # If we are reusing a deleted slot, update it
                self.table[index] = HashTableNode(key)
                self.table[index].deleted = False
                self.count += 1
                return True

            # If the slot is occupied and the key is already present (and not deleted),
            # then this is a duplicated; do not insert.
            if self.table[index].key == key and not self.table[index].deleted:
                return False # duplicate found
            
        # If we exit the loop, it means we've probed all slots and found no available slot.
        # The table is full.
        return False
                

    def hash_delete(self, key):
        #add your implementations
        
        # Try to find the key using linear probing
        for i in range(self.size):
            index = self._hash(key, i)
            
            # If we hit an empty slot, the key is not in the table
            if self.table[index] is None:
                return False
            
            # If the key is found and is not already marked as deleted,
            # mark it as deleted and return True.
            if self.table[index].key == key and not self.table[index].deleted:
                self.table[index].deleted = True
                self.count -= 1
                return True
            
            # Otherwise, key probing (even if the slot is marked as deleted,
            # because the key might be further along in the probe sequence
            
        # If we've probed all slots and didn't find the key, return False.
        return False
            
            

    def hash_search(self, key):
        #add your implementations
        for i in range(self.size):
            index = self._hash(key, i)
            
            # If an empty slot is encounted, the key isn't in the table.
            if self.table[index] is None:
                return False
            
            # If the key is found and is not marked as deleted, return True.
            if self.table[index].key == key and not self.table[index].deleted:
                return True
            
            # Otherwise, keep probing.
        # If we've checked all slots without finding the key, return False.
        return False

    def hash_print(self):
        print("Hash Table:")
        for i, node in enumerate(self.table):
            if node is None:
                print(f"Slot {i}: Empty")
            else:
                status = "Deleted" if node.deleted else "Occupied"
                print(f"Slot {i}: {node.key} ({status})")


# Menu-driven program
if __name__ == "__main__":
    print("============= Hash Table ============")
    print("|1. Create a hash table             |")
    print("|2. Insert a key to the hash table  |")
    print("|3. Search a key in the hash table  |")
    print("|4. Delete a key from the hash table|")
    print("|5. Print the hash table            |")
    print("|6. Quit                            |")
    print("=====================================")

    ht = None

    while True:
        opt = int(input("Enter selection: "))
        if opt == 1:
            size = int(input("Enter number of hash slots: "))
            ht = HashTable(size)
            print(f"HashTable with {size} slots is created.")
        elif opt == 2:
            key = int(input("Enter a key to be inserted: "))
            if ht and ht.hash_insert(key):
                print(f"{key} is inserted.")
            else:
                print(f"{key} is a duplicate or table is full. No key is inserted.")
        elif opt == 3:
            key = int(input("Enter a key for searching in the HashTable: "))
            if ht and ht.hash_search(key):
                print(f"{key} is found.")
            else:
                print(f"{key} is not found.")
        elif opt == 4:
            key = int(input("Enter a key to delete: "))
            if ht and ht.hash_delete(key):
                print(f"{key} is deleted.")
            else:
                print(f"{key} is not found.")
        elif opt == 5:
            if ht:
                ht.hash_print()
            else:
                print("No hash table created yet.")
        elif opt == 6:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")