from hash_node import HashNode

# HashTable class with dynamic resizing
class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity  # Number of buckets
        self.size = 0  # Number of items in the hash table
        self.table = [None] * self.capacity  # Initialize buckets

    def _hash_function(self, key):
        return hash(key) % self.capacity

    def _rehash(self):
        # Save the old table
        old_table = self.table
        # Double the capacity
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0  # Reset size and re-insert items

        for head_node in old_table:
            current = head_node
            while current:
                self.insert(current.key, current.item)
                current = current.next

    def insert(self, key, item):
        # Check load factor and resize if necessary
        load_factor = self.size / self.capacity
        if load_factor > 0.7:
            self._rehash()

        index = self._hash_function(key)
        new_node = HashNode(key, item)
        current = self.table[index]

        if current is None:
            self.table[index] = new_node
            self.size += 1
        else:
            # Collision handling using linked list
            while True:
                if current.key == key:
                    # Update existing item
                    current.item = item
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = new_node
            self.size += 1

    def search(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.item
            current = current.next
        return None

    def delete(self, key):
        index = self._hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    # Remove node at head
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True  # Deletion successful
            prev = current
            current = current.next
        return False  # Key not found