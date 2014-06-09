#!/usr/bin/python
"""
You're challenge for today is to create a program that can calculate pi accurately to at least 30 Decimal places.
[MAIN]: DONE
"""

# We will use the some weird arcsin taylor series that I took from the decimal package docs.
from decimal import *

def pi(precision):
    getcontext().prec = precision
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts = 0
    t = three
    s = 3
    n, na = 1, 0
    d, da = 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

def pi_one_line(): # As a bonus
    print reduce(lambda x,k:2+k/2*x/k,range(999,1,-2),Decimal())

print "Our approximation of pi:", pi(30) # Should evel to 3.14159265358979323846264338328

