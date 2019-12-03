# Main game file

import zork

life = True
room = 4

while life:
    print("---------------------------------------------------------")
    print("Welcome to Zork - The Unofficial Python Version.")
    if room == 1:
        print("---------------------------------------------------------")
        print("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print("A small pier juts out into the lake.")
        print("A fishing rod rests on the pier.")
        print("(You can see a white house in the distance to the south.)")
        action = input("What do you do? ")
        outcome = zork.room1(action)
        room = outcome[0]
        life = outcome[1]

    elif room == 4:
        print("---------------------------------------------------------")
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        action = input("What do you do? ")
        outcome = zork.room4(action)
        room = outcome[0]
        life = outcome[1]
        
    else:
        print('THIS IS AN ERROR! ROOM %s NOT DEFINED' % room)
        room = int(input('please choose room number'))