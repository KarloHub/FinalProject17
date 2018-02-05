import sys,time,random
from random import randint

count = 0
typing_speed = 50 #wpm
#function that will make a print-like function that types slow
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*1/typing_speed)
#fuction for character's actions
def_actions = "\nWhat would you like to do?\na)|  Clean |\nb)|  Move  |\nc)| Search |\nd)| Check Inventory |\n"

def printActions():
    print("\nWhat would you like to do?\na)| Clean |\nb)| Move  |\nc)| Search |\nd)| Potion |:")
#dictionaries for all characters in the game
Hero = {"name" : "Unknown", "Lvl" : 1, "TPP" : 0, "NextLvl" : 30, "Cln" : 0, "Sts" : {"MaxHP" : 40, "CurrHP" : 40, "StrLvl" : 1, "atk1" : [5, 10], "atk2" : [3, 15], "atk3" : [1, 20]}, "Inv" : {"kitchen key" : 0, "livingroom key" : 0, "masterbedroom key" : 0, "bathroom key" : 0, "smallbedroom key" : 0, "diningroom key" : 0, "gameroom key" : 0, "tide pod" : 0, "bleach potion" : 0}}

Mon1 = {"name" : "Gush Jr.", "Lvl" : 1, "TPP" : 0, "reward": 50, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 30, "CurrHP" : 30, "StrLvl" : 1, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
Mon2 = {"name" : "Gushton", "Lvl" : 3, "TPP" : 0, "reward": 100, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
Mon3 = {"name" : "Gush", "Lvl" : 4, "TPP" : 0, "reward": 200, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
Mon4 = {"name" : "Gushell", "Lvl" : 6, "TPP" : 0, "reward": 350, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
Mon5 = {"name" : "Gushpy", "Lvl" : 9, "TPP" : 0, "reward": 700, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
Mon6 = {"name" : "Gushdon", "Lvl" : 11, "TPP" : 0, "reward": 800, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
Mon7 = {"name" : "Gushas", "Lvl" : 12, "TPP" : 0, "reward": 900, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
KM = {"name" : "King Gush", "Lvl" : 15, "TPP" : 0, "reward": 1200, "key": 1, "NextLvl" : 30, "Sts" : {"MaxHP" : 50, "CurrHP" : 50, "StrLvl" : 2, "atk1" : [3, 5], "atk2" : [2, 8], "atk3" : [1, 15]}}
#creates dictionary for every room's cleanliness
ldry = {"tide pod" : 0}
groom = {"tide pod" : 0}
sbroom = {"tide pod" : 0}
livrm = {"tide pod" : 0}
bathrm = {"tide pod" : 0}
mbroom = {"tide pod" : 0}
dinrm = {"tide pod" : 0}
kitrm = {"tide pod" : 0}
#shos the stats of the character after something is defeated
Sts = {"MaxHP" : 40, "CurrHP" : 30, "StrLvl" : 1}
def line():
    print("\n-------------------------------------------------------")
def level(MC, Sts):
    nMaxHP, nCurrHP, nStrLvl = 0, 0, 0
    while MC["TPP"] >= MC["NextLvl"]:
        print("Nice! You levelled up!")
        MC["Lvl"] += 1
        MC["TPP"] = MC["TPP"] - MC["NextLvl"]
        MC["NextLvl"] = round(MC["NextLvl"] * 1.80)
        nMaxHP += 10
        nCurrHP += 10
        nStrLvl += 1
    print("level:", MC["Lvl"])
    line()
    print("Tide Pod Points:", MC["TPP"])
    line()
    print("Tide Pod Points until next level: {}".format(int(MC["NextLvl"] - MC["TPP"])))
    line()
    print("CURRENT HP: {} +{} MAX HP: {} +{} STRENGTH LEVEL: {} +{}".format(Sts["CurrHP"], nCurrHP, Sts["MaxHP"], nMaxHP, Sts["StrLvl"], nStrLvl))
    Sts["MaxHP"] += nMaxHP
    Sts["CurrHP"] += nCurrHP
    Sts["StrLvl"] += nStrLvl

#function that lets the character check their inventory
def chkInv():
    slow_type("\nGOD: What amount of what would you like to check in your inventory?")
    chk1 = input("\na)|   tide pods    |\nb)| bleach potions |\nc)|      keys      |\n").lower()
    if chk1 == "a" and Hero["Inv"]["tide pod"] == 0:
        slow_type("GOD: You have no tide pods. Shame.")
    if chk1 == "a" and Hero["Inv"]["tide pod"] == 1:
        slow_type("GOD: You have {} tide pod.".format(Hero["Inv"]["tide pod"]))
    if chk1 == "a" and Hero["Inv"]["tide pod"] > 1:
        slow_type("GOD: You have {} tide pods.".format(Hero["Inv"]["tide pod"]))
    if chk1 == "b" and Hero["Inv"]["bleach potion"] == 0:
        slow_type("GOD: You have no bleach potions. Shame.")
    if chk1 == "b" and Hero["Inv"]["bleach potion"] == 1:
        slow_type("GOD: You have {} bleach potion.".format(Hero["Inv"]["bleach potion"]))
    if chk1 == "b" and Hero["Inv"]["bleach potion"] > 1:
        slow_type("GOD: You have {} bleach potions.".format(Hero["Inv"]["bleach potion"]))
    if chk1 == "c":
        chk2 = input("GOD: And what key are you checking for?\na)|bath room|\nb)|game room|\nc)|living room|\nd)|small bedroom|\ne)|master bedroom|\nf)|dining room|\ng)|kitchen|\n").lower()
        if chk2 == "a" and Hero["Inv"]["bathroom key"] == 1:
            slow_type("GOD: You have the key to the bathroom.")
        if chk2 == "a" and Hero["Inv"]["bathroom key"] == 0:
            slow_type("GOD: You do not have the key to the bathroom.")
        if chk2 == "b" and Hero["Inv"]["gameroom key"] == 1:
            slow_type("GOD: You have the key to the game room.")
        if chk2 == "b" and Hero["Inv"]["gameroom key"] == 0:
            slow_type("GOD: You do not have the key to the game room.")
        if chk2 == "c" and Hero["Inv"]["livingroom key"] == 1:
            slow_type("GOD: You have the key to the living room.")
        if chk2 == "c" and Hero["Inv"]["livingroom key"] == 0:
            slow_type("GOD: You do not have the key to the living room.")
        if chk2 == "d" and Hero["Inv"]["smallbedroom key"] == 1:
            slow_type("GOD: You have the key to the small bedroom.")
        if chk2 == "d" and Hero["Inv"]["smallbedroom room key"] == 0:
            slow_type("GOD: You do not have the key to the small bedroom.")
        if chk2 == "e" and Hero["Inv"]["masterbedroom key"] == 1:
            slow_type("GOD: You have the key to the master bedroom.")
        if chk2 == "e" and Hero["Inv"]["masterbedroom key"] == 0:
            slow_type("GOD: You do not have the key to the master bedroom.")
        if chk2 == "f" and Hero["Inv"]["diningroom key"] == 1:
            slow_type("GOD: You have the key to the dining room.")
        if chk2 == "f" and Hero["Inv"]["diningroom key"] == 0:
            slow_type("GOD: You do not have the key to the dining room.")
        if chk2 == "g" and Hero["Inv"]["kitchen key"] == 1:
            slow_type("GOD: You have the key to the kitchen room.")
        if chk2 == "g" and Hero["Inv"]["kitchen key"] == 0:
            slow_type("GOD: You do not have the key to the kitchen room.")

#function thatdoes damage, attack function
def getHit1GR(attacker,defender):
    Hit = randint(attacker["Sts"]["atk1"][0], attacker["Sts"]["atk1"][1])
    defender["Sts"]["CurrHP"] = defender["Sts"]["CurrHP"] - Hit
    if (defender["Sts"]["CurrHP"] > 0):
        slow_type("\n{} has taken {} damage!".format(defender["name"], Hit))
        slow_type("\n{} is now at {} HP!".format(defender["name"], defender["Sts"]["CurrHP"]))

def getHit2GR(attacker,defender):
    Hit = randint(attacker["Sts"]["atk2"][0], attacker["Sts"]["atk2"][1])
    defender["Sts"]["CurrHP"] = defender["Sts"]["CurrHP"] - Hit
    if (defender["Sts"]["CurrHP"] > 0):
        slow_type("\n{} has taken {} damage!".format(defender["name"], Hit))
        slow_type("\n{} is now at {} HP!".format(defender["name"], defender["Sts"]["CurrHP"]))

def getHit3GR(attacker,defender):
    Hit = randint(attacker["Sts"]["atk3"][0], attacker["Sts"]["atk3"][1])
    defender["Sts"]["CurrHP"] = defender["Sts"]["CurrHP"] - Hit
    if (defender["Sts"]["CurrHP"] > 0):
        slow_type("\n{} has taken {} damage!".format(defender["name"], Hit))
        slow_type("\n{} is now at {} HP!".format(defender["name"], defender["Sts"]["CurrHP"]))

#function that heals character when a potion is used
def usepotion(attacker):
    new_hp = attacker["Sts"]["CurrHP"] + randint(5, 20)
    if((attacker["Sts"]["CurrHP"] + randint(5, 20)) < attacker["Sts"]["MaxHP"]):
        slow_type("{}'s HP went from {} to {}!".format(attacker["name"], attacker["Sts"]["CurrHP"], new_hp))
        attacker["Sts"]["CurrHP"] ==  new_hp
        attacker["Inv"]["bleach potion"] -= 1
    if((attacker["Sts"]["CurrHP"] + randint(5, 20)) > attacker["Sts"]["MaxHP"]) and (attacker["Sts"]["CurrHP"] != attacker["Sts"]["MaxHP"]):
        slow_type("\n{}'s HP went from {} to {}!".format(attacker["name"], attacker["Sts"]["CurrHP"], attacker["Sts"]["MaxHP"]))
        attacker["Sts"]["CurrHP"] == attacker["Sts"]["MaxHP"]
        attacker["Inv"]["bleach potion"] -= 1
    if(attacker["Sts"]["CurrHP"] == attacker["Sts"]["MaxHP"]):
        slow_type("\nYou are already at max health! Keep the potion!")

#creates the turn based fighting system for all the rooms
def commands1(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon1["reward"]
        player["Inv"]["gameroom key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a game room key! Put it in your inventory!".format(enemy["name"]));
        return laundry();

def commands2(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon2["reward"]
        player["Inv"]["smallbedroom key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a small bedroom key! Put it in your inventory!".format(enemy["name"]));
        return gameroom();
    if victor == "enemy":
        ded = input("\nYou have died. Do you want to try again? y/n :").lower()
        if ded == "y":
            print(menu())
        if ded == "n":
            slow_type("Goodbye.");
            return 0;

def commands3(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 10):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0 and player["Sts"]["CurrHP"] > 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon3["reward"]
        player["Inv"]["livingroom key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a living room key! Put it in your inventory!".format(enemy["name"]));
        return smallbr();

    if victor == "enemy":
        ded = input("\nYou have died. Do you want to try again? y/n :").lower()
        if ded == "y":
            print(menu())
        if ded == "n":
            slow_type("Goodbye.");
            return 0;

def commands4(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 11):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon4["reward"]
        player["Inv"]["bathroom key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a bathroom key! Put it in your inventory!".format(enemy["name"]));
        print(livr());
    if victor == "enemy":
        ded = input("\nYou have died. Do you want to try again? y/n :").lower()
        if ded == "y":
            print(menu())
        if ded == "n":
            slow_type("Goodbye.");
            return 0;

def commands5(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon5["reward"]
        player["Inv"]["masterbedroom key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a master bedroom key! Put it in your inventory!".format(enemy["name"]));
        return laundry();

    if victor == "enemy":
        ded = input("\nYou have died. Do you want to try again? y/n :").lower()
        if ded == "y":
            print(menu())
        if ded == "n":
            slow_type("Goodbye.");
            return 0;

def commands6(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon6["reward"]
        player["Inv"]["diningroom key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a dining room key! Put it in your inventory!".format(enemy["name"]));
        return laundry();

def commands7(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += Mon7["reward"]
        player["Inv"]["kitchen key"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a kitchen room key! Put it in your inventory!".format(enemy["name"]));
        return laundry();

    if victor == "enemy":
        ded = input("\nYou have died. Do you want to try again? y/n :").lower()
        if ded == "y":
            print(menu())
        if ded == "n":
            slow_type("Goodbye.");
            return 0;

def commands7(player, enemy):
    slow_type("\n{} is in a battle with {}!".format(player["name"], enemy["name"]))
    player_turn = True
    while(player["Sts"]["CurrHP"] != 0 and enemy["Sts"]["CurrHP"] != 0):
        if player_turn == True:
            line()
            ques = input("What will {} do?\na)|   attack   |\nb)|   potion   |\nc)|   escape   |\n".format(player["name"])).lower()
            if(ques == "a"):
                ques2 = input("What move would you like to use?\na) | Tide-al Wave |\nb) | Bleach Blast |\nc) |  Pod Punch   |\n").lower()
                if(ques2 == "a"):
                    getHit1GR(player, enemy)
                if(ques2 == "b"):
                    getHit2GR(player, enemy)
                if(ques2 == "c"):
                    getHit3GR(player, enemy)
            if(ques == "b" and Hero["Inv"]["bleach potion"] == 0):
                slow_type("You have no potions to use.")
                pass
            if(ques == "b" and Hero["Inv"]["bleach potion"] >= 1):
                slow_type("You use a bleach potion.")
                usepotion(player)
            if(ques == "c"):
                escpe = randint(0,10)
                if(escpe == 11):
                    slow_type("You have escaped!")
                    break
                if(escpe <= 9):
                    slow_type("You could not escape!")
            else:
                pass
        player_turn = False

        if player_turn == False:
            com_atk = randint(1, 3)
            if com_atk == 1:
                slow_type("\nIt is now {}'s turn, and it uses Squirt!".format(enemy["name"], player["name"]))
                getHit1GR(enemy, player)
            if com_atk == 2:
                slow_type("\nIt is now {}'s turn, and it uses Lick!".format(enemy["name"], player["name"]))
                getHit2GR(enemy, player)
            if com_atk == 3:
                slow_type("\nIt is now {}'s turn, and it uses Giga Gusher!".format(enemy["name"], player["name"]))
                getHit3GR(enemy, player)
        player_turn = True

        if (enemy["Sts"]["CurrHP"] <= 0):
            victor = "player"
            break

        if (player["Sts"]["CurrHP"] <= 0):
            victor = "enemy"
            break

    if victor == "player":
        slow_type("\n{} has been killed!".format(enemy["name"]))
        Hero["TPP"] += KM["reward"]
        player["Inv"] +=  enemy["key"]
        level(Hero, Sts)
        slow_type("\n{} dropped a kitchen room key! Put it in your inventory!".format(enemy["name"]));
        return laundry();

    if victor == "enemy":
        ded = input("\nYou have died. Do you want to try again? y/n :").lower()
        if ded == "y":
            print(menu())
        if ded == "n":
            slow_type("Goodbye.");
            return 0;
#makes a function for the starting menu
def menu():
    slow_type("GOD: Hello, this is God. I have seen that you recently transformed into a certain type of clothing, and you are currently in a house, in the laundry room. \nI don't really remember your name though.\n")
    global decis_name
    decis_name = input("\nWhat is your name? :")
    slow_type(f"{decis_name}, ah yes, thats a great name!")
    Hero["name"] == decis_name
    global decis_cloth
    decis_cloth = input("\nOh, and what piece of clothing are you? You look like you are either shorts, a shirt, or a dress. :").lower()
    if(decis_cloth == "shorts") or (decis_cloth == "shirt") or (decis_cloth == "dress"):
        slow_type(f"{decis_name} the {decis_cloth}. Thats got a nice ring to it. OK, are you ready to start your adventure?")
        choice1 = (input(" y/n :"))
        if(choice1 == "y"):
            slow_type(f"Ok, so before you start this adventure, you'll need some background");
            return laundry();
        if(choice1 == "n"):
            slow_type("OK, well then. Uhmmm, goodbye.");
            return 0;
    elif (decis_cloth != "shorts") or (decis_cloth != "shirt") or (decis_cloth != "dress"):
        slow_type(f"You can't be a {decis_cloth}!");
        return DC();
#makes function to return to the second question of the starting menu
def DC():
    decis_cloth = input("\nWhat piece of clothing are you? You look like you are either shorts, a shirt, or a dress. :").lower()
    if(decis_cloth == "shorts") or (decis_cloth == "shirt") or (decis_cloth == "dress"):
        slow_type(f"{decis_name} the {decis_cloth}. Thats got a nice ring to it. OK, are you ready to start your adventure?")
        choice1 = (input(" y/n :"))
        if(choice1 == "y"):
            slow_type(f"Ok, so before you start this adventure, you'll need some background");
            return laundry();
        if(choice1 == "n"):
            slow_type("OK, well then. Uhmmm, goodbye.");
            return 0;
    elif (decis_cloth != "shorts") or (decis_cloth != "shirt") or (decis_cloth != "dress"):
        slow_type(f"You can't be a {decis_cloth}!")
        print(DC())
#makes function for game room
def gameroom():
    Hero["name"] = decis_name
    Leave = False
    if(groom["tide pod"] == 0 and Hero["Inv"]["smallbedroom key"] == 1):
        slow_type("\nGOD: Great job {}! Now, you can clean the room with the tide pods that you possess!".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhere would you like to look?\na)|  basket  |\nb)| cabinet  |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing of importance in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: It's just empty.\n")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["small bedroom key"] == 0):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["small bedroom key"] == 0):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the game room.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                groom["tide pod"] += 2


            if(ASD == "b") and (Hero["Cln"] == 1):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")
            else:
                pass

            if(ASD == "b") and (Hero["Cln"] >= 2):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Laundry Room  |\n")
                if(dir1 == "a"):
                    slow_type("GOD: {}, you are moving to the laundry room!".format(Hero["name"]))
                    print(laundry())
            else:
                pass

    if(ldry["tide pod"] == 2) and (Hero["Inv"]["smallbedroom key"] == 0) and (Hero["Inv"]["tide pod"] <= 1):
        slow_type("\n You are in the game room now.")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     |                      | XXXXXXXXXXXXXXXXXXX |\n|    SMALL  BEDROOM   L     LAUNDRY ROOM     U XXXXX GAMEROOM XXXX |\n|                     |      (CLEANSED)      | XXXXXXXXXXXXXXXXXXX |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: There is a basket full of random toys and video games to your left. On the cabinet of board games, something seems to stand out.\nWhat would you like to look\na)|  basket  |\nb)| cabinet  |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] > 3):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] < 3):
                    slow_type("GOD: Look, you found 2 Bleach Potions! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 2
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 2):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] == 1):
                    slow_type("GOD: Look, you found 5 tide pods!\n")
                    Hero["Inv"]["tide pod"] += 5
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["smallbedroom key"] == 0):
                slow_type("GOD: Lets get started on this room!\n....................")
                slow_type("\nGUSHTON: Don't you dare clean those dirty, dirty clothing.")
                slow_type("\nGOD: Not another one!")
                commands2(Hero, Mon2)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["smallbedroom key"] == 0):
                slow_type("GOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "b"):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     |                      | XXXXXXXXXXXXXXXXXX |\n|    SMALL  BEDROOM   L     LAUNDRY ROOM     U XXXXX GAMEROOM XXXX |\n|                     |      (CLEANSED)      | XXXXXXXXXXXXXXXXXX |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Laundry Room  |")
                if(dir1 == "a"):
                    slow_type("\nGOD: {}, you have gone to the laundry room!".format(Hero["name"]));
                    print(laundry());
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass

    if(Hero["Cln"] >= 2 and groom["tide pod"] == 2):
        slow_type("\nGOD: This room is already clean.")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhat would you like to look through?\na)|  basket  |\nb)| cabinet |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: Its just empty.\n")
                else:
                    pass

            if(ASD == "a"):
                slow_type("\nGOD: The gameroom is already clean.")

            if(ASD == "b") and (Hero["Cln"] == 1):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Laundry Room  |\n")
                if dir1 == "a":
                    slow_type("\nGOD: {}, you have entered the laundry room.");
                    print(laundry())
            if(ASD == "d"):
                chkInv()
            else:
                pass
