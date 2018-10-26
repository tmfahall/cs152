import datetime

def main():
    string_for_month = "Enter month as number (for June enter 6): "
    string_for_day = "Enter day as number: "
    string_for_year = "Enter four digit year: "

    month = user_input_getter("month", string_for_month)

    day = user_input_getter("day", string_for_day)

    year = user_input_getter("year", string_for_year)

    if is_real_year_finder(year) is not True:
        user_input_getter("year", string_for_year)

    if is_real_month_finder(month) is not True:
        user_input_getter("month", string_for_month)

    leapyear = is_leapyear_finder(year)

    if is_real_day_finder(month, day, leapyear) is not True:
        user_input_getter("day", string_for_day)

    output_gatherer(day, month, year)


def user_input_getter(type_string, statement):
    return_data = ""
    if type_string == "month":
        return_data = int(input(statement))
    elif type_string == "day":
        return_data = int(input(statement))
    elif type_string == "year":
        return_data = int(input(statement))

    return return_data


def is_real_year_finder(year):
    year_is_real = True
    if year < 1:
        year_is_real = False

    return year_is_real


def is_real_month_finder(month):
    month_is_real = True
    if month > 12 or month < 1:
        month_is_real = False

    return month_is_real


def is_leapyear_finder(year):
    year_is_leapyear = False
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        year_is_leapyear = True

    return year_is_leapyear


def is_real_day_finder(month, day, leapyear):
    day_is_real = True
    if day > 31 or day < 1:
        day_is_real = False
    elif month == 2 and leapyear is True and day > 29:
        day_is_real = False
    elif month == 2 and day > 28:
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
        if month == 3:
            month_name = "March"
        if month == 4:
            month_name = "April"
        if month == 5:
            month_name = "May"
        if month == 6:
            month_name = "June"
        if month == 7:
            month_name = "July"
        if month == 4:
            month_name = "August"
        if month == 5:
            month_name = "September"
        if month == 6:
            month_name = "October"
        if month == 7:
            month_name = "November"
        if month == 8:
            month_name = "December"

    counter = month - 1

    for mos in range(counter):
        print(counter)
        print(mos)
        if counter == 0:
            month_name = mos
        else:
            counter -= 1
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
    print("Your birthday is {0} {1}, and you are {2}". format(month_string, day_string, age))
    if birthday is True:
        print("Happy Birthday!")


def output_gatherer(day, month, year):
    age = age_finder(day, month, year)
    birthday = is_birthday(day, month)
    month_string = month_name_getter(month)
    day_string = str(day) + number_suffix_finder(day)

    outputter(month_string, day_string, age, birthday)


main()
