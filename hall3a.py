#Author: Andrew Hall
#Date: 9/19/2018
#Class: CSIS 152
#Instructor: Dr. Brekke
#Assignment: Program 3a

#calculate MPH given distance, hours, minutes, and seconds

##inputs
#distance traveled in miles(float)
#time in hours(int)
#time in minutes(int)
#time in seconds(int)

##outputs
#avg mph(float) rounded to 1 decimal

def mphFinder(distance, time):
    mph = distance / time

    return mph

def hmsToTime(hours, minutes, seconds):
    hoursAsIntPerHour = int(hours)
    minutesAsIntPerHour = int(minutes) / 60
    secondsAsIntPerHour = int(seconds) / 60 / 60

    totalTime = hoursAsIntPerHour + minutesAsIntPerHour + secondsAsIntPerHour

    return totalTime

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

distance = getInput("Enter total miles: ")
hours = getInput("How many hours? ")
minutes = getInput("How many minutes? ")
seconds = getInput("How many seconds? ")

time = hmsToTime(hours, minutes, seconds)

mph = mphFinder(distance, time)

mphToOneDecimalAsString = str(round(mph, 1))

returnString = mphToOneDecimalAsString + " MPH"

print(returnString)
