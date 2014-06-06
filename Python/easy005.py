#!/usr/bin/python
"""
Your challenge for today is to create a program which is password protected, and wont open unless the correct user and password is given.
For extra credit, have the user and password in a seperate .txt file.
for even more extra credit, break into your own program :)
[MAIN]: DONE
[EXTRA]: DONE
[EXTRAEXTRA]: DONE
"""
from md5 import md5
from getpass import getpass

password_hashes = {}

with open('easy005.txt', 'r') as file:
    for line in file:
        stored_name, stored_hash = line.split(',')[0], line.split(',')[1]
        password_hashes[stored_name] = stored_hash

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

if __name__ == "__main__":
    while True:
        u,p = get_user_info()
        unlock(u,p)

#########BACKDOOR############
def crack():
    with open('/usr/share/dict/american-english') as f:                                                                                                                                                                                                     
        lines = f.read().splitlines()                                                                                                                                                                                                                       
        for l in lines:                                                                                                                                                                                                                                     
            if md5(l).hexdigest() == password_hashes['admin']:
                print "PASSWORD IS: ", l                                                                                                                                                                                                            
