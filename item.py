# item.py
class Item:
    def __init__(self, name, quantity, general_location, specific_location, category):
        self.name = name
        self.quantity = quantity
        self.general_location = general_location
        self.specific_location = specific_location
        self.category = category
