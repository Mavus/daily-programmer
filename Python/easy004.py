#!/usr/bin/python
"""
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
[MAIN]: DONE
[EXTRA]: TODO
[EXTRAEXTRA]: TODO
"""
from random import randint

def generate_password(length=16):
    random_characters = map(chr,[randint(33,127) for i in range(length+1)])
    return ''.join(random_characters)

print generate_password()