from item import Item

class Phone(Item): # this class in inheriting properties from the Item class
    def __init__(self, name: str, price: float, quantity: int, broken_phones = 0):
        super().__init__(name, price, quantity) # responsible for inheriting all attributes and the methods of the parent class <Item>

        self.broken_phones = broken_phones