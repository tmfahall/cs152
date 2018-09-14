# Author: Andrew Hall
# Date: 9/14/18
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 2

import math

##inputs
#radius (float)

##outputs
#diameter (float),
#circumference (float),
#area (float)

def radiusToDiameter(radius):
    diameter = str(radius*2)
    return diameter

def radiusToCircumference(radius):
    circumference = str(radius * math.pi * 2)
    return circumference

def radiusToArea (radius):
    area = str(math.pi * math.pow(radius, 2))
    return area

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

radius = getInput("Enter radius: ")

d = "Diameter = " + radiusToDiameter(radius) + " units"
c = "Circumference = " + radiusToCircumference(radius) + " units"
a = "Area = " + radiusToArea(radius) + " units"

returnString = "If the radius of a circle is " + str(radius) + " units:\n" + d + "\n" + c + "\n" + a + "\n"

print(returnString)
