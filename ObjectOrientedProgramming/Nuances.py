class House:
    def __init__(self, size):
        self.size = size
        self.appliances = []

    def install(self, appliance):
        self.appliances.append(appliance)


home = House(1000)
vacation_home = House(5000)

# The two homes no longer share a single list of appliances!
print(home.appliances is vacation_home.appliances)  # False

home.install('oven')
home.install('microwave')
print(home.appliances)
print(vacation_home.appliances)

print(home.__dict__)
print(vacation_home.__dict__)


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = set()
    def teach(self, trick):
        self.tricks.add(trick)

# Change the broken code above so that the following lines work:
#
buddy = Dog('Buddy')
pascal = Dog('Pascal')
buddy.teach('sit')
pascal.teach('fetch')
buddy.teach('roll over')
print(buddy.tricks)  # {'sit', 'roll over'}
print(pascal.tricks)  # {'fetch'}