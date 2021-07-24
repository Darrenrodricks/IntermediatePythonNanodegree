def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)

# 1 keyword argument
parrot(voltage=1000)

# 2 keyword arguments
parrot(voltage=1000000, action='VOOOOOM')

# 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)

# 3 positional arguments
parrot('a million', 'bereft of life', 'jump')

# 1 positional, 1 keyword
parrot('a thousand', state='pushing up the daisies')


def ask_yn(prompt, retries=4, complaint='Enter Y/N!'):
    for i in range(retries):
        ok = input(prompt).strip()
        if ok in ('Y', 'y'):
            return True
        if ok in ('N', 'n'):
            return False
        print(complaint)
    return False


# Call with only the mandatory argument
ask_yn('Really quit?')

# Call with one keyword argument
ask_yn('OK to overwrite the file?', retries=2)

# Call with one keyword argument - in any order!
ask_yn('Update status?', complaint='Just Y/N')

# Call with all of the keyword arguments
ask_yn('Send text?', retries=2, complaint='Y/N please!')

# These can provide variants of a simple idea.
ask_yn("Do you like raindrops on roses?")
ask_yn("How about whiskers on kittens?", retries=10)
ask_yn("Any love for bright copper kettles?", complaint="Yes or no :)")
ask_yn("Would you like warm woolen mittens?", retries=10, complaint="A yes or no shall suffice.")



