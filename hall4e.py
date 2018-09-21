# Author: Andrew Hall
# Date: 9/19/2018
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 4e

# inputs an integer N then outputs the odd integers from 1 to N inclusive 
# then outputs the even integers from 1 to N inclusive.


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


def get_odds_and_evens(integer_n):
    odd_list = list()
    even_list = list()
    counter = integer_n

    while counter > 0:
        if counter % 2 == 0:
            even_list.insert(0, counter)
        else:
            odd_list.insert(0, counter)
        counter = counter - 1

    return (odd_list, even_list)


input_message = "Enter an integer: "
input_type = int

integer_n = get_input(input_message, input_type)
return_tuple = get_odds_and_evens(integer_n)

for int_list in return_tuple:
    print(", ".join(str(item) for item in int_list))

