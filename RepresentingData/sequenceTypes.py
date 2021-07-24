# Slicing
hello = 'Hello, world!'

a = hello[0]  # Turn me into 'H'
b = hello[11]  # Turn me into 'd'
c = hello[1:5]  # Turn me into 'ello'
d = hello[-6:]  # Turn me into 'world!'
e = hello[::2]  # Turn me into 'Hlo ol!'
f = hello[::-1]  # Turn me into '!dlrow ,olleH'

# Manipulating Strings

def make_palindrome(s):
    """Create a palindrome with the given string as a prefix.

    A palindrome is text that reads the same forwards and backwards.

    :param s: A string to form the prefix of a new palindrome.
    """

    return s + s[::-1]

