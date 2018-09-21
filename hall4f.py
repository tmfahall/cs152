# Author: Andrew Hall
# Date: 9/19/2018
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 4f

# inputs integers M and N then outputs the product (M * N)
# without using the multiplication operator.


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


def sum_of_n_groups_of_m(integer_n, integer_m):
    total = 0
    counter = integer_n

    while counter > 0:
        total = total + integer_m
        counter = counter - 1

    return total


input_message = "Enter an integer: "
input_type = int

integer_n = get_input(input_message, input_type)
integer_m = get_input(input_message, input_type)

return_int = sum_of_n_groups_of_m(integer_n, integer_m)

print(return_int)
