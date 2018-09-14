# Author: Andrew Hall
# Date: 9/14/18
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 2

##inputs
#seconds (float)

##outputs
#days (int),
#hours (int),
#minutes (int),
#seconds (int).

#For example, 100000 seconds is 1 day, 3 hours, 46 minutes, and 40 seconds.


def secondsToDHMS(seconds):
    startingSeconds = seconds
    daysString = "0 days"
    hoursString = "0 hours"
    minutesString = "0 minutes"
    secondsString = "0 seconds"

    if seconds > 86400:
        days = seconds//86400
        seconds = seconds - (days * 86400)
        daysString = str(days) + " days"
    
    if seconds > 3600:
        hours = seconds//3600
        seconds = seconds - (hours * 3600)
        hoursString = str(hours) + " hours"

    if seconds > 60:
        minutes = seconds//60
        seconds = seconds - (minutes * 60)
        minutesString = str(minutes) + " minutes"

    if seconds > 0:
        seconds = int(seconds)
        secondsString = str(seconds) + " seconds"

    timeTuple = (daysString, hoursString, minutesString, secondsString, startingSeconds)

    return timeTuple


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

totalSeconds = getInput("Enter total seconds: ")
timeTuple = secondsToDHMS(totalSeconds)

returnString = \
    str(timeTuple[-1]) + " seconds works out to " + \
    timeTuple[0] + ", " + \
    timeTuple[1] + ", " + \
    timeTuple[2] + ", " + \
    timeTuple[3]

print(returnString)