#makes function for laundry room
def laundry():
    Hero["name"] = decis_name
    Leave = False
    if(ldry["tide pod"] == 0 and Hero["Inv"]["gameroom key"] == 1):
        slow_type("\nGOD: Great job {}! Now, you can clean the room with the tide pods that you possess!".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhat would you like to look through?\na)|  laundry bag  |\nb)|washing machine|\nc)|     trash     |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: It's just empty.\n")
                if (laun1 == "c"):
                    slow_type("\nGOD: There is trash in the trash.")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["gameroom key"] == 0 and Hero["Cln"] == 0):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["gameroom key"] == 0 and Hero["Cln"] == 1):
                slow_type("\nGOD: This room is already clean.")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["gameroom key"] == 1):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the laundry room.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                ldry["tide pod"] += 2
            if(ASD == "b") and (Hero["Cln"] == 0):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")

            if(ASD == "b") and (Hero["Cln"] == 1):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb)| Small Bedroom |\nc)|  Game Room  |")
                if dir1 == "a":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "b":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "c":
                    slow_type("\nGOD: {}, you have entered the game room!".format(Hero["name"]))
                    print(gameroom())
                else:
                    pass

            else:
                pass

    if(Hero["Cln"] >= 1):
        slow_type("\nGOD: This room is already clean.")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhat would you like to look through?\na)|  laundry bag  |\nb)|washing machine|\nc)|     trash     |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: Its just empty.\n")
                if (laun1 == "c"):
                    slow_type("\nGOD: There is trash in the trash.")

            if(ASD == "a"):
                slow_type("\nGOD: The laundromat is already clean.")

            if(ASD == "b") and (Hero["Cln"] == 1):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb)| Small Bedroom |\nc)|  Game Room  |")
                if dir1 == "a":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "b":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "c":
                    slow_type("\nGOD: {}, you have entered the game room!".format(Hero["name"]))
                    print(gameroom())


            if(ASD == "b") and (Hero["smallbedroom key"] == 1) and (Hero["Cln"] == 2):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX U       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb)| Small Bedroom |\nc)|  Game Room  |\n")
                if(dir1 == "a"):
                    slow_type("\nGOD: You don't have the key to that room.")
                if(dir1 == "b"):
                    slow_type("\nGOD: {}, you have entered the small bedroom!".format(Hero["name"]))
                    print(smallbr())
                if(dir1 == "c"):
                    slow_type("\nGOD: {}, you have entered the game room!".format(Hero["name"]));
                    print(gameroom())

            if(ASD == "b") and (Hero["smallbedroom key"] == 1) and (Hero["livingroom key"]) and (Hero["Cln"] == 3):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   U XXX LAUNDRY ROOM XXX U       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb)| Small Bedroom |\nc)|  Game Room  |")
                if dir1 == "a":
                    slow_type("\nGOD: {}, you have entered the living room!".format(Hero["name"]))
                    print(livr())
                if dir1 == "b":
                    slow_type("\nGOD: {}, you have entered the small bedroom!".format(Hero["name"]))
                    print(smallbr())
                if(dir1 == "c"):
                    slow_type("\nGOD: {}, you have entered the game room!".format(Hero["name"]));
                    print(gameroom())


            if(ASD == "b") and (Hero["small bedroom key"] == 1) and (Hero["Cln"] > 3):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________U_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   U XXX LAUNDRY ROOM XXX U       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb)| Small Bedroom |\nc)|  Game Room  |")
                if dir1 == "a":
                    slow_type("\nGOD: {}, you have entered the living room!".format(Hero["name"]))
                    print(livr())
                if dir1 == "b":
                    slow_type("\nGOD: {}, you have entered the small bedroom!".format(Hero["name"]))
                    return smallbr()
                if dir1 == "c":
                    slow_type("\nGOD: {}, you have entered the game room!".format(Hero["name"]));
                    print(gameroom())
            if(ASD == "d"):
                chkInv()
            else:
                pass




    if(ldry["tide pod"] == 0) and (Hero["Inv"]["gameroom key"] == 0) and (Hero["Inv"]["tide pod"] == 0) and (Hero["Inv"]["bleach potion"] == 0):
        slow_type(" So, you are at the laundry room right now")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        slow_type("\nGOD: Right now, this room, along with all the other rooms are very dirty.\nYour purpose in this house is to clean up the mess using Tide Pods.\nYou will need about 2 pods per room in order to fully clean a room full of dirty clothing.\nYou may need to fight some disgusting, gross pieces of candy known as Gushers, aka the wannabee Tide Pods. \nThese gushers may have items, such as keys to other rooms, and maybe even more tide pods!\nBefore you transformed into a {}, I taught you the way of the Tide Pod, and you now have the moves to fend off those grotesque Gushers!\nYou are still level one though, but you can improve on that by getting Tide Pod Points, which are given after fighting Gushers. This will improve your health and your attacks.\nYou've got all that? Great! Lets start cleaning this dirty house!".format(decis_cloth))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: There is a laundry bag on the floor, a washing machine by the opposite wall, and a trash can brimming with garbage.\n Where would you like to look?\na)|  laundry bag  |\nb)|washing machine|\nc)|     trash     |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] > 0):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] not in Hero):
                    slow_type("\nGOD: Look, you found a Bleach Potion! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 1
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 0):
                    slow_type("\nGOD: There is nothing in there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] not in Hero):
                    slow_type("\nGOD: Look, you found 3 tide pods! Thats great! Now you can use this to clean the room!\n")
                    Hero["Inv"]["tide pod"] += 3
                if (laun1 == "c"):
                    slow_type("\nGOD: There is trash in the trash.")
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["gameroom key"] == 0):
                slow_type("GOD: Lets get started on this room!\n....................Oh no! You found a Gusher! Now you have to fight it!")
                slow_type("\nGUSH JR: Well, well. Someone is trying to clean this dirty boi?")
                slow_type("\nGOD: Use the power of the tide pods to defeat it!")
                commands1(Hero, Mon1)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["gameroom key"] == 0):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "b"):
                slow_type("\nGOD: You can not go anywhere. You don't have the key to any doors.")

            if(ASD == "d"):
                chkInv()
            else:
                pass


