from item import Item

item1 = Item("MyItem", 750)

# item1.name = 'otheritem' # will throw error , as it is read only; if a setter is there, no error

# print(item1.name)

item1.new_name('yash')

print(item1.name)

# testing some code