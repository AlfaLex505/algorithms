#!/bin/python3

"""
In this file, I will code sorting algorithms.
"""

import random

def generate_random_list(iterations):
    """
    Generate a list of random numbers between zero and a hundred for the
    sorting.
    """
    random_list = []

    i = 0
    while i < iterations:
        random_number = random.randint(0, 100)
        random_list.append(random_number)
        i += 1

    print(f'The randomnly generated list is: {random_list}')

    return random_list


def insertion_sort():
    """
    This function will contain the insertion sort algorithm.
    """


def main():
    """
    Where the magic happens!
    """
    random_list = generate_random_list(10)


if __name__ == '__main__':
    main()
