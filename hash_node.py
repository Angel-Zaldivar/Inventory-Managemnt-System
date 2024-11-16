# HashNode class for linked list nodes in the hash table
class HashNode:
    def __init__(self, key, item):
        self.key = key  # Key is the item name
        self.item = item  # The Item object
        self.next = None  # Pointer to the next node (for collision handling)
        