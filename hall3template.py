#Author: Andrew Hall
#Date: 9/19/2018
#Class: CSIS 152
#Instructor: Dr. Brekke
#Assignment: Program 3

def getInput(text):
    while True:
        try:
            usersInput = float(input(text))
        except (ValueError, NameError):
            print("Input must be of type float or integer!")
            continue
        else:
            return usersInput
            break
