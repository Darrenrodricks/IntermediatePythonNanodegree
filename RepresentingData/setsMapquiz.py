"""Check whether a word is 'efficient' - if each letter can be drawn by a pencil without lifting."""
EFFICIENT_LETTERS = set('BCDGIJLMNOPSUVWZ')

def is_efficient(letters):
    for char in EFFICIENT_LETTERS:
        if letters != EFFICIENT_LETTERS:
            return True

"""Swap the keys and values in a mapping."""


def swap_keys_and_values(d):
    swapped = {}
    for key, value in d.items():
        if value not in swapped:
            swapped[value] = set()
        swapped[value].add(key)
    return swapped