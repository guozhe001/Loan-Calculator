# Stage 1/4 start
# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

# Stage 1/4 end
################################################################################################################
# Stage 2/4 start

# print("Enter the loan principal:")
# loan_principal = int(input())
# message = """
# What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:
# """
# print(message)
# model = input()
# if model == "m":
#     monthly_payment = int(input())
#     print("It will take %s months to repay the loan" % (loan_principal / monthly_payment))
# elif model == "p":
#     number_of_months = int(input())
#     if loan_principal % number_of_months == 0:
#         print("Your monthly payment = %s", loan_principal / number_of_months)
#     else:
#         month_repay = loan_principal // number_of_months + 1
#         last_payment = loan_principal - month_repay * number_of_months + month_repay
#         print("Your monthly payment = %s and the last payment = %s." % (month_repay, last_payment))

# Stage 2/4 end
################################################################################################################
# Stage 3/4 start
# import math
#
#
# def get_period(loan_principal, monthly_payment, monthly_interest):
#     log = math.log(monthly_payment / (monthly_payment - i * loan_principal), i + 1)
#     return math.ceil(log)
#
#
# def get_period_and_print(loan_principal, monthly_payment, monthly_interest):
#     period = get_period(loan_principal, monthly_payment, monthly_interest)
#     year = period // 12
#     month = int(period - year * 12)
#     print_period(year, month)
#
#
# def print_period(year, month):
#     print("It will take {}{}{} to repay this loan!".format(f"{year} years" if year > 0 else "",
#                                                            " and " if year > 0 and month > 0 else "",
#                                                            f"{month} months" if month > 0 else ""))
#
#
# def get_loan_principal(monthly_payment, period, i):
#     return round(monthly_payment / ((i * math.pow(1 + i, period)) / (math.pow(1 + i, period) - 1)))
#
#
# message = """
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# """
# print(message)
# model = input()
# loan_principal = 0
# monthly_payment = 0
# period = 0
#
# if model != "p":
#     print("Enter the loan principal:")
#     loan_principal = float(input())
#
# if model != "a":
#     print("Enter the monthly payment:")
#     monthly_payment = float(input())
#
# if model != "n":
#     print("Enter the number of periods:")
#     period = float(input())
#
# print("Enter the loan interest:")
# interest = float(input())
# i = interest / (12 * 100)
#
# if model == "n":
#     get_period_and_print(loan_principal, monthly_payment, i)
# elif model == "a":
#     monthly_payment = math.ceil(loan_principal * ((i * math.pow(1 + i, period)) / (math.pow(1 + i, period) - 1)))
#     print(f"Your monthly payment = {monthly_payment}!")
# elif model == "p":
#     loan_principal = get_loan_principal(monthly_payment, period, i)
#     print(f"Your loan principal = {loan_principal}!")

# Stage 3/4 end
################################################################################################################
# Stage 4/4 start
import argparse
import math


# 验证入参的个数，如果不符合预期的个数则打印异常
def args_validation(args):
    count = 0
    for a in args:
        if a:
            count += 1
    return count


# 打印错误信息如果参数输入不正确
def print_incorrect():
    print("Incorrect parameters")


# 定义入参
def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", help="Calculation of differentiated payments", required=True)
    parser.add_argument("-p", "--principal", help="the loan principal", type=float)
    parser.add_argument("-n", "--periods", help="number of payments", type=int)
    parser.add_argument("-i", "--interest", help="annual interest rate", type=float)
    parser.add_argument("--payment", help="the monthly payment amount", type=float)
    return parser.parse_args()


# 判断不包含负值，如果包含负值则返回False，不包含负值则返回True
def do_not_have_negative(periods, interest, principal, payment):
    if (periods and periods < 0) or (interest and interest < 0) or (principal and principal < 0) or (
            payment and payment < 0):
        print_incorrect()
        return False
    return True


def get_period(loan_principal, monthly_payment, i):
    log = math.log(monthly_payment / (monthly_payment - i * loan_principal), i + 1)
    return math.ceil(log)


def print_period(year, month):
    print("It will take {}{}{} to repay this loan!".format(f"{year} years" if year > 0 else "",
                                                           " and " if year > 0 and month > 0 else "",
                                                           f"{month} months" if month > 0 else ""))


def get_period_and_print(loan_principal, monthly_payment, monthly_interest):
    period = get_period(loan_principal, monthly_payment, monthly_interest)
    year = period // 12
    month = int(period - year * 12)
    print_period(year, month)
    return period


def get_loan_principal(monthly_payment, period, i):
    return math.floor(monthly_payment / ((i * math.pow(1 + i, period)) / (math.pow(1 + i, period) - 1)))


# 等额本息
def annuity(periods, interest, principal, payment):
    if not periods:
        periods = get_period_and_print(principal, payment, interest)
    elif not payment:
        payment = math.ceil(
            principal * ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1)))
        print(f"Your annuity payment = {payment}!")
    elif not principal:
        principal = get_loan_principal(payment, periods, interest)
        print(f"Your loan principal = {principal}!")
    print("Overpayment = {}".format(round(periods * payment - principal)))


# 等额本金
def diff(n, i, p):
    all_payment = 0
    for m in range(1, n + 1):
        d = math.ceil(p / n + i * (p - (p * (m - 1) / n)))
        print(f"Month {m}: payment is {d}")
        all_payment += d
    print("Overpayment = {}".format(round(all_payment - p)))


args = define_args()
args_dict = vars(args)

if args_validation(args_dict) < 4 or not args.interest:
    print_incorrect()
else:
    periods = args.periods
    interest = args.interest
    principal = args.principal
    payment = args.payment
    if do_not_have_negative(periods, interest, principal, payment):
        monthly_interest = interest / (12 * 100)
        if args.type == "annuity":
            annuity(periods, monthly_interest, principal, payment)
        elif args.type == "diff":
            if payment:
                print_incorrect()
            else:
                diff(periods, monthly_interest, principal)
        else:
            print_incorrect()
    else:
        print_incorrect()
# Stage 4/4 end