#makes function for small bedroom
def smallbr():
    Hero["name"] = decis_name
    Leave = False
    if(sbroom["tide pod"] == 0 and Hero["Inv"]["livingroom key"] == 1 and Hero["Cln"] == 2):
        slow_type("\nGOD: Great job {}! Those pesky Gushers. They are disgusting. The world would be better without them.".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhere would you like to look?\na)|  under the bed  |\nb)|  wardrobe  |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing of importance in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: It's just empty.\n")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["livingroom key"] == 1):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["livingroom key"] == 1):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the small bedroom.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                smallbr["tide pod"] += 2


            if(ASD == "b") and (Hero["Cln"] == 2):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")
            else:
                pass

            if(ASD == "b") and (Hero["Cln"] > 2):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Laundry Room  |\n")
                if(dir1 == "a"):
                    slow_type("GOD: {}, you are moving to the laundry room!".format(Hero["name"]))
                    print(laundry())
            else:
                pass

    if(ldry["tide pod"] == 2) and (groom["tide pod"] == 2) and (Hero["Inv"]["livingroom key"] == 0) and (Hero["Inv"]["tide pod"] <= 1):
        slow_type("\n You are in the small bedroom now.")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: The bed is cleaned on top, but the floor under the bed is a mess. \nThe wardrobe is slightly open. Maybe it warrants closer inspection?. \nWhere will you search?\na)|  under the bed  |\nb)|   wardrobe   |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] > 3):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] <= 3):
                    slow_type("GOD: Look, you found 3 Bleach Potions! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 3
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 4):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] <= 4):
                    slow_type("GOD: Look, you found 2 tide pods!\n")
                    Hero["Inv"]["tide pod"] += 2
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["livingroom key"] == 0):
                slow_type("GOD: Lets get started on this room!\n....................")
                slow_type("\nGUSHTON: GUSH GUSH GUSH GUSH!")
                slow_type("GOD: Goodness...")
                commands3(Hero, Mon3)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["small bedroom key"] == 0):
                slow_type("GOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "b"):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Laundry Room  |")
                if(dir1 == "a"):
                    slow_type("\nGOD: {}, you have gone to the laundry room!".format(Hero["name"]))
                    print(laundry())
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass

    if(Hero["Cln"] >= 3 and smallbr["tide pod"] == 2):
        slow_type("\nGOD: This room is already clean.")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhere would you like to look?\na)|  under the bed  |\nb)|    wardrobe   |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: Its just empty.\n")
                if (laun1 == "c"):
                    slow_type("\nGOD: There is trash in the trash.")
                else:
                    pass

            if(ASD == "a"):
                slow_type("\nGOD: The small bedroom is already clean.")

            if(ASD == "b") and (Hero["Cln"] == 1):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n| XX SMALL  BEDROOM X U     LAUNDRY ROOM     U       GAMEROOM      |\n| XXXXX(CLEANSED)XXXXX |                      |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Laundry Room  |\n")
                if dir1 == "a":
                    slow_type("\nGOD: {}, you have entered the laundry room.");
                    print(laundry())
                else:
                    pass
            if(ASD == "d"):
                chkInv()
            else:
                pass
