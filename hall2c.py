# Author: Andrew Hall
# Date: 9/14/18
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 2

##inputs
# Fahrenheit temperature (float)

##outputs
# Celsius temperature (float)

def fahrenheitToCelsius(fahrenheit):
    celsius = (((fahrenheit-32)*5)/9)
    return celsius

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

fahrenheit = getInput("Enter Fahrenheit temperature: ")
celsius = fahrenheitToCelsius(fahrenheit)

returnString = str(fahrenheit) + " degrees Fahrenheit = " + str(celsius) + " degrees Celsius"

print(returnString)
