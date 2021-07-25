from pathlib import Path

here = Path('.')  # Get an instance of a Path subclass describing the interpreter's current location (which is usually, but not necessarily, the directory containing your Python files).
here = here.resolve()  # Resolve symbolic links and `..` segments into an absolute `Path`.
parent = here.parent  # Navigate up the chain of parents. A purely lexical operation, so it's important to call `.resolve()` or a similar method first.
child = here / 'subfolder' / 'subfile.txt'  # Navigate to a subfolder or subfile. Hooray for magic methods (`__div__`) and polymorphism!

# **************NOTES******************
#
# The general pattern for reading and writing plain text from files is:
#
# 1. Extract data from a file into Python
#  - Open a file-like object f
#  - Call f.read() or a similar method
# 2. Do something with the data, now within Python
# 3. Write data from Python to a file.
#  - Open a file-like object f
#  - Call f.write(line) or a similar method

# (A)
with open('my-outfile-file.txt', 'w') as outfile:
    outfile.write("Hello, world!")

# (B)
outfile = open('my-outfile-file.txt', 'w')
outfile.write("Hello, world!")
# Oops! We forgot to close the file.

# A is the correct way to write this




# Example
# Suppose that we have a file queries.txt:
#
#  *** python programmer ***
#  *** UDACITY ***
#  *** Web developer ***
#
# and that we wish to write a program that will normalize the queries in this file by lowercasing them all and removing the extra lines between each query.

# (1) Extract data from the `queries.txt` file into Python.
with open('queries.txt', 'r') as infile:
    contents = infile.read()  # Read one big string - the contents of this file.


# (2) Transform the data within Python.
queries = contents.split('\n')  # Split the string into a list by line breaks.
normalized = [query.strip().lower() for query in queries[::2]]  # Normalize each query with the stripped, lowercased version of every other line.

# (3) Write the normalized queries out to a file.
with open('normalized-queries.txt', 'w') as outfile:
    for query in normalized:
        outfile.write(query + '\n')  # It might be better to use outfile.writelines here, but let's practice `.write`-ing strings.

