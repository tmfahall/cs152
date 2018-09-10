##inputs
#miles (float)

##outputs
#kilometers (float)

def milesToKilometers(miles):
    return str(miles*1.60934)

miles = input("Enter total miles: ")

returnString = (str(miles)) + " miles is equal to " + milesToKilometers(miles) + " kilometers"

print(returnString)
