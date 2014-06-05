#!/usr/bin/python
"""
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)
[MAIN]: DONE
[EXTRA]: TODO
[EXTRAEXTRA]: TODO
"""
from md5 import md5
from getpass import getpass

assword_hashes = {'admin': 'e4b48fd541b3dcb99cababc87c2ee88f'}

def get_user_info():
    user = raw_input("Username: ")
    password = getpass("Enter the secure password: ")
    return user, password

def unlock(user, password):
    hash_obj = md5(password)
    try:
        if hash_obj.hexdigest() == password_hashes[user]:
            print "ACCESS GRANTED"
            exit()
    except KeyError:
        print "User doesn't exist"
    else:
        print "ACCESS DENIED"

while True:
    u,p = get_user_info()
    unlock(u,p)