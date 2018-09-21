# Author: Andrew Hall
# Date: 9/19/2018
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 4d

# inputs an integer N then calculates and outputs N! (factorial). 
# N! is 1*2*3*...*N


def get_input(input_text, input_type):
    while True:
        try:
            if input_type == str:
                type_string = "string"
                users_input = str(input(input_text))
            if input_type == int:
                type_string = "integer"
                users_input = int(input(input_text))
            if input_type == float:
                type_string = "float"
                users_input = float(input(input_text))
        except (ValueError, NameError):
            print("Input must be of type " + type_string + "!")
            continue
        else:
            return users_input


def product_of_first_n_integers(integer_n):
    counter = integer_n
    total = 1

    while counter > 0:
        total = total * counter
        counter = counter - 1
    return total

input_message = "Enter an integer: "
input_type = int

integer_n = get_input(input_message, input_type)

total_to_return = product_of_first_n_integers(integer_n)

print(total_to_return)
