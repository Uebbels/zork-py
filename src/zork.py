import items

def room1(inputstr, itemlist):	#lake
	life = True
	room = 1
	if inputstr.lower() == ("go south"):
		room = 4
	elif inputstr.lower() == ("swim"):
		print("---------------------------------------------------------")
		print("You don't have a change of clothes and you aren't here on vacation.")
	elif inputstr.lower() == ("fish"):
		print("---------------------------------------------------------")
		print("You spend some time fishing but nothing seems to bite.")
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		if dead_inp.lower() == ("y"):
			life = True
	else:
		print("---------------------------------------------------------")
	return [room, life]

def room2(inputstr, itemlist):	#Back of house
	life = True
	room = 2
	if inputstr.lower() == ("go west"):
		print("---------------------------------------------------------")
		print("You tryu and climb in a window, because the window is not implemented.")
	elif inputstr.lower() == ("go south"):
		room = 3
	elif inputstr.lower() == ("cook"):
		print("---------------------------------------------------------")
		print("You never bothered to learn and don't want to burn the house down.")
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		if dead_inp.lower() == ("y"):
			life = True
	else:
		print("---------------------------------------------------------")
	return [room, life]


def room4(inputstr, itemlist):
	life = True
	room = 4
	if inputstr.lower() == ("take mailbox"):
		print("---------------------------------------------------------")
		print("It is securely anchored.")
	elif inputstr.lower() == ("open mailbox"):
		print("---------------------------------------------------------")
		print("Opening the small mailbox reveals a leaflet.")
	elif inputstr.lower() == ("go north"):
		room = 1
	elif inputstr.lower() == ("go west"):
		room = 2
	elif inputstr.lower() == ("look at house"):
		print("---------------------------------------------------------")
		print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
	elif inputstr.lower() == ("go southwest"):
		room = 8
	elif inputstr.lower() == ("read leaflet"):
		print("---------------------------------------------------------")
		print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		elif dead_inp.lower() == ("y"):
			life = True
	else:
		print("---------------------------------------------------------")
	return [room, life]

def room8(inputstr, itemlist):	#Forest
	life = True
	room = 8
	if inputstr.lower() == ("go west"):
		print("---------------------------------------------------------")
		print("You would need a machete to go further west.")
	elif inputstr.lower() == ("go north"):
		print("---------------------------------------------------------")
		print("The forest becomes impenetrable to the North.")
	elif inputstr.lower() == ("go south"):
		print("---------------------------------------------------------")
		print("Storm-tossed trees block your way.")
	elif inputstr.lower() == ("go east"):
		room = 9
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		if dead_inp.lower() == ("y"):
			life = True
	else:
		print("---------------------------------------------------------")
	return [room, life]
		
def room9(inputstr, itemlist):
	life = True
	room = 9
	if inputstr.lower() == ("go south"):
		print("---------------------------------------------------------")
		print("You see a large ogre and turn around.")
	elif inputstr.lower() == ("descend grating"):
		room = 10
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		if dead_inp.lower() == ("y"):
			life = True
	else:
		print("---------------------------------------------------------")	
	return [room, life]

def room10(inputstr, itemlist):
	life = True
	room = 10
	if inputstr.lower() == ("descend staircase"):
		room = 11
	elif inputstr.lower() == ("take skeleton"):
		print("---------------------------------------------------------")
		print("Why would you do that? Are you some sort of sicko?")
	elif inputstr.lower() == ("smash skeleton"):
		print("---------------------------------------------------------")
		print("Sick person. Have some respect mate.")
	elif inputstr.lower() == ("light up room"):
		print("---------------------------------------------------------")
		print("You would need a torch or lamp to do that.")
	elif inputstr.lower() == ("break skeleton"):
		print("---------------------------------------------------------")
		print("I have two questions: Why and With What?")
	elif inputstr.lower() == ("go down staircase"):
		loop = 11
	elif inputstr.lower() == ("scale staircase"):
		loop = 11
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		if dead_inp.lower() == ("y"):
			life = True
	elif inputstr.lower() == ("scale staircase"):
		loop = 11
	else:
		print("---------------------------------------------------------")
	return [room, life]

def room11(inputstr, itemlist):
	life = True
	room = 11
	if inputstr.lower() == ("open trunk"):
		print("---------------------------------------------------------")
		print("You have found the Jade Statue and have completed your quest!")
		exit_inp = input("Do you want to continue? Y/N ")
		if exit_inp.lower() == ("n"):
			life = False
		if exit_inp.lower() == ("y"):
			life = True
	elif inputstr.lower() == ("kick the bucket"):
		print("---------------------------------------------------------")
		print("You die.")
		print("---------------------------------------------------------")
		dead_inp = input("Do you want to continue? Y/N ")
		if dead_inp.lower() == ("n"):
			life = False
		if dead_inp.lower() == ("y"):
			life = True
	else:
		print("---------------------------------------------------------")
	
	return [room, life]
