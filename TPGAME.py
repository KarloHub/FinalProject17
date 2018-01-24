import time
import sys
#give actions for player to use
def_actions = "You can: look around | flashlight (default on, toggle by typing flashlight)| search | :"


def startMenu():
        print("Welcome to Cave Explorer. You are a famous archaelogist looking for the a long lost treasure from the Spanish Inquisition. \n Your search has lead you to an uncharted cave in the region where the desert ends and jungle meets. Start your adventure? \n")
        decision = input("y/n:")
        if(decision == "n"):
              print("No. Play.")
        elif(decision == "y"):
            print("You descend down into the depths...\n");
            for x in range (0, 12):
                print("   |   ")
                time.sleep(0.5)
            print("______________")

def printActions():
        print("You can: look around | flashlight (default on, toggle by typing flashlight)| search | :")


def fifthCave():
        leave = False
        print("You come out into a large hallway with high ceilings. Above, stalactites shimmer with water.")
        while(leave != True):
            choice = input(def_actions)
            if(choice == "look around"):
                for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                print("Not much to see. Only one way to go, which is forward. Advance?")
                choice2 = input("y/n: ")
                if(choice2 == "y"):
                    print("You advance into the next room.")
                    return 0
            if(choice == "search"):
                for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                print("There is a large diamond embedded in the wall. Try to pry it out?")
                choice3 = input("y/n: ")
                if (choice3 == "y"):
                    print("You try to pry the diamond out of the wall, but as you do the floor beneath you opens up and you fall into an endless hole. Try again?")
                    choice4 = input("y/n: ")
                    if(choice4 == "y"):
                        main();
                    else:
                        return 0
            if(choice == "flashlight"):
                print("You try turning off your flashlight, and something glints in the darkness on the wall. Maybe it warrants closer inspection?")

def fourthCave():
        leave = False;
        key = False;
        print("This third cave has a single exit on the other end of a rushing stream.")
        while(leave != True):
                choice = input(def_actions)
                if (choice == "search" and key == False):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("You search around in the dirt and find a small, metal key.")
                        key = True
                elif (choice == "search" and key == True):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("You search around in the dirt, but there is nothing else of value.")
                        key = True
                if (choice == "look around"):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("You inspect the stream and find it is too deep and too fast to cross safely. You must find another way across.")
                if (choice == "flashlight"):
                        print("You find a small metal hole in the wall glinting from after you turn off your flashlight.")
                        if(key == True):
                            print("You insert the key into the hole, and a bridge appears. You cross and enter into the next room.")
                            print(" _ \n  _ \n   _ \n    _\n     _ \n")
                            return 0
                        else:
                            print("Looks like you need a key.")

def thirdCave():
        leave = False
        print("The next room is filled with crystals, and the light from your flashlight bounces off the walls. There is no discernable exit.")
        while(leave != True):
                choice = input(def_actions)
                if (choice == "search"):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("You pick up a small crystal from the floor, hoping it will be worth something later.")
                if (choice == "look around"):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("Looking around, there are even crystals on the ceiling.")
                if (choice == "flashlight"):
                        print("You turn off your flashlight, and the crystals glow faintly, until suddenly the glow from the crystals reveals a hidden path. Go down the path?")
                        choice2 = input("y/n :")
                        if (choice2 == "y"):
                                print(" _ \n  _ \n   _ \n    _\n     _ \n")
                                return 0

def secondCave():
        leave = False
        machete = False
        print("You stand in a very dark room, and the only light is from your flashlight. Now there is only one exit.")
        print("What will you do?")
        while(leave != True):
               choice = input(def_actions)
               if (choice == "search"):
                       for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                       print("You find an old machete on the ground, covered in dirt. You pick it up and put it into your belt.")
                       machete = True
               if (choice == "look around" and machete != True):
                       for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                       print("By looking closer, you determine that the pathway is blocked with spiderwebs. It is impossible to pass.")
               if (choice == "look around" and machete == True):
                       for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                       print("You use the machete to cut down the spiderwebs, advancing into the next room.")
                       print(" _ \n  _ \n   _ \n    _\n     _ \n")
                       return 0;
               if (choice == "flashlight"):
                       print("The room turns pitch black, and you can't even see your own two hands in front of your face. You decide that keeping the flashlight on is probably a better idea.")






def startingCave():
        leave = False
        leave2 = False
        print("You are in a small cave. Water drips from the ceiling. There are three openings.")
        while(leave != True):
                choice = input(def_actions)

                if (choice.lower() == "look around"):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("There are three paths in front of you. You can hear a faint wind blowing from the middle path.\n The left path is totally silent, and the right path is suspiciously dark. \n What will you do?")
                        leave2 = False
                        while(leave2 != True):
                                choice2 = input("left | right | middle | stay |")
                                if(choice2 == "left"):
                                        print("You begin to walk down the path, but the ground suddenly opens up beneath you and you fall to your death. \n Try again?")
                                        choice3 = input("y/n :")
                                        if(choice3 == "y"):
                                                main();
                                        elif(choice3 == "n"):
                                                return 0;
                                        else:
                                                return 0;
                                if(choice2 == "right"):
                                        print("You step into path, but find that it comes quickly to a dead end, and you return to the original room.")
                                        leave2 = True
                                if(choice2 == "middle"):
                                        print("you walk down the middle path, and find yourself in another cave.")
                                        print(" _ \n  _ \n   _ \n    _\n     _ \n")
                                        return 0;
                                if(choice2 == "stay"):
                                        print("you choose to stay in the current room.")
                                        leave2 = True

                if (choice.lower() == "search"):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("nothing to be found of value on the ground or the walls.")

                if (choice.lower() == "flashlight"):
                        for x in range (0, 5):
                                print(".")
                                time.sleep(0.5)
                        print("There's no point turning the flashlight on and off in this room, as the light from the cave opening already floods in.")

def finalCave():
        print("You stand in a very dark room, and the only light is from your flashlight. Now there is only one exit.")
        print("What will you do?")
        choice = input(def_actions)
        if (choice == "search"):
                for x in range (0, 5):
                    print(".")
                    time.sleep(0.5)
                    print("You find treasure on the ground! You win! Good job!")
                    time.sleep(5)
                    sys.exit()
        if (choice == "look around"):
                for x in range (0, 5):
                    print(".")
                    time.sleep(0.5)
                    print("No more paths to look for")
        if (choice == "flashlight"):
                print("Your flashlight doesn't work anymore!")

def main():
    startMenu();
    startingCave();
    secondCave();
    thirdCave();
    fourthCave();
    fifthCave();
    finalCave();
print(main())

