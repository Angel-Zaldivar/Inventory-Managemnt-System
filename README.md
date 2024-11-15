# Inventory-Managemnt-System

## Overview

The Inventory Management System allows users to add, delete, search, and view items dynamically, with no predefined categories or limitations on the number of items.

## Data Structures Used

- **Arrays (Dynamic Lists):**
  - Used for storing categories (`categories` list).
  - Used for storing items within each category (`category_items` dictionary with lists).

- **Hash Table with Dynamic Resizing:**
  - Used for quick lookup of items by their names.
  - Supports dynamic resizing to accommodate an unlimited number of items.
  - Collisions are handled using linked lists (separate chaining).

- **Linked Lists:**
  - Used within the hash table to handle collisions.

## Key Features

- **Dynamic Item Addition:**
  - No fixed size; the system can handle a growing number of items efficiently.

- **Dynamic Categories:**
  - Users can create categories on the fly by adding items with new categories.

- **Efficient Operations:**
  - Average-case O(1) time complexity for insertions, deletions, and searches in the hash table.

## Classes and Functions

- **Item Class:**
  - Represents an item with attributes like `name`, `quantity`, etc.

- **HashTable Class:**
  - Implements a dynamic hash table with methods `insert`, `search`, and `delete`.
  - Automatically resizes when the load factor exceeds 0.7.

- **Functions:**
  - `add_item`: Adds an item to the inventory.
  - `delete_item`: Deletes an item from the inventory.
  - `search_item`: Searches for an item by name.
  - `find_item_location`: Finds the location of an item.
  - `view_items_by_category`: Views all items in a category.
  - `view_items_by_location`: Views all items in a general location.
  - `list_items_in_category`: Lists items in a category when an item is not found.

## Error Handling

- **Duplicate Items:**
  - The system checks for existing items before adding new ones to prevent duplicates.

- **Non-Existent Items:**
  - Appropriate messages are displayed when attempting to delete or search for items that do not exist.

- **Empty Categories:**
  - Categories with no items are automatically removed from the system.
