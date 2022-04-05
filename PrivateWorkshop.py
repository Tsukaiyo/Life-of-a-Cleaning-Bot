# -*- coding: utf-8 -*-
"""
Room#1: Private Workshop
"""
import Item as I
import utils
import CleaningBotStorage

#print("You're in the Private Workshop.")

utils.roomsvisited[0] = 1

## Items in Room
##################

#name, canTake, inInventory, description, interactable, useText
#nullItem = I.Item("", False, False, "", False, "")
computer1 = I.Computer("computer", False, False, "A fairly modern PC. Some sticky notes line the edges of the monitor. A keyboard sits in front of it on the desk.", True, "")
keyboard = I.Item("keyboard", False, False, "A beat up old keyboard. There's a note sitcking out from under it.", True, "A beat up old keyboard. There's a note sitcking out from under it.",)
note = I.Item("note", True, False, "It reads: 'If I forget again: Initials, year of birth, lucky number. No commas or spaces. PS: create a better password.'", True, "It reads: 'If I forget again: Initials Birth year Lucky number, no spaces. PS: create a better password.'")
trash = I.Item("trash", False, False, "Inside the bin, there is a piece of paper.", True, "I could take the paper out of it")
trash = I.Item("trash", False, False, "Inside the bin, there is a piece of paper.", True, "I could take the paper out of it")
paper = I.Item("paper", False, False, "It reads:\nApril 20, 2020. \nHead of Robotics at The National Institute for Mechanical Innovation, Cordelia Weaver, has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.", True, "It reads:\nApril 20, 2020. \nHead of Robotics at The National Institute for Mechanical Innovation, Cordelia Weaver, has been awarded for remarkable contribution to science for her creation of a highly adaptable cleaning robot. At the age of 28, she is one of the youngest scientists to ever achieve such an acomplishment. We're excited to see what she does next.")
terminal1 = I.Terminal(1)

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , False],
   'computer': [computer1 , False ],
   'keyboard': [keyboard  , None ],               
   'note':     [note      , None ],
   'trash':    [trash     , None ],
  'paper':     [paper     , None ],
  'terminal':  [terminal1     , None ]
}

def basicDes():
    print("A small room with a computer on a desk. Next to the desk is a trash bin. There is a door to the West, and a terminal beside it.")

def fancyDes():
    print("A small room with a computer on a desk. Next to the desk is a trash bin. There is a door to the West, and a terminal beside it.")

def movewest():
    if utils.cheat == True or terminal1.locked == False:
      utils.x = utils.x + 1
      CleaningBotStorage.basicDes()
    else:
      print("The door is locked.")
    if utils.x < 0:
        utils.x = 0
    if utils.y < 0:
        utils.y = 0
    #print("You're moving to Cleaning Bot Storage", utils.x, utils.y)

def movenorth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def movesouth():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def moveeast():
    #print(utils.x, utils.y)
    print("Woops! Can't go that way!")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def listItems():
    lst = itemsInhere()
    for each in lst:
        print(each)
    
def examine(obj):
    lst = itemsInhere()
    #print(obj)
    if obj in lst:
        if itemdictionary[obj][1] == True or itemdictionary[obj][1] == None:
            itemdictionary[obj][0].examine()
    else:
        print("Hmm... {} doesn't seem to be in this room!".format(obj))

def use(obj):
    lst = itemsInhere()
    if obj in lst:
        if itemdictionary[obj][1] == True:
            print("It's Locked!")
            #itemdictionary[obj][0].use()
        else:
            itemdictionary[obj][0].use()
    else:
        print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))
 
def take(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take()
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))

def unlock(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].unlock()
    else:
        print("Hmm... {} cannot be unlocked!".format(obj))

def removeInventory(obj):
    lst = itemsInhere()
    if obj in lst:
        (utils.inventory).remove(obj)
    else:
        print("Hmm... {} is not in inventory!".format(obj))