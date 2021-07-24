s = 'Udacity'

# Access an element by index, starting at position 0.
s[0] == 'U'
s[1] == 'd'
s[4] == 'i'
s[7] # Bad!

# Access an element by a negative index, starting at the end.
s[-1] == 'y'
s[-2] == 't'
s[-4] == 'c'
s[-7] == 'U'

s[1:5:2] == 'dc'
s[4::-2] == 'iaU'

