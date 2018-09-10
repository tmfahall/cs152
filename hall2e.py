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

    return str(startingSeconds) + " seconds is " + daysString + ", " + hoursString + ", " + minutesString + ", " + secondsString

seconds = input("Enter time in seconds: ")

def isNumber(toTest):
    try:
        float(toTest)
        return True
    except ValueError:
        pass
    
    return False

if isNumber(seconds) == True:
    print(secondsToDHMS(seconds))

else:
    print("input needs to be type float or integer")
