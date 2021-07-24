class MyFirstClass:
    """A simple example class."""
    num = 12345

    def greet(self):
        return "Hello, world"


print(MyFirstClass)

print(MyFirstClass.num)
print(MyFirstClass.greet)

print(type(MyFirstClass.__dict__))
print('num' in MyFirstClass.__dict__)
print('greet' in MyFirstClass.__dict__)


class House:
    layout = 'square'

    def paint(self, color):
        self.color = color


print(House.layout)
print(House.paint)

home = House()
print(home)
print(type(home) is House) 


home.size = '1000'
print(home.size)
print(home.__dict__)

home.color = 'red'
print(home.__dict__)

home.num_bathrooms = 2
home.num_bedrooms = 3
print(home.__dict__)

home.color = 'blue'
print(home.color)
print(home.num_bathrooms)