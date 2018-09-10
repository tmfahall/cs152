##inputs
#inches (float)

##outputs
#centimeters (float)

def inchesToCentimeters(inches):
    return str(inches/0.39370)

inches = input("Enter total inches: ")

returnString = str(inches) + " inches is equal to " + inchesToCentimeters(inches) + " centimeters"

print(returnString)
