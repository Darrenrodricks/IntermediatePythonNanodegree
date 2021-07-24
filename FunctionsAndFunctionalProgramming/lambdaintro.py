

(lambda x: x > 3)(4)  # => True

# Squares from 0**2 to 9**2
map(lambda val: val ** 2, range(10))

# Tuples with positive second elements
filter(lambda pair: pair[1] > 0, [(4,1), (3, -2), (8,0)])

# Sort a collection based on a custom function.
sorted([(4,1), (3, -2), (8,0)], key=lambda pair: pair[1])


# triple = lambda x: x * 3
# a waste of lambda  because it is saved  within a variable for multiple usages
# whereas lambda is supposed to be used once for small functional tasks
