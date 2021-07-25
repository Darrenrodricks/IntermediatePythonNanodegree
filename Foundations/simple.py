import random

cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
print(cat_string)

cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--"
cat_list = cat_string.split(', ')
cat_list = [cat.strip('--') for cat in cat_list]
print(cat_list)


print(random.int(0, 10))  # generate a random integer between 0 and 10
print(random.choice(['icecream', 'cake', 'pudding'])) # select a random dessert

first = "hello"
second = "world"
print(first+second)
# Output "helloworld"

first = "hello"
second = "world"
print(f'{first}{second}')


cat_string = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--"
cat_list = cat_string.split(', ')
cat_list = [cat.strip('--') for cat in cat_list]
random_cat = random.choice(cat_list)

print(f'{random_cat} is a good kitty')

