import csv

class Item:

    pay_rate = 0.8 # this is a class attribute
    all = []
    def __init__(self, name: str, price: int, quantity: int = 0):  # clearly defined the type of input required

        # run validations to the received arguments
        assert type(price) == int, f"price {price} is not int"  # assert will validate the arguments with the passed conditions and if error found will send
        assert type(quantity) == int, f"quantity {quantity} is not int" # the message
        
        #assign to sefl object
        self.__name = name # this way I can use the property decorator for creating name as a read only attribute of the Item class; if I do __name, then this is a private attribute and I cannot access (__name) this out of the class
        self.price = price
        self.quantity = quantity

        # actions
        Item.all.append(self)

    @property # getter; encapsulation
    def name(self):
        return self.__name
    
    def new_name(self, text): # changes can be indirectly made or by using setter as shown below, not directly
        self.__name = self.__name + text
    
    # @name.setter # format : @<property_name>.setter ; in this case name, we will set the value even it is a read only using this decorator
    # def name(self, value):
    #     self.__name  = value
        
    #testing some code 

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
    
    # @property # encapsulation, for creating read only attributes; encapsulation requires __ before the attribute ; example = __name
    # def read_only_name(self):
    #     return "AAA"
    