#makes function for living room
def livr():
    Hero["name"] = decis_name
    Leave = False
    if(livr["tide pod"] == 0 and Hero["Inv"]["bathroom key"] == 1):
        slow_type("\nGOD: Great job {}! Now, you can clean the room with the tide pods that you possess!".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhat would you like to look through?\na)|  sofa  |\nb)| coat hanger |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                    slow_type("\nGOD: It's just clothes.\n")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["bathroom key"] == 0 and Hero["Cln"] == 0):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["bathroom key"] == 0 and Hero["Cln"] == 4):
                slow_type("\nGOD: This room is already clean.")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["bathroom key"] == 1):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the living room.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                ldry["tide pod"] += 2
            if(ASD == "b") and (Hero["Cln"] == 0):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")

            if(ASD == "b") and (Hero["Cln"] == 4):
                print("\n____________________________________________________________________\n|                     | XXXXXXXXXXXXXXXXXXXXX |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   | XXXXXXXXXXXXXXXXXXXX |        KITCHEN      |\n|                     L XXXXXXXXXXXXXXXXXXXXX |                     |\n|                 ____| XXXXXXXXXXXXXXXXXXXXX |___________L_________|\n|                | XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|----------------| XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|    BATHROOM    | XXXXX LIVING  ROOM XXXX L     DINING  ROOM    |\n|                L XXXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|________________|_____________U_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Dining Room  |\nb)| Master Bedroom |\nc)|  Bathroom  |\nd)| Laundry Room |").lower()
                if dir1 == "a":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "b":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "c":
                    slow_type("\nGOD: {}, you have entered the bathroom!".format(Hero["name"]))
                    print(bathroom())
                if(dir1 == "d"):
                    slow_type("\nGOD: {}, you have entered the Laundry Room!".format(Hero["name"]));
                    print(laundry())
                else:
                    pass
            else:
                pass

    if(Hero["Cln"] >= 4):
        slow_type("\nGOD: This room is already clean.")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhat would you like to look through?\na)|    sofa    |\nb)| coat hanger |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in the sofa.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: It's just clothes.\n")
            if(ASD == "a"):
                slow_type("\nGOD: The laundromat is already clean.")

            if(ASD == "b") and (Hero["Cln"] == 4):
                print("\n____________________________________________________________________\n|                     | XXXXXXXXXXXXXXXXXXXXX |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   | XXXXXXXXXXXXXXXXXXXX |        KITCHEN      |\n|                     L XXXXXXXXXXXXXXXXXXXXX |                     |\n|                 ____| XXXXXXXXXXXXXXXXXXXXX |___________L_________|\n|                | XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|----------------| XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|    BATHROOM    | XXXXX LIVING  ROOM XXXX L     DINING  ROOM    |\n|                L XXXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|________________|_____________U_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Dining Room  |\nb)| Master Bedroom |\nc)|  Bathroom  |\nd)| Laundry Room |").lower()
                if dir1 == "a":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "b":
                    slow_type("GOD: You don't have the key to that room.")
                if dir1 == "c":
                    slow_type("\nGOD: {}, you have entered the Bathroom!".format(Hero["name"]))
                    print(gameroom())
                if(dir1 == "d"):
                    slow_type("\nGOD: {}, you have entered the Laundry Room!".format(Hero["name"]));
                    print(laundry())


            if(ASD == "b") and (Hero["masterbedroom key"] == 1) and (Hero["Cln"] == 5):
                print("\n____________________________________________________________________\n|                     | XXXXXXXXXXXXXXXXXXXXX |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   | XXXXXXXXXXXXXXXXXXXX |        KITCHEN      |\n|                     U XXXXXXXXXXXXXXXXXXXXX |                     |\n|                 ____| XXXXXXXXXXXXXXXXXXXXX |___________L_________|\n|                | XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|----------------| XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|    BATHROOM    | XXXXX LIVING  ROOM XXXX L     DINING  ROOM    |\n|                U XXXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|________________|_____________U_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   U     LAUNDRY ROOM     U       GAMEROOM      |\n|      (CLEANSED)        |      (CLEANSED)      |      (CLEANSED)      |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Dining Room  |\nb)| Master Bedroom |\nc)|  Bathroom  |\nd)| Laundry Room |").lower()
                if(dir1 == "a"):
                    slow_type("\nGOD: You don't have the key to that room.")
                if(dir1 == "b"):
                    slow_type("\nGOD: {}, you have entered the Master Bedroom!".format(Hero["name"]))
                    print(smallbr())
                if(dir1 == "c"):
                    slow_type("\nGOD: {}, you have entered the Bathroom!".format(Hero["name"]));
                    print(gameroom())
                if(dir1 == "d"):
                    slow_type("\nGOD: {}, you have entered the Laundry Room!".format(Hero["name"]));
                    print(laundry())

            if(ASD == "b") and (Hero["diningroom key"] == 1) and (Hero["Cln"] == 6):
                print("\n____________________________________________________________________\n|                     | XXXXXXXXXXXXXXXXXXXXX |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   | XXXXXXXXXXXXXXXXXXXX |        KITCHEN      |\n|                     U XXXXXXXXXXXXXXXXXXXXX |                     |\n|                 ____| XXXXXXXXXXXXXXXXXXXXX |___________L_________|\n|                | XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|----------------| XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|    BATHROOM    |       LIVING  ROOM      U     DINING  ROOM    |\n|                U XXXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|________________|_____________U_____________|_____________________|\n|                     |                      |                     |\n|                     |                      |                     |\n|    SMALL  BEDROOM   L     LAUNDRY ROOM     L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Dining Room  |\nb)| Master Bedroom |\nc)|  Bathroom  |\nd)| Laundry Room |").lower()
                if dir1 == "a":
                    slow_type("\nGOD: {}, you have entered the dining room!".format(Hero["name"]))
                    print(livr())
                if dir1 == "b":
                    slow_type("\nGOD: {}, you have entered the master bedroom!".format(Hero["name"]))
                    print(smallbr())
                if(dir1 == "c"):
                    slow_type("\nGOD: {}, you have entered the game room!".format(Hero["name"]));
                    print(gameroom())
                if(dir1 == "d"):
                    slow_type("\nGOD: {}, you have entered the Laundry Room!".format(Hero["name"]));
                    print(laundry())
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass




    if(livrm["tide pod"] == 0) and (Hero["Inv"]["livingroom key"] == 0) and (Hero["Inv"]["tide pod"] >= 0) and (Hero["Inv"]["bleach potion"] >= 0):
        slow_type(" So, you are at the living room right now")
        print("\n____________________________________________________________________\n|                     | XXXXXXXXXXXXXXXXXXXXX |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   | XXXXXXXXXXXXXXXXXXXX |        KITCHEN      |\n|                     U XXXXXXXXXXXXXXXXXXXXX |                     |\n|                 ____| XXXXXXXXXXXXXXXXXXXXX |___________L_________|\n|                | XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|----------------| XXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|    BATHROOM    | XXXXX LIVING  ROOM XXXX L     DINING  ROOM    |\n|                U XXXXXXXXXXXXXXXXXXXXXXXXX |                     |\n|________________|_____________U_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   U XXX LAUNDRY ROOM XXX U       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: There is a sofa that has an object peeking under it. The coat hanger looks suspiciously lumpy, too.\n Where would you like to look?\na)|    sofa   |\nb)| coat hanger |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] > 9):
                    slow_type("GOD: There is nothing by there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] <= 8):
                    slow_type("\nGOD: Look, you found 2 Bleach Potion! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 2
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 0 and livr["tide pod"] == 0):
                    slow_type("\nGOD: There is nothing by there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] < 4):
                    slow_type("\nGOD: Look, you found 2 tide pods! Thats great! Now you can use this to clean the room!\n")
                    Hero["Inv"]["tide pod"] += 2
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["gameroom key"] == 0):
                slow_type("GOD: Lets get started on this room!\n....................Oh no! You found a Gusher! Now you have to fight it!")
                slow_type("\nGUSHELL: OOGA BOOGA.")
                slow_type("\nGOD: Every freaking time!")
                commands4(Hero, Mon4)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["gameroom key"] == 0):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "b"):
                dir1 = input("\nGOD: Where do you want to go?\na)|  Dining Room  |\nb)| Master Bedroom |\nc)|  Bathroom  |\nd)| Laundry Room |").lower()
                if dir1 == "a":
                    slow_type("\nGOD: You do not have the key to this room.")
                    print(diner())
                if dir1 == "b":
                    slow_type("\nGOD: You do not have the key to this room.")
                    print(mastbr())
                if dir1 == "c":
                    slow_type("\nGOD: You do not have the key to this room.");
                    print(bathroom())
                if(dir1 == "d"):
                    slow_type("\nGOD: {}, you have entered the Laundry Room!".format(Hero["name"]));
                    print(laundry())
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass
#makes function for bathroom
def bathroom():
    Hero["name"] = decis_name
    Leave = False
    if(bathrm["tide pod"] == 0 and Hero["Inv"]["masterbedroom key"] == 1 and Hero["Cln"] == 2):
        slow_type("\nGOD: Great job {}! Those Gushers are getting on my nerves!".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhere would you like to look?\na)|  in the toilet  |\nb)|  under the sink  |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing of importance in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: It's just floor.\n")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["masterbedroom key"] == 1):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["masterbedroom key"] == 1):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the bathroom.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                bathrm["tide pod"] += 2

            if(ASD == "b") and (Hero["Cln"] == 4):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")
            else:
                pass

            if(ASD == "b") and (Hero["Cln"] == 5):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\n")
                if(dir1 == "a"):
                    slow_type("GOD: {}, you are moving to the living room!".format(Hero["name"]))
                    print(livr())
                else:
                    pass
            else:
                pass

    if(ldry["tide pod"] == 2) and (groom["tide pod"] == 2) and (Hero["Inv"]["masterbedroom key"] == 0) and (Hero["Inv"]["tide pod"] <= 1):
        slow_type("\n You are in the bathroom now.")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: There is a sink with a little cabinet under it. The toilet seat is also open.\nWhere will you search?\na)|    toilet    |\nb)| under the sink |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] >= 10):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] < 10):
                    slow_type("GOD: Look, you found 3 Bleach Potions! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 3
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 4):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] <= 4):
                    slow_type("GOD: Look, you found 3 tide pods!\n")
                    Hero["Inv"]["tide pod"] += 3
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["livingroom key"] == 0):
                slow_type("GOD: Time to clean the bathroom!\n....................")
                slow_type("\nGUSHPY: GUSSSHHHHHHHHH PYYYYYYYYY!")
                slow_type("GOD: ...")
                commands5(Hero, Mon5)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["small bedroom key"] == 0):
                slow_type("GOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "b"):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |")
                if(dir1 == "a"):
                    slow_type("\nGOD: {}, you have gone to the living room!".format(Hero["name"]))
                    print(livr())
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass
#makes function for master bedroom
def mastbr():
    Hero["name"] = decis_name
    Leave = False
    if(bathrm["tide pod"] == 0 and Hero["Inv"]["masterbedroom key"] == 1 and Hero["Cln"] == 2):
        slow_type("\nGOD: Great job {}! Those Gushers are getting on my nerves!".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhere would you like to look?\na)|    bed    |\nb)|  closet  |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing of importance in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: Only some old shoeboxes in there.\n")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["diningroom key"] == 1):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["diningroom key"] == 1):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the master bedroom.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                bathrm["tide pod"] += 2

            if(ASD == "b") and (Hero["Cln"] == 5):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")
            else:
                pass

            if(ASD == "b") and (Hero["Cln"] > 5):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\n")
                if(dir1 == "a"):
                    slow_type("GOD: {}, you are moving to the living room!".format(Hero["name"]))
                    print(livr())
                else:
                    pass
            else:
                pass

    if(ldry["tide pod"] == 2) and (groom["tide pod"] == 2) and (Hero["Inv"]["diningroom key"] == 0) and (Hero["Cln"] == 5):
        slow_type("\n You are in the master bedroom now.")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: There is a large bed, with some objects poking out of the cover. There is closet where some things might be found, too.\nWhere will you search?\na)|    bed    |\nb)|   closet   |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] >= 12):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] < 12):
                    slow_type("GOD: Look, you found 2 Bleach Potions! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 2
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 5):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] <= 5):
                    slow_type("GOD: Look, you found 3 tide pods!\n")
                    Hero["Inv"]["tide pod"] += 3
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["diningroom key"] == 0):
                slow_type("GOD: Time to clean the master bedroom!\n....................")
                slow_type("\nGUSHDON: REEEEEEEEEEEEEEEEEEE")
                slow_type("GOD: OH MY FU-")
                commands6(Hero, Mon6)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["diningroom key"] == 0):
                slow_type("GOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "b"):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |")
                if(dir1 == "a"):
                    slow_type("\nGOD: {}, you have gone to the living room!".format(Hero["name"]))
                    print(livr())
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass
#makes function for dining room
def diner():
    Hero["name"] = decis_name
    Leave = False
    if(dinrm["tide pod"] == 0 and Hero["Inv"]["kitchen key"] == 1 and Hero["Cln"] == 2):
        slow_type("\nGOD: Great job {}! Those Gushers are getting on my nerves!".format(decis_name))
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhere would you like to look?\na)|    bed    |\nb)|  closet  |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing of importance in there.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: Only some old shoeboxes in there.\n")
                else:
                    pass
            if(ASD == "d"):
                chkInv()

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["kitchen key"] == 1):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")

            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["kitchen key"] == 1):
                slow_type("\nGOD: Good, you have enough tide pods to clean the clothes on the floor! Lets begin!\n..........................\n{} used two tide pods to clean the clothes in the master bedroom.\n.............................\nGOD: The room is now clean. Great job! On to the next room!".format(Hero["name"]))
                Hero["Inv"]["tide pod"] = Hero["Inv"]["tide pod"] - 2
                Hero["Cln"] += 1
                dinrm["tide pod"] += 2

            if(ASD == "b") and (Hero["Cln"] == 6):
                slow_type("\nGOD: Maybe you should clean this mess before you move on to the next room.")
            else:
                pass

            if(ASD == "b") and (Hero["Cln"] > 6):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb) Kitchen")
                if(dir1 == "a"):
                    slow_type("\nGOD: {}, you have gone to the living room!".format(Hero["name"]))
                    print(livr())
                if(dir1 == "b"):
                    slow_type("\nGOD: {}, you have gone to the kitchen!".format(Hero["name"]))
                    print(kitch())
                else:
                    pass
            else:
                pass
    if(Hero["Cln"] >= 7):
        slow_type("\nGOD: This room is already clean.")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nWhat would you like to look through?\na)|    sofa    |\nb)| coat hanger |\n").lower()
                if (laun1 == "a"):
                    slow_type("\nGOD: Looks like there is nothing in the sofa.\n")
                if (laun1 == "b") and (Hero["Inv"]["tide pod"] > 0):
                        slow_type("\nGOD: It's just clothes.\n")

            if(ASD == "a"):
                slow_type("\nGOD: The dining room is already clean.")

            if(ASD == "b") and (Hero["Cln"] == 4):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n|                     | XXXXXXXXXXXXXXXXXXXX |                     |\n|    SMALL  BEDROOM   L XXX LAUNDRY ROOM XXX L       GAMEROOM      |\n|                     | XXXXX(CLEANSED)XXXXX |                     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb)|  Kitchen  |\n").lower()
                if dir1 == "a":
                    slow_type("\nGOD: {}, you have entered the Living Room!".format(Hero["name"]))
                    print(livr())
                if(dir1 == "b"):
                    slow_type("\nGOD: {}, you have entered the Kitchen!".format(Hero["name"]));
                    print(kitrm())

    if(ldry["tide pod"] == 2) and (groom["tide pod"] == 2) and (Hero["Inv"]["kitchen key"] == 0) and (Hero["Cln"] == 5):
        slow_type("\n You are in the master bedroom now.")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        while Leave != True:
            ASD = input(def_actions)
            if(ASD == "c"):
                laun1 = input("\nGOD: There is a large bed, with some objects poking out of the cover. There is closet where some things might be found, too.\nWhere will you search?\na)|    bed    |\nb)|   closet   |\n").lower()
                if (laun1 == "a" and Hero["Inv"]["bleach potion"] >= 12):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "a" and Hero["Inv"]["bleach potion"] < 12):
                    slow_type("GOD: Look, you found 2 Bleach Potions! Now, you have that in your inventory!\n")
                    Hero["Inv"]["bleach potion"] += 2
                if (laun1 == "b" and Hero["Inv"]["tide pod"] > 5):
                    slow_type("GOD: There is nothing in there.\n")
                elif (laun1 == "b" and Hero["Inv"]["tide pod"] <= 5):
                    slow_type("GOD: Look, you found 3 tide pods!\n")
                    Hero["Inv"]["tide pod"] += 3
                else:
                    pass
            if(ASD == "a") and (Hero["Inv"]["tide pod"] >= 2) and (Hero["Inv"]["kitchen key"] == 0):
                slow_type("\nGOD: Time to clean the master bedroom!\n....................")
                slow_type("\nGUSHDON: REEEEEEEEEEEEEEEEEEE")
                slow_type("\nGOD: OH MY FU-")
                commands6(Hero, Mon6)

            if(ASD == "a" and Hero["Inv"]["tide pod"] < 2 and Hero["Inv"]["kitchen key"] == 0):
                slow_type("\nGOD: You need two tide pods to clean this room. You might need to search for some around here...")


            if(ASD == "b"):
                print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
                dir1 = input("\nGOD: Where do you want to go?\na)|  Living Room  |\nb) Kitchen")
                if(dir1 == "a"):
                    slow_type("\nGOD: {}, you have gone to the living room!".format(Hero["name"]))
                    print(livr())
                if(dir1 == "b"):
                    slow_type("\nGOD: You do not have the key to this room yet.")
                else:
                    pass

            if(ASD == "d"):
                chkInv()
            else:
                pass
