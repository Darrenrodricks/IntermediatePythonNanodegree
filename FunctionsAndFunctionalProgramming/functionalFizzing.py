import helper

"""Generate an infinite stream of successively larger random lists."""

def generate_cases():
    a = 0
    while True:
        yield helper.random_list(a)
        a += 1


if __name__ == '__main__':
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)