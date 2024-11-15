# Item class to represent each inventory item
class Item:
    def __init__(self, name, quantity, general_location, specific_location, category):
        self.name = name
        self.quantity = quantity
        self.general_location = general_location
        self.specific_location = specific_location
        self.category = category


# HashNode class for linked list nodes in the hash table
class HashNode:
    def __init__(self, key, item):
        self.key = key  # Key is the item name
        self.item = item  # The Item object
        self.next = None  # Pointer to the next node (for collision handling)


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


# Global data structures
categories = []  # List of category names
category_items = {}  # Dictionary mapping category names to lists of Item objects
hash_table = HashTable()  # Initialize hash table


# Function to add an item to the inventory
def add_item(name, quantity, general_location, specific_location, category):
    # Check if item already exists
    existing_item = hash_table.search(name)
    if existing_item:
        print(f"Item '{name}' already exists.")
        return

    # Create new item
    item = Item(name, quantity, general_location, specific_location, category)

    # Add category if it doesn't exist
    if category not in categories:
        categories.append(category)
        category_items[category] = []

    # Add item to category
    category_items[category].append(item)

    # Add item to hash table
    hash_table.insert(name, item)
    print(f"Item '{name}' added successfully.")


# Function to delete an item from the inventory
def delete_item(name):
    # Search for the item in hash table
    item = hash_table.search(name)
    if item:
        # Remove item from category
        category_items[item.category].remove(item)

        # Remove category if empty
        if not category_items[item.category]:
            categories.remove(item.category)
            del category_items[item.category]

        # Remove item from hash table
        hash_table.delete(name)
        print(f"Item '{name}' deleted successfully.")
        return True
    else:
        print(f"Item '{name}' not found.")
        return False


# Function to search for an item by name
def search_item(name):
    item = hash_table.search(name)
    if item:
        print(f"Item found:")
        print(f"Name: {item.name}")
        print(f"Quantity: {item.quantity}")
        print(f"General Location: {item.general_location}")
        print(f"Specific Location: {item.specific_location}")
        print(f"Category: {item.category}")
    else:
        print(f"Item '{name}' not found.")


# Function to find the location of an item
def find_item_location(name):
    item = hash_table.search(name)
    if item:
        print(f"Item '{name}' is located at:")
        print(f"General Location: {item.general_location}")
        print(f"Specific Location: {item.specific_location}")
    else:
        print(f"Item '{name}' not found.")


# Function to view all items in a category
def view_items_by_category(category):
    if category in categories:
        items_list = category_items[category]
        if items_list:
            print(f"Items in category '{category}':")
            for item in items_list:
                print(f"- Name: {item.name}, Quantity: {item.quantity}, General Location: {item.general_location}, Specific Location: {item.specific_location}")
        else:
            print(f"No items found in category '{category}'.")
    else:
        print(f"Category '{category}' does not exist.")


# Function to view all items in a general location
def view_items_by_location(general_location):
    matching_items = []
    for items_list in category_items.values():
        for item in items_list:
            if item.general_location == general_location:
                matching_items.append(item)
    if matching_items:
        print(f"Items in general location '{general_location}':")
        for item in matching_items:
            print(f"- Name: {item.name}, Category: {item.category}, Specific Location: {item.specific_location}, Quantity: {item.quantity}")
    else:
        print(f"No items found in general location '{general_location}'.")


# Function to list items in a category when an item is not found
def list_items_in_category(category):
    if category in categories:
        print(f"Items in category '{category}':")
        view_items_by_category(category)
    else:
        print(f"Category '{category}' does not exist.")


# Example usage
if __name__ == "__main__":
    #  Testing will go down here:
    # Add items
    add_item("Screwdriver", 50, "Tool Shed", "Shelf A", "Tools")
    add_item("Hammer", 30, "Tool Shed", "Shelf B", "Tools")
    add_item("Paint", 20, "Storage Room", "Rack 3", "Supplies")
    add_item("Wrench", 15, "Tool Shed", "Shelf C", "Tools")
    add_item("Drill", 10, "Tool Shed", "Shelf D", "Tools")
    add_item("Brush", 25, "Storage Room", "Rack 2", "Supplies")
    add_item("Ladder", 5, "Garage", "Corner", "Equipment")

    # Delete an item
    delete_item("Hammer")

    # Search for items
    search_item("Screwdriver")
    search_item("Hammer")  # Should indicate item not found

    # Find item location
    find_item_location("Paint")

    # View items by category
    view_items_by_category("Tools")
    view_items_by_category("Supplies")

    # View items by general location
    view_items_by_location("Tool Shed")
    view_items_by_location("Garage")

    # List items in a category if an item is not found
    item_name = "Chainsaw"
    item = hash_table.search(item_name)
    if item is None:
        print(f"Item '{item_name}' not found.")
        category = "Tools"
        print(f"Here are items in the '{category}' category:")
        view_items_by_category(category)