#makes function for kitchen room
def kitch():
    Hero["name"] = decis_name
    Leave = False
    while Leave != True:
        slow_type("\nYou are in the kitchen now.")
        print("\n____________________________________________________________________\n|                     |                      |                     |\n|                     |                      |                     |\n|    MASTER BEDROOM   |                      |        KITCHEN      |\n|                     L                      |                     |\n|                 ____|                      |___________L_________|\n|                |                           |                     |\n|----------------|                           |                     |\n|    BATHROOM    |       LIVING  ROOM        L     DINING  ROOM    |\n|                L                           |                     |\n|________________|_____________L_____________|_____________________|\n|                     |                      |                     |\n| XXXXXXXXXXXXXXXXXXX |                      |                     |\n| XX SMALL BEDROOM XX U     LAUNDRY ROOM     U      GAMEROOM       |\n| XXXXXXXXXXXXXXXXXXX |      (CLEANSED)      |      (CLEANSED)     |\n|_____________________|______________________|_____________________|\n\nL = LOCKED DOOR\nU = UNLOCKED DOOR")
        ASD = input(def_actions)
        if ASD == "d":
            chkInv()
        if ASD == "c":
            slow_type("\nGOD: There is nothing but dirty clothes in this room...")
        if ASD == "b":
            slow_type("\nGOD: Yeah, I think it would be best if you just left this room... HUH? The door is locked. Strange.")
        if ASD == "a":
            slow_type("\nGOD:Yeah, let's clean this place then dip. OK, so...")
            slow_type("\nUNKNOWN: What do you mean, dip?")
            slow_type("\nGOD: Who are you?")
            slow_type("\nUNKNOWN: I'm King Gush! The ruler of all the gushers!")
            slow_type("\nKING GUSH: I don't really like how you have been killing all my gusher minions. So I'll get rid of you before you kill any more!")
            commands7(Hero, GM)
print(menu())
