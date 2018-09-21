# Author: Andrew Hall
# Date: 9/19/2018
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 4g

# inputs an integer N, then inputs N additional integers and finds and outputs the average of the N integers.

finished = False
int_list = list()


def get_input(input_text_local, input_type_local):
    global finished
    while not finished:
        try:
            if input_type_local == str:
                type_string = "string"
                users_input = str(input(input_text_local))
            if input_type_local == int:
                users_input = input(input_text_local)
                if users_input == "":
                    finished = True
                    break
                else:
                    type_string = "integer"
                    users_input = int(users_input)
            if input_type_local == float:
                type_string = "float"
                users_input = float(input(input_text_local))
        except (ValueError, NameError):
            print("Input must be of type " + type_string + "!")
            continue
        else:
            return users_input


def get_sum(int_list_local):
    sum_from_int_list = 0

    for number in int_list_local:
        sum_from_int_list = sum_from_int_list + number

    return sum_from_int_list


def get_count(int_list_local):
    total_items_in_int_list = 0

    for number in int_list_local:
        total_items_in_int_list += 1

    return total_items_in_int_list


def get_average(total_sum, total_number):
    average = total_sum / total_number

    return average


input_message = "Enter an integer: "
input_type = int

while not finished:
    integer_n = get_input(input_message, input_type)

    if type(integer_n) == int:
        int_list.append(integer_n)


int_list_sum = get_sum(int_list)
int_list_count = get_count(int_list)
int_list_average = get_average(int_list_sum, int_list_count)


# debugging
print(int_list)
print("total / count = average")
print(str(int_list_sum) + " / " + str(int_list_count) + " = " + str(int_list_average))


# using import functools just to try some stuff

from functools import reduce

int_list_sum_reduce_lambda = reduce((lambda a, b: a + b), int_list)
int_list_average_reduce_lambda = reduce(lambda a, b: a + b, int_list) / float(len(int_list))

print(int_list_sum_reduce_lambda)
print(int_list_average_reduce_lambda)
