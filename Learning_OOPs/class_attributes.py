class Item:

    pay_rate = 0.8 # this is a class attribute
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
    
    def apply_discout(self):
        self.price = self.price * self.pay_rate # we can also do self.calculate_total_price()*Item.pay_rate , 
                                                        # pay_rate can be accessed by both class and instance

    

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

# print(Item.pay_rate)
# print(item1.pay_rate) # class attributes can be accessed by the instances as well
# print(Item.__dict__) # will give all the attributes at the class level
# print(item1.__dict__) # will give all the attribtes at the instance level

print(item1.price)
item1.apply_discout()
print(item1.price)

# we can explicitly define the class attribute for an instance

item2.pay_rate = 0.7 # you have to ensure that in the method <apply_discount> it is self.pay_rate and not Item.pay_rate or else value will not be override

print(item2.price)
item2.apply_discout()
print(item2.price)