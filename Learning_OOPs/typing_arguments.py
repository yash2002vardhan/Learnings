class Item:
    def __init__(self, name: str, price: int, quantity: int):  # clearly defined the type of input required

        # run validations to the received arguments
        assert type(price) == int, f"price {price} is not int"  # assert will validate the arguments with the passed conditions and if error found will send
        assert type(quantity) == int, f"quantity {quantity} is not int" # the message
        
        #assign to sefl object
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price*self.quantity

    

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)

cost1 = item1.calculate_total_price()
cost2 = item2.calculate_total_price()

print(f"Total Price : {cost1}")
print(f"Total Price : {cost2}")

# we can add other attributes to items apart from the __init__ method
# example

item2.has_numpad = False