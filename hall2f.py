# Author: Andrew Hall
# Date: 9/14/18
# Class: CSIS 152
# Instructor: Dr. Brekke
# Assignment: Program 2

import math

#inputs
#principle (float - amount of loan), 
#APR (float - annual percentage rate entered as 4.5 or %4.5),
#term (int -length of the loan in years)

#****Input MUST be in the order given.

##outputs
#monthly payment (float) = Amt /
#total amount paid for the loan (float),
#total interest paid (float) for the loan.

def monthlyPayment(principle, apr, term):
    i = apr / 12
    n = term * 12
    payment = principle * (i / (1 - math.pow((1 + i), (-n))))

    return payment


def totalAmountPaid(monthlyPayment, term):
    totalPaid = monthlyPayment * term * 12
    return totalPaid


def totalInterestPaid(totalPaid, principle):
    totalInterest = totalPaid - principle
    return totalInterest

def getInput(text):
    while True:
        usersInput = input(text)


        try:
            usersInput = float(usersInput)
        except (ValueError):
            print("Input must be of type float or integer!")
            continue
        else:
            return usersInput
            break


principle = getInput("Enter loan principle: ")
apr = getInput("Enter APR: ")
term = getInput("Enter loan term: ")

print("apr = " + str(apr))

if int(apr) > 0:
    apr = apr / 100

print("apr = " + str(apr))

mp = monthlyPayment(principle, apr, term)
print("apr = " + str(apr))

tp = totalAmountPaid(mp, term)
print("apr = " + str(apr))

ti = totalInterestPaid(tp, principle)
print("apr = " + str(apr))

monthlyPaymentString = "$" + str(mp)
totalPaidString = "$" + str(tp)
totalInterest = "$" + str(ti)

print("apr = " + str(apr))


returnTuple = (
    "Monthly payment is " + monthlyPaymentString,
    "Total paid over lifetime of loan is " + totalPaidString,
    "Total interest paid on loan is " + totalInterest
)

for i in returnTuple:
    print(i)
