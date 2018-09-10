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

radius = input("Enter radius: ")

d = "Diameter = " + radiusToDiameter(radius) + " units"
c = "Circumference = " + radiusToCircumference(radius) + " units"
a = "Area = " + radiusToArea(radius) + " units"

returnString = "A radius of " + str(radius) + " units has:\n" + d + "\n" + c + "\n" + a + "\n"

print(returnString)
