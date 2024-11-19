from hash_table import HashTable
from item import Item

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

    print("Hi! Welcome back to BinBase!")
    print()

    cont = True

    while cont:
        print('Please choose an option:\n')
        user_input = int(input(
            'Add an item (1)\n'
            'Delete an item (2)\n'
            'View an item and their attributes (3)\n'
            'Get the location of one of your items (4)\n'
            'View items by category (5)\n'
            'View items by location (6)\n\n'
            'Enter your choice: '
        ))

        print()

        if user_input == 1:
            print('To add an item, enter Name, Quantity, General Location, Specific Location, and Category.')
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            item_general_location = input('Enter item general location: ')
            item_specific_location = input('Enter item specific location: ')
            item_category = input('Enter item category: ')
            add_item(item_name, item_quantity, item_general_location, item_specific_location, item_category)

        elif user_input == 2:
            item_name = input('To delete an item, input the item\'s name: ')
            print()
            delete_item(item_name)

        elif user_input == 3:
            item_name = input('Enter the name of the item you want to view: ')
            print()
            search_item(item_name)

        elif user_input == 4:
            item_name = input('Enter the name of the item to find its location: ')
            print()
            find_item_location(item_name)

        elif user_input == 5:
            item_category = input('Enter the category you want to view: ')
            print()
            view_items_by_category(item_category)

        elif user_input == 6:
            general_location = input('Enter the general location you want to view: ')
            print()
            view_items_by_location(general_location)

        else:
            print('Invalid choice. Please enter a number between 1 and 6.')

        print()

        if input('Would you like to continue? (y/n):  ') == 'y':
            print()
            cont = True
        else:
            cont = False

    print('Thank you for using BinBase!\nWe hope to see you again!')