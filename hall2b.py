# Author: Andrew Hall
# Date: 9/14/18
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 2

##inputs
#miles (float)

##outputs
#kilometers (float)

def milesToKilometers(miles):
    kilometers = miles*1.60934
    return kilometers

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

miles = getInput("Enter total miles: ")
kilometers = milesToKilometers(miles)

kilometersAsString = str(kilometers)

returnString = (str(miles)) + " miles is equal to " + kilometersAsString + " kilometers"

print(returnString)