
room0items = [] #room does not exist but list is needed for index purposes
room1items = ['fishing rod']
room2items = []
room3items = ['lantern']
room4items = ['leaflet']
room5items = ['diary']
room6items = []
room7items = []
room8items = []
room9items = []
room10items = ['skeleton']
room11items = ['Jade Statue']
room12items = ['crowbar']

allItems = [room0items, room1items, room2items, room3items, room4items, room5items, room6items, room7items, room8items, room9items, room10items, room11items, room12items]

# Returns item to be added to inventory if it exists in this room and removes it from the list of items in the coom
def pick_up(itemName, roomNum):
    if itemName in allItems[roomNum]:
        allItems[roomNum].remove(itemName)
        return itemName
    else:
        print("Not a valid item to pick up")
        

# Puts the item down in the current room, adds it to the item list of the current room, 
# and returns 0 to indicate that it was successfully removed.
def put_down(itemName, roomNum):
    print("You put down the ", itemName)
    allItems[roomNum].append(itemName)
    return 0

def useItem(itemName, itemlist):
    if itemName in itemlist:
        print('You use the', itemName)
        return True
    else:
        return False