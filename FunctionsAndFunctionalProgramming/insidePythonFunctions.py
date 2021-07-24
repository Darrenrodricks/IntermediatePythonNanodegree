product = 'Water'

def shadowing_example(price):
    product = 'Bottled Water'  # Oops! Same name as in the global scope.
    quantity = 50
    print(locals())  # A
    print(globals()['product'])  # B
    print(product, price, quantity)  # C

shadowing_example(10)

# All function calls return one object
# The statement return value1,  value2 returns a tuple of two values
