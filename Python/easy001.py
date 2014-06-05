#!/usr/bin/python
"""
Create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
your name is (blank), you are (blank) years old, and your username is (blank)
EXTRA CREDIT: Have the program log this information in a file to be accessed later.
[MAIN] : DONE
[EXTRA]: DONE
"""
fields = ['name', 'age', 'reddit username']
answers = []

def get_info(field):
    return raw_input("What is your %s? : " % field)


for f in fields:
    answers.append(get_info(f))

with open("userlog.txt", 'w') as f:
    f.write(','.join(answers))
    
for q, a in zip(fields, answers):
    print "Your {0} is {1}.".format(q, a)
