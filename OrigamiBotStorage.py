# -*- coding: utf-8 -*-
"""
Room#3: Storage for Origami Bots.
"""

import Item as I
import utils
import OutdoorsSouth
import oriBot as o
import text as T
import os

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
origamiBot = o.oriBot()

itemdictionary = { # [Item, isLocked]
  'origamibot': [origamiBot, None]
}

def basicDes():
    T.OrigamiBotStorage.basicDes()
    if not utils.inInventory("origamiBot"):
      print("A single origamiBot sits out on a table.")
         
def fancyDes():
    T.OrigamiBotStorage.fancyDes()
    if not utils.inInventory("origamiBot"):
      print("A single origamiBot sits out on a table.")

def movewest():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.x = utils.x + 1
    utils.roomsvisited[6] = 1 
    if not utils.advanced:
      OutdoorsSouth.basicDes()
    else:
      OutdoorsSouth.fancyDes()

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    print("Woops! Can't go that way!")

def moveeast():
    print("Woops! Can't go that way!")

def itemsInhere():
    itemlist = []
    for each in itemdictionary.keys():
        itemlist.append(each)
    return itemlist

def itemsInInventory():
    inventorylist = [] 
    for each in utils.inventory.keys():
      inventorylist.append(each)
    return inventorylist
    
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
    lst2 = itemsInInventory()
    #print(lst2)
    if obj in lst and obj not in lst2:
        itemdictionary[obj][0].use()
    elif obj in lst2 and obj not in lst:
        where = utils.inventory[obj]
        __import__(where).use(obj)
    elif obj in lst and obj in lst2:
        itemdictionary[obj][0].use()
    else:
        print("Hmm... {} can't use an object that's not in this room! You can check your inventory to look for items to use".format(obj))
 
def take(obj):
    lst = itemsInhere()
    if obj in lst:
        itemdictionary[obj][0].take(filename)
    else:
        print("Hmm... {} can't be taken out of this room!".format(obj))