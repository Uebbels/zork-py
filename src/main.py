# Main game file

import zork

life = True
room = 4
print("---------------------------------------------------------")
print("Welcome to Zork - The Unofficial Python Version.")
itemlist = []

while life:
    if room == 1:
        print("---------------------------------------------------------")
        print("You find yourself at the edge of a beautiful lake aside rolling hills.")
        print("A small pier juts out into the lake.")
        print("A fishing rod rests on the pier.")
        print("(You can see a white house in the distance to the south.)")
        print('To the west lies an old boathouse.')
        action = input("What do you do? ")
        outcome = zork.room1(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    elif room == 2:
        print("---------------------------------------------------------")
        print("You find yourself at the back of the house.")
        print('There is a rickety window to the west.')
        print('The field lies to the south.')
        action = input("What do you do? ")
        outcome = zork.room2(action, itemlist)
        room = outcome[0]
        life = outcome[1]
    
    elif room == 3:
        print("---------------------------------------------------------")
        print("You find yourself in a dimly lit kitchen with dust covering the floor.")
        print('A lantern rests on the kitchen island.')
        print('A set of stairs leads up to another room.')
        action = input("What do you do? ")
        outcome = zork.room3(action, itemlist)
        room = outcome[0]
        life = outcome[1]
    
    elif room == 4:
        print("---------------------------------------------------------")
        print("You are standing in an open field west of a white house, with a boarded front door.")
        print("You can see a small lake to the north.")
        print("(A secret path leads southwest into the forest.)")
        print("There is a Small Mailbox.")
        action = input("What do you do? ")
        outcome = zork.room4(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    elif room == 5:
        print("---------------------------------------------------------")
        print("You find yourself in a dingy attic, filled with dusty boxes.")
        print("A window shows a clearing deep in the forest.")
        print("The floor creaks as you walk across it.")
        action = input("What do you do? ")
        outcome = zork.room5(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    elif room == 6:
        print("---------------------------------------------------------")
        print("You are at a dimly lit stone arch.")
        print("Through the arch, to the south, appears to be a maze of some sort.")
        print("On the arch , a single word is etched.")
        print('"BEWARE"')
        action = input("What do you do? ")
        outcome = zork.room6(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    elif room == 7:
        print("---------------------------------------------------------")
        print('Just a few steps into the maze, and you cannot see a thing.')
        action = input("What do you do? ")
        outcome = zork.room7(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    elif room == 8:
        print("---------------------------------------------------------")
        print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
        action = input("What do you do? ")
        outcome = zork.room8(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    elif room == 9:
        print("---------------------------------------------------------")
        print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
        print("There is an open grating, descending into darkness.")
        action = input("What do you do? ")
        outcome = zork.room9(action, itemlist)
        room = outcome[0]
        life = outcome[1]
    
    elif room == 10:
        print("---------------------------------------------------------")
        print("You are in a tiny cave with a dark, forbidding staircase leading down.")
        print("There is a skeleton of a human male in one corner.")
        print('There is a crack in the cave wall to the south you might be able to squeze through')
        action = input("What do you do? ")
        outcome = zork.room10(action, itemlist)
        room = outcome[0]
        life = outcome[1]
    
    elif room == 11:
        print("---------------------------------------------------------")
        print("You have entered a mud-floored room.")
        print("Lying half buried in the mud is an old trunk, bulging with jewels.")
        action = input("What do you do? ")
        outcome = zork.room11(action, itemlist)
        room = outcome[0]
        life = outcome[1]
    
    elif room == 12:
        print("---------------------------------------------------------")
        print("You enter the old boathouse.")
        print("There are no boats here, but there is an old workbench in the corner.")
        print("A variety a tools are on the workbench.")
        action = input("What do you do? ")
        outcome = zork.room12(action, itemlist)
        room = outcome[0]
        life = outcome[1]

    else:
        print('THIS IS AN ERROR! ROOM %s NOT DEFINED' % room)
        room = int(input('please choose room number'))
