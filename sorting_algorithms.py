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


def red_print(text):
    """
    Function for printing red text.
    """
    print(f"\033[91m {text}\033[00m")


def green_print(text):
    """
    Function for printing red text.
    """
    print(f"\033[92m {text}\033[00m")


def insertion_sort(random_list):
    """
    Function for programming a sorting algorithm.
    """
    for i in range(1, len(random_list)):
        key = random_list[i]
        j = i - 1

        while j >= 0 and key < random_list[j]:
            random_list[j + 1] = random_list[j]
            j -= 1
        random_list[j + 1] = key

        k = 0
        print('\nList iteration:')
        while k < len(random_list):
            if random_list[k -1] <= random_list[k] or k == 0:
                green_print(random_list[k])
            else:
                red_print(random_list[k])
            k += 1


def main():
    """
    Where the magic happens!
    """
    random_list = generate_random_list(10)
    # random_list = [72, 21, 19, 44, 48, 77, 53, 98, 46, 63]
    insertion_sort(random_list)


if __name__ == '__main__':
    main()
