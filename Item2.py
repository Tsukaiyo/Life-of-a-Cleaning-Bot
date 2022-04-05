import random
import utils 

#Inventory = []
# class Computer:
#     birth_year = 1988
#     initials = 'sample'  #change initials to what you want
#     lucky_num = random.randint(000,999)

class Workshop:
    def item_add():
        item = ['NFC key', random.randint(0000,9999)]
        #visited = False
        if item in utils.inventory:
            #visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print(f"Added {item} to inventory.")
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
                
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory.append(item)
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")

class Main_Building:
    def item_add():
        item = 'broom'
        #visited = False
        if item in utils.inventory:
            #visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print(f"Added {item} to inventory.")
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory.append(item)
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")


class Construc_Headoff:
    def item_add():
        item = "Head of Construction's Key Card"
        #visited = False
        if item in utils.inventory:
            #visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print(f"Added {item} to inventory.")
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory.append(item)
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")

class CreatorOffice:
    def item_add():
        pass
    
    def GPS():
        print("Description about meeting her Creator.")
        print("Interaction with Creator before turning off GPS.")
        utils.GPS = False
      
class StorageCloset:
    def item_add():
        pass
    
    def disguise():
        print("Description about disguising.")
        utils.disgsuise = False

class Origami_Office:
    def item_add():
        item = "OrigamiKey"
        #visited = False
        if item in utils.inventory:
            #visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print(f"Added {item} to inventory.")
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory.append(item)
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")

class PrototypeWorkshop:
    def item_add():
        item = "copperwire"
        #utils.roomsvisited[23] = 1
        if item in utils.inventory:
            #visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print("Added {} to inventory.".format(item))
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print("You refused to take the {}.".format(item))
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print("Added {} to inventory.".format(item))
                        utils.inventory.append(item)
                        x = 1
                    elif (value == 'N') or (value == 'n'):
                        print("You refused to take the {}.".format(item))
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")    

class Obstacle_Course:
    def item_add():
        item = "ScrewDriver"
        visited = False
        if visited == False:
            visited = True
            
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print(f"Added {item} to inventory.")
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory.append(item)
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")


class Lost_Found:
    def item_add():
        item = "Clothes"
        visited = False
        if visited == False:
            visited = True
            x = 0
            while x == 0:
                value = input("There's something here... Wanna pick it up? Y/N\n")
                if (value == 'Y') or (value == 'y'):
                    print(f"Added {item} to inventory.")
                    utils.inventory.append(item)
                    x = 1
                elif (value == 'N') or (value == 'n'):
                    print(f"You refused to take the object.")
                    x = 1
                else:
                    print("Error, invalid input... Type Y/N")
                    continue
        else:
            if (item not in utils.inventory):
                x = 0
                while x == 0:
                    value = input(f"{item} is still in this room... Wanna pick it up? Y/N\n")
                    if (value == 'Y') or (value == 'y'):
                        print(f"Added {item} to inventory.")
                        utils.inventory.append(item)
                        x = 1.
                    elif (value == 'N') or (value == 'n'):
                        print(f"You refused to take the object.")
                        x = 1
                    else:
                        print("Error, invalid input... Type Y/N")
                        continue
            else:
                print("There's nothing here... Keep walking")


class Check_Inventory:
    def check():
        print(utils.inventory)