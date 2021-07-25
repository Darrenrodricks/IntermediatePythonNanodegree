import random, os

catString = "--Whiskers--, --Spot--, --Meowmeow--, --Tiger--, --Kitty--, --Henry--, --Mr.Paws--"
def RANDOM_CAT(string_list):
    cat_list = catString.split(', ')# split the cats
    cat_list = [cat.strip('--') for cat in cat_list]
    return random.choice(cat_list)

print(  f'{RANDOM_CAT(catString)} is a good kitty'  )

class Document():

    def __init__(self, filename):
        self.filename = filename

contract = Document('agreement3234.docx')
signed_contract = contract
signed_contract.filename = 'agreement3234_signed.pdf'

print(contract.filename)

