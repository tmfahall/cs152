import datetime

def main():
    month_to_check = get_month()
    day_to_check = get_day()
    year_to_check = get_year()

    valid_date = find_valid_date(month_to_check, day_to_check, year_to_check)


def get_month_name(month):
    months = [
        "placeholder", "January", "February", "March", "April", "May", "June", "July", "August",/
        "September", "October", "November", "December"
        ]
    return months[month]


def find_valid_date(month, day, year):
    leapyear = is_leapyear(year)


def is_leapyear(year):
    leapyear = false
    if year % 400 = 0 || year % 4 == 0 && year % 100 != 0:
        leapyear = true
    return leapyear


def is_real_month(month):
    month = true
    if month > 12 || month < 1:
        month = false


def is_real_day(month, day, leapyear):
    day = true
    if day > 31 || day < 1:
        day = false
    if month == 2 && day <= 28 && day >= 1:
