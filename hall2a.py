# Author: Andrew Hall
# Date: 9/14/18
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 2

##inputs
# inches (float)

##outputs
# centimeters (float)

def inchesToCentimeters(inches):
    centimeters = inches / 0.39370
    return centimeters

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


inches = getInput("Enter total inches: ")
centimeters = inchesToCentimeters(inches)

centimetersAsString = str(centimeters)
returnString = str(inches) + " inches is equal to " + centimetersAsString + " centimeters"

print(returnString)
