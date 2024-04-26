class Item:

    pay_rate = 0.8 # this is a class attribute
    all = []
    def __init__(self, name: str, price: int, quantity: int):  # clearly defined the type of input required

        # run validations to the received arguments
        assert type(price) == int, f"price {price} is not int"  # assert will validate the arguments with the passed conditions and if error found will send
        assert type(quantity) == int, f"quantity {quantity} is not int" # the message
        
        #assign to sefl object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discout(self):
        self.price = self.price * self.pay_rate # we can also do self.calculate_total_price()*Item.pay_rate , 
                                                        # pay_rate can be accessed by both class and instance
        
    def __repr__(self):  # returns the representation version of the instances of the class
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"

    

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item('Keyboard', 100, 20)
item4 = Item('Mouse', 20, 3)

print(Item.all)

# for instance in Item.all:
#     print(instance.name)