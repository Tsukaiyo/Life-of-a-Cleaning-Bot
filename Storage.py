# -*- coding: utf-8 -*-
"""
Room#7: Storage room
"""
import Item as I
import utils
import Hallway6
import text as T
import os
import room

filename = (os.path.basename(__file__))
filename = filename.replace(".py", "")

## Items in Room
##################
#name, canTake, inInventory, description, interactable, useText
hat = I.Item("hat", True, False, "A lovely red hat.", True, "I put on the hat")
coat = I.Item("coat", True, False, "A light spring coat.", True, "I pull on the coat")

itemdictionary = { # [Item, isLocked]
#   'nullItem': [nullItem  , None],
  'hat':  [hat , None ],
  'coat':  [coat, None]
}

def basicDes():
    T.Storage.basicDes()
         
def fancyDes():
    T.Storage.fancyDes()

def movewest():
    print("Woops! Can't go that way!")

def movenorth():
    print("Woops! Can't go that way!")

def movesouth():
    os.system('cls' if os.name == 'nt' else 'clear')
    utils.y = utils.y + 1
    if not utils.advanced:
        Hallway6.basicDes()
    else:
        Hallway6.fancyDes()
  
def moveeast():
    print("Woops! Can't go that way!")

def listItems():
    print(itemdictionary.keys())
    
def examine(obj):
    room.examine(obj, itemdictionary)

def use(obj):
    room.use(obj, itemdictionary)
 
def take(obj):
    room.take(obj, itemdictionary, filename)
