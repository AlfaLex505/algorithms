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


def yellow_print(text):
    """
    Function for printing red text.
    """
    print(f"\033[93m {text}\033[00m")


def print_colored_list(random_list):
    """
    Function for printing a list colored based on wether or not the elements
    are correctly sort
    """
    final_string = ''
    k = 0
    print('\nList iteration:')
    while k < len(random_list):
        if random_list[k -1] <= random_list[k] or k == 0:
            final_string += f'\033[92m{random_list[k]}\033[00m '
        else:
            final_string += f'\033[91m{random_list[k]}\033[00m '
        k += 1

    print(final_string)


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

        print_colored_list(random_list)


def bubble_sort(random_list):
    """
    Function for programming a sorting algorithm.
    """
    swaps = 1
    while swaps > 0:
        i = 0
        print_colored_list(random_list)
        swaps = 0
        while i < len(random_list)-1:
            if random_list[i] > random_list[i + 1]:
                # print(f'{random_list[i]} is greater than {random_list[i+1]}')
                aux = random_list[i]
                random_list[i] = random_list[i + 1]
                random_list[i + 1] = aux
                swaps += 1

            i += 1
            print_colored_list(random_list)

        yellow_print(f'number of swaps: {swaps}')



def main():
    """
    Where the magic happens!
    """
    # random_list = generate_random_list(10)
    random_list = [72, 21, 19, 44, 48, 77, 53, 98, 46, 63]
    # insertion_sort(random_list)
    bubble_sort(random_list)


if __name__ == '__main__':
    main()
