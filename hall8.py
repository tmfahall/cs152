def main():
    find_print_primes(1, 100)


def find_print_primes(start_num, end_num):
    primes = []
    working_list = []

    finished = False

    next_prime = 2

    for num in range(start_num, end_num):
        if num > 1:
            working_list.append(num)

    while not finished:
        num_to_check = working_list[0]

        # checks list for multiples of next_prime
        # create a second list to work on to avoid index and closure issues
        # i didn't test to see if it was necessary but just to play it safe
        working_list_closure = working_list

        # remove the number we're checking from the list we're checking against
        # working_list_closure.remove(num_to_check)

        if num_to_check == next_prime:
            # is prime
            primes.append(num_to_check)

        # loop through the list of remaining numbers
        for num in working_list_closure:
            # if a number in the list is a multiple of the check number
            if num % num_to_check == 0:
                # remove it
                working_list.remove(num)

        if len(working_list) == 0:
            finished = True
        else:
            next_prime = working_list_closure[0]

    output_string = ""

    for num in primes:
        output_string += str(num) + " "

    print(output_string)


main()
