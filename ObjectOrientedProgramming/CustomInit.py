class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color

home = House(1000, color='red')
print(home.size)
print(home.color)

mansion = House(25000)
print(mansion.size)
print(mansion.color)


# ******************* MINI QUIZ **************************
# Define a class object Notebook that can be instantiated with three arguments - a number of pages
# (required), a paper size description (optional, defaulting to 'a4'), and a spacing description
# (optional, defaulting to 'college')
# Your class should be able to be initialized like:
# journal = Notebook(80, size='letter', spacing='wide')
# You should set three attributes on the instance object in the initializer - pages, size, and spacing.
# Have some fun here too! Are there other attributes you would like your notebook to have?


class Notebook:
    def __init__(self, pages, size='a4', spacing='college'):
        self.pages = pages
        self.size = size
        self.spacing = spacing


journal = Notebook(80, size='letter', spacing='wide')



