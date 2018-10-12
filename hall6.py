Author: Andrew Hall
Date: 10/17/2018
Class: CSIS 152
Instructor: Dr. Brekke
Assignment: Program 6

def main():
    loan_amount = get_loan_amount()
    loan_apr = get_loan_apr()
    loan_length = get_loan_length()

    monthly_payment = find_monthly_payment(loan_amount, loan_apr, loan_length)

    loan_summary_as_dictionary = find_loan_summary(loan_amount, loan_apr, loan_length, monthly_payment)

    output_looper(loan_summary_as_dictionary)

    payment_schedule_as_tuple = find_payment_schedule_as_tuple(loan_summary_as_dictionary)

    output_looper(payment_schedule_as_tuple)


def get_loan_amount():
    loan_amount = input("Enter amount of loan: ")
    return loan_amount


def get_loan_apr():
    loan_apr = input("Enter APR (5% entered as 0.05): ")
    return loan_apr


def get_loan_length():
    loan_length = input("Enter length of loan in years: ")
    return loan_length


def find_monthly_payment(amount, apr, length):
    number_of_payments = length * 12
    periodic_interest_rate = apr / number_of_payments
    discount_factor_top = (((1 + periodic_interest_rate)^number_of_payments)-1)
    discount_factor_bottom = (i * (1 + periodic_interest_rate)^number_of_payments)
    discount_factor = discount_factor_top / discount_factor_bottom
    payment = amount / discount_factor
    return payment


def find_loan_summary(amount, apr, length, payment):
    length_as_months = length * 12
    total_paid = payment * length_as_months
    total_interest = total_paid - amount

    loan_summary = {
            "loan amount": amount,
            "payment": payment,
            "months": length_as_months,
            "interest paid": apr,
            "total paid": total_paid,
            "total interest": total_interest
            }

    return loan_summary



