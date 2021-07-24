def print_my_arguments(a, *b, c=1):
    print(f"a={a}, b={b}, c={c}")

print_my_arguments(2)                   # a=2, b=(), c=1
print_my_arguments(2, 7)                # a=2, b=(7,), c=1
print_my_arguments(2, 7, 1)             # a=2, b=(7, 1), c=1
print_my_arguments(2, 7, 1, 8)          # a=2, b=(7, 1, 8), c=1
print_my_arguments(2, 7, 1, 8, 2)       # a=2, b=(7, 1, 8, 2), c=1
print_my_arguments(2, 7, 1, 8, 2, c=8)  # a=2, b=(7, 1, 8, 2), c=8


def product(*nums, start=1):
    running_product = start
    for number in nums:
        running_product *= number
    return running_product


product(3, 5)  # => 15
product(3, 4, 2)  # => 24
product(3, 4, 2, 5)  # => 120
product()  # => 1
product(7, start=15)  # => 105
product(5, 6, start=10)  # => 300