import csv

class Item:

    pay_rate = 0.8 # this is a class attribute
    all = []
    def __init__(self, name: str, price: float, quantity: int):  # clearly defined the type of input required

        # run validations to the received arguments
        assert type(price) == float, f"price {price} is not float"  # assert will validate the arguments with the passed conditions and if error found will send
        assert type(quantity) == int, f"quantity {quantity} is not int" # the message
        
        #assign to sefl object
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # we can also do self.calculate_total_price()*Item.pay_rate , 
                                                        # pay_rate can be accessed by both class and instance
        
    # def instantiate_from_csv(self):  # we have to convert this to a class method, as this method itself is responsible for instantiating an instance
    @classmethod # a decorator for converting this to a class method    
    def instantiate_from_csv(cls):  # class wil be passed as an argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),

            )
    @staticmethod # does not receive any class or instance as an argument
    def check_integer(num):
        # we will count out the floats that are point zero
        # example : 10.0, 5.0
        if isinstance(num, float):
            return num.is_integer() # returns True for floats with point zero and false otherwise
        elif isinstance(num, int):
            return True
        else:
            return False
    

    def __repr__(self):  # returns the representation version of the instances of the class
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    

class Phone(Item): # this class in inheriting properties from the Item class
    def __init__(self, name: str, price: float, quantity: int, broken_phones = 0):
        super().__init__(name, price, quantity) # responsible for inheriting all attributes and the methods of the parent class <Item>

        self.broken_phones = broken_phones


phone1 = Phone('PHone1', 100.0, 5, 1)

print(phone1.calculate_total_price())
print(Phone.all) # this will work as super has inherited all and repr from the parent class
