
print('How many years have you / will you be saving?')
years = int(input('Enter years: '))

print('How much money do you have in your account?')
principal = float(input('Enter the current amount in your account: '))

print('How much will you invest monthly?')
investment_month = float(input('Enter amount you will invest: '))

print('What will the average yearly interest be?')
interest = float(input('Enter the interest in decimal numbers (10% = 0.1: '))

print(' ')

investment_month = investment_month * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + investment_month) * (1 + interest)

print('After {} years, you will have: '.format(years) + str(final_amount))