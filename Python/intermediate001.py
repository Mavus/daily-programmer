#!/usr/bin/python
"""
Create a menu driven program
Using the menu drive program allow a user to add/delete items
The menu should be based on an events calender where users enter the events by hour
No events should be hard-coded.
[MAIN] : TODO
"""
schedule = {}

class Event:
    def __init__(self,time,name,description):
        self.time = time
        self.name = name
        self.description = description
    
def create_event():
    try:
        time = int(input("Please enter the event time: "))
    except ValueError:
        print "Please enter a time in the format 0900"
        return
    if time in schedule:
        print "There is already an even at ", time
        return
    name = input("Enter and event name: ")
    description = input("Enter a short description of the event: ")
    schedule[time] = Event(time,name,description)

def list_events():
    pass

def edit_event():
    pass

def delete_event():
    pass

def show_menu():
    pass