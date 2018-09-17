#Author: Andrew Hall
#Date: 9/19/2018
#Class: CSIS 152
#Instructor: Dr. Brekke
#Assignment: Program 3b

#calculate time from mph

##inputs 
#miles(float)
#MPH (float)

##outputs 
#hours(int)
#min(int)
#sec(int) seconds should be rounded

def mphToTime(miles, mph):
    timeAsFloat = miles / mph

    return timeAsFloat

def timeAsFloatToHMS(timeAsFloat):
    hours = round(timeAsFloat)
    timeAsFloatLessHours = timeAsFloat - hours

    minutes = round(timeAsFloatLessHours * 60)
    timeAsFloatLessHoursAndMinutes = timeAsFloatLessHours - minutes

    seconds = round(timeAsFloatLessHoursAndMinutes * 60 * 60)

    #########LEFT OFF HERE - RETURN HMS AS TUPLE

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
