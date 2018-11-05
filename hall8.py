# Author: Andrew Hall
# Date: 11/05/18
# Class: CSIS 152
# Assignment: Program 8

import math


def main():
    find_print_primes(243, 10000)


def find_print_primes(start_num, end_num):
    working_list = []
    test_list = []

    finished = False

    max_multiple = math.floor(math.sqrt(end_num))

    for num in range(2, max_multiple + 1):
        test_list.append(num)

    for num in range(start_num, end_num):
        if num > 1:
            working_list.append(num)

    while not finished:
        num_to_check = test_list[0]

        # checks list for multiples of next_prime
        # create a second list to work on to avoid index and closure issues
        # i didn't test to see if it was necessary but just to play it safe
        working_list_closure = working_list
        test_list_closure = test_list

        # loop through the list of remaining numbers
        for num in working_list_closure:
            # if a number in the list is a multiple of the check number
            if num > num_to_check:
                if num % num_to_check == 0:
                    # remove it
                    working_list.remove(num)

        # loop through list of test numbers
        for num in test_list_closure:
            # if a number in the list is a multiple of the check number
            if num % num_to_check == 0:
                # remove it
                test_list.remove(num)

        if len(test_list) == 0:
            finished = True

    output_string = ""

    for num in working_list:
        output_string += str(num) + " "

    print(output_string)


main()
