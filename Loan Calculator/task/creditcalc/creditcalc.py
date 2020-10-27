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

# Stage 2/4 start
print("Enter the loan principal:")
loan_principal = int(input())
message = """
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
"""
print(message)
model = input()
if model == "m":
    monthly_payment = int(input())
    print("It will take %s months to repay the loan" % (loan_principal / monthly_payment))
elif model == "p":
    number_of_months = int(input())
    if loan_principal % number_of_months == 0:
        print("Your monthly payment = %s", loan_principal / number_of_months)
    else:
        month_repay = loan_principal // number_of_months + 1
        last_payment = loan_principal - month_repay * number_of_months + month_repay
        print("Your monthly payment = %s and the last payment = %s." % (month_repay, last_payment))

# Stage 2/4 end

str.isdigit()