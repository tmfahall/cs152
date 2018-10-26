import datetime


def main():
    date_to_use = birthday_getter()

    month = date_to_use[0]
    day = date_to_use[1]
    year = date_to_use[2]

    leapyear = is_leapyear(year)

    if is_real_year(year) is not True or \
            is_real_month(month) is not True or \
            is_real_day(month, day, leapyear) is not True:
        print("not a valid date")
    else:
        output_gatherer(day, month, year)


def birthday_getter():
    print("Input your birthday as all ints")

    month = int(input("enter month: "))
    day = int(input("enter day: "))
    year = int(input("enter year: "))

    date = [month, day, year]

    return date


def is_real_year(year):
    year_is_real = True
    if year < 1:
        year_is_real = False

    return year_is_real


def is_real_month(month):
    month_is_real = True
    if month > 12 or month < 1:
        month_is_real = False

    return month_is_real


def is_leapyear(year):
    year_is_leapyear = False
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        year_is_leapyear = True

    return year_is_leapyear


def is_real_day(month, day, leapyear):
    day_is_real = True
    if day > 31 or day < 1:
        day_is_real = False
    elif month == 2 and leapyear is not True and day > 28:
        day_is_real = False
    elif month in [4, 6, 9, 11] and day > 30:
        day_is_real = False
    elif month in [1, 3, 5, 7, 10, 12] and day > 31:
        day_is_real = False

    return day_is_real


def age_finder(day, month, year):
    current_month = int(datetime.datetime.now().month)
    current_day = int(datetime.datetime.now().day)
    current_year = int(datetime.datetime.now().year)

    age = current_year - year

    if current_month < month or current_month == month and current_day <= day:
        age += 1

    return age


def is_birthday(day, month):
    current_month = int(datetime.datetime.now().month)
    current_day = int(datetime.datetime.now().day)
    birthday = False

    if current_month == month and current_day == day:
        birthday = True

    return birthday


def month_name_getter(month):
    month_name = "January"
    if month == 2:
        month_name = "February"
    elif month == 3:
        month_name = "March"
    elif month == 4:
        month_name = "April"
    elif month == 5:
        month_name = "May"
    elif month == 6:
        month_name = "June"
    elif month == 7:
        month_name = "July"
    elif month == 8:
        month_name = "August"
    elif month == 9:
        month_name = "September"
    elif month == 10:
        month_name = "October"
    elif month == 11:
        month_name = "November"
    elif month == 12:
        month_name = "December"

    return month_name


def number_suffix_finder(day):
    suffix = "th"
    if day in [1, 21, 31]:
        suffix = "st"
    elif day in [2, 22]:
        suffix = "nd"
    elif day in [3, 23]:
        suffix = "rd"

    return suffix


def outputter(month_string, day_string, age, birthday):
    print("Your birthday is {0} {1}, you are {2} years old". format(month_string, day_string, age))
    if birthday is True:
        print("Happy Birthday!")


def output_gatherer(day, month, year):
    age = age_finder(day, month, year)
    birthday = is_birthday(day, month)
    month_string = month_name_getter(month)
    day_string = str(day) + number_suffix_finder(day)

    outputter(month_string, day_string, age, birthday)


main()
