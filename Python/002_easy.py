#!/usr/bin/python
"""
Create a calculator application that has use in your life.
It might be an interest calculator, or it might be something that you can use in the classroom.
For example, if you were in physics class, you might want to make a F = M * A calc.
EXTRA CREDIT: make the calculator have multiple functions! Not only should it be able to calculate F = M * A, but also A = F/M, and M = F/A!
[MAIN] : DONE
[EXTRA]: DONE
"""
# Constants (edit for real values)
FIXED_PRICE = 1.50
INITIAL_VALUE = 3000
SHARES = INITIAL_VALUE // FIXED_PRICE

def get_current_capital(shares):
    price = input("Enter today's share price: ")
    return shares * price

def get_desired_price(shares):
    capital = input("Enter desired capital: ")
    return float(capital) / shares

def mode():
    mode = raw_input("Select function (v)alue, (p)rice, (e)xit: ")
    if mode == 'v':
        value = get_current_capital(SHARES)
        print "The value of your shares is", value
    elif mode == 'p':
        price = get_desired_price(SHARES)
        print "The price you need is", price
    elif mode == 'e':
        exit()
    else:
        pass

while True:
    mode()