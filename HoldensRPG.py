print "Welcome to Holden's RPG!"
print "\nYou are the sole survivor of the village of Karn, burned to ashes by the Dragon Svelenor. Svelenor was once a Warlock who let his quest for power and rage consume him, turning him into the beast that terrorizes the entire continent. Svelenor, The Emerald Dragon has been living and roaming free for far too long. It is up to you to stop him. It is up to you for revenge."
import random
import shelve
#!/usr/bin/env python

#import pickle
#data = {my_stats, Class_Choice, my_level, my_damage, my_health, inventory}
##Classes Class##
class Classes(object):
    def __init__(self, class_name, weapon, skill):
        self.class_name = class_name
        self.weapon = weapon
        self.skill = skill
    def __str__(self):
        return "Class: %s \nWeapon: %s \nSkill: %s" % (self.class_name, self.weapon, self.skill)
##Classes##
Warrior = Classes("Warrior", "Sword", "Power Slash")
Hunter = Classes("Hunter", "Bow", "Tri-Shot")
Mage = Classes("Mage", "Staff", "Fireball")
Holy_Knight = Classes("Holy Knight", "Holy Blade", "Holy")
Ranger = Classes("Ranger", "Athena's Bow", "Snipe")
Warlock = Classes("Warlock", "Hade's Staff", "Death")
Dev = Classes("Developer", "Ultima Weapon", "Armageddon")
Upgrade = Classes("Upgrade", "Ultima Weapon", "Test")
##Character Class##
class Character():
    def __init__(self, clazz, name):
        self.clazz = clazz        
        self.name = name
    def __str__(self):
        return "\nName: %s \n%s \n" % (self.name, self.clazz)
##Location Class##
class Location():
    def __init__(self, current_location):
        self.current_location = current_location
##Event Class##
class Event():
    def __init__(self, event):
        self.event = event
##Shop Class##
class Shop():
    def __init__(self, item):
        self.item = item        
    def __str__(self):
        return "%s" % (self.item)
###Gear Class###
class Gear():
    def __init__(self, gear):
        self.gear = gear
    def __str__(self):
        return "%s" % (self.gear)
##Action Class##
class Action():
    def __init__(self, action):
        self.action = action
    def __str__(self):
        return "%s" % self.action
##Monster Class##
class Monster():
    def __init__(self, monster):
        self.monster = monster
    def __str__(self):
        return "%s" % (self.monster)
##Treasure Class##
class Treasure():
    def __init__(self, treasure):
        self.treasure = treasure
    def __str__(self):
        return "%s" % (self.treasure)
##RANDOM DROP CLASS##
class Drop():
    def __init__(self, drop):
        self.drop = drop
    def __str__(self):
        return "%s" % self.drop
##Skill Class##
class Skill():
    def __init__(self, skill):
        self.skill = skill
    def __str__(self):
        return "%s" % self.skill
##SKILLS##
Fireball = Skill("Fireball")
Tri_Shot = Skill("Tri Shot")
Power_Slash = Skill("Power Slash")
Armageddon = Skill("Armageddon")

##Locations##
Forest = Location("Forest")
Dungeon = Location("Dungeon")
Mountains = Location("Mountains")
Shop = Location("Shop")
Equipment = Location("Equip")
##Actions##
Explore = Action("Explore")
Travel = Action("Travel")
Exit = Action("Action")
Shop = Action("Shop")
##Random Explore##
Random_Explore = ["Fight!", "Treasure!"]
##Monsters#
Goblin = Monster("Goblin")
Bat = Monster("Bat")
##Monster List##
Monster_List_1 = []
Monster_List_1.append(Monster("Goblin"))
Monster_List_1.append(Monster("Bat"))
##MONSTER LIST 2##
Monster_List_2 = []
Monster_List_2.append(Monster("Troll"))
Monster_List_2.append(Monster("Skeleton"))
##MONSTER LIST 3##
Monster_List_3 = []
Monster_List_3.append(Monster("Barbarian"))
Monster_List_3.append(Monster("Svelanor, Emerald Dragon"))
##Treasure Items##
Gold = Treasure("Gold")
Gems = Treasure("Gems")
##Treasure List Random##
Treasure_List_1 = []
Treasure_List_1.append(Treasure("Gold"))
Treasure_List_1.append(Drop("Emerald"))
##Drops##
Emerald = Drop("Emerald")
Apple = Drop("Apple")
##DROP LIST##
Drop_List_1 = []
Drop_List_1.append(Drop("Emerald"))
Drop_List_1.append(Treasure("Gold"))
##DropLIST DUNGEON##
Drop_List_2 = []
Drop_List_2.append(Drop("Emerald"))
Drop_List_2.append(Treasure("Gold"))
##DropLIST Mountain##
Drop_List_3 = []
Drop_List_3.append(Drop("Emerald"))
Drop_List_3.append(Treasure("Gold"))
##Gear##
Wood_Sword = Gear("Wood Sword")
Silver_Sword = Gear("Silver Sword")
Gold_Sword = Gear("Gold Sword")
Excalibur_Sword = Gear("Excalibur")
Ultima_Weapon = Gear("Ultima Weapon")
Wood_Armor = Gear("Wood Armor")
Silver_Armor = Gear("Silver Armor")
Gold_Armor = Gear("Gold Armor")
Armor_Of_Darkness = Gear("Armor Of Darkness")
Holy_Armor = Gear("Holy Armor")
Emerald_Armor = Gear("Emerald Armor")
Mythril_Sword = Gear("Mythril Sword")
Athenas_Bow = Gear("Athena's Bow")
Holy_Blade = Gear("Holy Blade")
Hades_Staff = Gear("Hade's Staff")
##Shop Items##
#Sword = Shop("Sword")
#Exit = Shop("Exit")
##SHOP DICTIONARY##
Shop_List = {"Wood Sword" : 10, \
             "Silver Sword" : 50, \
             "Gold Sword" : 125, \
             "Wood Armor" : 15 , \
             "Silver Armor" : 60, \
             "Gold Armor" : 150 \
             }
##SHOP DICTIONARY 2##
Shop_List_2 = {"Holy Armor" : 1000, \
             "Excalibur" : 1200, \
             "Gold Sword" : 125, \
             "Gold Armor" : 150 \
             }
##RANDOM TAUNT LIST##
Random_Taunt_List = ["You laugh at how easy that was.", "You spit on the dead foe!", "That was easy.", "You do a little dance to celebrate your victory!", "This is the greatest game you've ever played!", "Your power can only grow", "Power Overwhelming", "Omnislash!", "Cloud has nothing on me", "Thanks Obama."]
Random_Defend = ["Hit", "Miss"]

##MY_STATS##

##DEVELOPER STATS##
Dev_Stats_1 = {"Level" : 100, \
                   "Power" : 4000, \
                 "Health" : 9999, \
                   "EXP" : 0, \
                   }

##Level 1 Stats##
Warrior_Stats_1 = {"Level" : 1, \
                   "Power" : 75, \
                 "Health" : 100, \
                   "EXP" : 0, \
                   }
Hunter_Stats_1 = {"Level" : 1, \
                  "Power" : 85, \
                 "Health" : 85, \
                  "EXP" : 0 \
                 }
Mage_Stats_1 = {"Level" : 1, \
                "Power" : 100, \
                 "Health" : 75, \
                  "EXP" : 0 \
                 }
##Level 2 Stats##
Warrior_Stats_2 = {"Level" : 2, \
                   "Power" : 100, \
                 "Health" : 125, \
                  "EXP" : 0 \
                 }
Hunter_Stats_2 = {"Level" : 2, \
                  "Power" : 110, \
                 "Health" : 110, \
                  "EXP" : 0 \
                 }
Mage_Stats_2 = {"Level" : 2, \
                "Power" : 125, \
                 "Health" : 100, \
                  "EXP" : 0 \
                }
##Level 3 Stats##
Warrior_Stats_3 = {"Level" : 3, \
                   "Power" : 150, \
                 "Health" : 200, \
                  "EXP" : 0 \
                 }
Hunter_Stats_3 = {"Level" : 3, \
                  "Power" : 175, \
                 "Health" : 175, \
                  "EXP" : 0 \
                 }
Mage_Stats_3 = {"Level" : 3, \
                "Power" : 200, \
                 "Health" : 150, \
                  "EXP" : 0 \
                }
##Level 4 Stats##
Warrior_Stats_4 = {"Level" : 4, \
                   "Power" : 225, \
                 "Health" : 325, \
                  "EXP" : 0 \
                 }
Hunter_Stats_4 = {"Level" : 4, \
                  "Power" : 275, \
                 "Health" : 275, \
                  "EXP" : 0 \
                 }
Mage_Stats_4 = {"Level" : 4, \
                "Power" : 325, \
                 "Health" : 225, \
                  "EXP" : 0 \
                 }
##Level 5 Stats##
Warrior_Stats_5 = {"Level" : 5, \
                   "Power" : 300, \
                 "Health" : 400, \
                  "EXP" : 0 \
                 }
Hunter_Stats_5 = {"Level" : 5, \
                  "Power" : 355, \
                 "Health" : 355, \
                  "EXP" : 0 \
                 }
Mage_Stats_5 = {"Level" : 5, \
                "Power" : 400, \
                 "Health" : 300, \
                  "EXP" : 0 \
                }
##Level 6 Stats##
Warrior_Stats_6 = {"Level" : 6, \
                   "Power" : 375, \
                 "Health" : 500, \
                  "EXP" : 0 \
                 }
Hunter_Stats_6 = {"Level" : 6, \
                  "Power" : 425, \
                 "Health" : 425, \
                  "EXP" : 0 \
                 }
Mage_Stats_6 = {"Level" : 6, \
                "Power" : 500, \
                 "Health" : 375, \
                  "EXP" : 0 \
                }
##Level 7 Stats##
Warrior_Stats_7 = {"Level" : 7, \
                   "Power" : 425, \
                 "Health" : 600, \
                  "EXP" : 0 \
                 }
Hunter_Stats_7 = {"Level" : 7, \
                  "Power" : 500, \
                 "Health" : 500, \
                  "EXP" : 0 \
                 }
Mage_Stats_7 = {"Level" : 7, \
                "Power" : 600, \
                 "Health" : 425, \
                  "EXP" : 0 \
                 }
##Level 8 Stats##
Warrior_Stats_8 = {"Level" : 8, \
                   "Power" : 550, \
                 "Health" : 800, \
                  "EXP" : 0 \
                 }
Hunter_Stats_8 = {"Level" : 8, \
                  "Power" : 675, \
                 "Health" : 675, \
                  "EXP" : 0 \
                 }
Mage_Stats_8 = {"Level" : 8, \
                "Power" : 800, \
                 "Health" : 550, \
                  "EXP" : 0 \
                 }
##Level 9 Stats##
Warrior_Stats_9 = {"Level" : 9, \
                   "Power" : 700, \
                 "Health" : 1000, \
                  "EXP" : 0 \
                 }
Hunter_Stats_9 = {"Level" : 9, \
                  "Power" : 850, \
                 "Health" : 850, \
                  "EXP" : 0 \
                 }
Mage_Stats_9 = {"Level" : 9, \
                "Power" : 1000, \
                 "Health" : 700, \
                  "EXP" : 0 \
                 }
##Level 10 Stats##
Warrior_Stats_10 = {"Level" : 10, \
                   "Power" : 900, \
                 "Health" : 1300, \
                  "EXP" : 0 \
                 }
Hunter_Stats_10 = {"Level" : 10, \
                  "Power" : 1000, \
                 "Health" : 1000, \
                  "EXP" : 0 \
                 }
Mage_Stats_10 = {"Level" : 10, \
                "Power" : 1300, \
                 "Health" : 900, \
                  "EXP" : 0 \
                 }
##Level 11 Stats##
Warrior_Stats_11 = {"Level" : 11, \
                   "Power" : 1100, \
                 "Health" : 1500, \
                  "EXP" : 0 \
                 }
Hunter_Stats_11 = {"Level" : 11, \
                  "Power" : 1250, \
                 "Health" : 1250, \
                  "EXP" : 0 \
                 }
Mage_Stats_11 = {"Level" : 11, \
                "Power" : 1500, \
                 "Health" : 1100, \
                  "EXP" : 0 \
                 }
##Level 12 Stats##
Warrior_Stats_12 = {"Level" : 12, \
                   "Power" : 1400, \
                 "Health" : 1750, \
                  "EXP" : 0 \
                 }
Hunter_Stats_12 = {"Level" : 12, \
                  "Power" : 1550, \
                 "Health" : 1550, \
                  "EXP" : 0 \
                 }
Mage_Stats_12 = {"Level" : 12, \
                "Power" : 1750, \
                 "Health" : 1400, \
                  "EXP" : 0 \
                 }
##Level 13 Stats##
Warrior_Stats_13 = {"Level" : 13, \
                   "Power" : 1600, \
                 "Health" : 2000, \
                  "EXP" : 0 \
                 }
Hunter_Stats_13 = {"Level" : 13, \
                  "Power" : 1750, \
                 "Health" : 1750, \
                  "EXP" : 0 \
                 }
Mage_Stats_13 = {"Level" : 13, \
                "Power" : 2000, \
                 "Health" : 1600, \
                  "EXP" : 0 \
                 }
##Level 14 Stats##
Warrior_Stats_14 = {"Level" : 14, \
                   "Power" : 1800, \
                 "Health" : 2300, \
                  "EXP" : 0 \
                 }
Hunter_Stats_14 = {"Level" : 14, \
                  "Power" : 2000, \
                 "Health" : 2000, \
                  "EXP" : 0 \
                 }
Mage_Stats_14 = {"Level" : 14, \
                "Power" : 2300, \
                 "Health" : 1800, \
                  "EXP" : 0 \
                 }
##Level 15 Stats##
Holy_Knight_Stats_1 = {"Level" : 15, \
                   "Power" : 3000, \
                 "Health" : 4000, \
                  "EXP" : 0 \
                 }
Ranger_Stats_1 = {"Level" : 15, \
                  "Power" : 3500, \
                 "Health" : 3500, \
                  "EXP" : 0 \
                 }
Warlock_Stats_1 = {"Level" : 15, \
                "Power" : 4000, \
                 "Health" : 3000, \
                  "EXP" : 0 \
                 }
##Monster Stats##
Goblin = {"Level" : 1, \
          "Power" : 10, \
          "Health" : 150 \
          }
Bat = {"Level" : 1, \
          "Power" : 15, \
          "Health" : 50 \
          }

##NAME CHARACTER FUNCTION##
def name_character(choice):
    char_name = ""
    if choice == Warrior:
        char_name = raw_input("\nPlease name your Warrior!: ")
    elif choice == Hunter:
        char_name = raw_input("\nPlease name your Hunter!: ")
    elif choice == Mage:
        char_name = raw_input("\nPlease name your Mage!: ")
    elif choice == Dev:
        char_name = raw_input("\nPlease name your so called Developer: ")
    elif choice == Upgrade:
        char_name = raw_input("\nPlease name your so called Upgrader: ")
    return char_name
##CHOOSE LOCATION FUNCTION##
def begin_quest(player_1):
    current_location = ""
    global my_stats
    global my_damage
    global my_health
    global name
    global Class_Choice
    global inventory
    global equipped_weapon
    global equipped_armor
    global player_status
    if player_1 == 1 or action == Travel:
        while current_location.lower() != "forest" or "dungeon" or "mountains" or "shop" or "equip":
            print "\nPlease choose where you would like to go!"
            print "[Forest][Dungeon][Mountains][Shop][Equip][Stats][Inventory][Save][Load]"
            current_location = raw_input(":")
            if current_location.lower() == "forest":
                print "You have entered the dark forest!"
                current_location = Forest
                return current_location
                break
            elif current_location.lower() == "dungeon":
                print "You have descended into the stench filled dungeons!"
                current_location = Dungeon
                return current_location
                break
            elif current_location.lower() == "mountains":
                print "You have begun to climb the snow capped mountains!"
                current_location = Mountains
                return current_location
                break
            elif current_location.lower() == "equip":
                print "Time to equip!"
                current_location = Equipment
                return current_location
                break
            elif current_location.lower() == "stats":
                print "My Character: \n" + str(my_stats)
                if my_stats["Level"] == 15:
                    print str(upgraded_class)
                    print "Name: " + str(name)
                    print "Equipped Weapon: " + str(equipped_weapon)
                    print "+Weapon Power: " + str(my_damage)
                    print "Equipped Armor: " + str(equipped_armor)
                    print "+Armor Health: " + str(my_health)   
                else:
                    print "Class: " + str(Class_Choice)
                    print "Name: " + str(name)
                    print "Equipped Weapon: " + str(equipped_weapon)
                    print "+Weapon Power: " + str(my_damage)
                    print "Equipped Armor: " + str(equipped_armor)
                    print "+Armor Health: " + str(my_health)
                    
                
            elif current_location.lower() == "inventory":
                print "Inventory: \n" + str(inventory)
            elif current_location.lower() == "dev":
                print "Developer"
                inventory["Gold"] += 1000
                inventory["Emerald"] += 1000
            elif current_location.lower() == "save":
                print "Game Saved!"
                shelfFile = shelve.open('HRPG_saved_game')
                shelfFile['mystatsVariable'] = my_stats
                shelfFile['mydamageVariable'] = my_damage
                shelfFile['myhealthVariable'] = my_health
                shelfFile['inventoryVariable'] = inventory
                shelfFile['eweaponVariable'] = equipped_weapon
                shelfFile['earmorVariable'] = equipped_armor
                shelfFile['playerstatusVariable'] = player_status
                shelfFile['classchoiceVariable'] = Class_Choice
                shelfFile['nameVariable'] = name
                shelfFile.close()
            elif current_location.lower() == "load":
                print "Game Loaded!"
                shelfFile = shelve.open('HRPG_saved_game')
                my_stats = shelfFile ['mystatsVariable']
                my_damage = shelfFile ['mydamageVariable']
                my_health = shelfFile ['myhealthVariable']
                inventory = shelfFile ['inventoryVariable']
                equipped_weapon = shelfFile ['eweaponVariable']
                equipped_armor = shelfFile ['earmorVariable']
                player_status = shelfFile ['playerstatusVariable']
                Class_Choice = shelfFile ['classchoiceVariable']
                name = shelfFile ['nameVariable']
                shelfFile.close()
              
            elif current_location.lower() == "shop":
                print "You travel to the shop."
                print "\nWelcome to the shop!"
                current_location = Shop
                return current_location        
            else:
                print "You didn't choose an actual location!"
##EQUIP FUNCTION##
def equip(current_location):
    if current_location == Equipment:
        equipment = ""
        action = ""
        print inventory
        print "[Armor][Weapon][Exit]"
        armor_or_weapon = raw_input(":")
        while armor_or_weapon.lower() != "armor" or "weapon" or "exit":
            if armor_or_weapon.lower() == "armor":
                global equipped_armor
                equip_choice = raw_input("\nWhat would you like to equip?")
                if equip_choice.lower() == "wood armor":
                
                    if "Wood Armor" in inventory:
                        if inventory["Wood Armor"] >= 1:
                            print "Equipped Wood Armor!" 
                            equipped_armor = str(Wood_Armor)
                            inventory.pop("Wood Armor")
                            print "\nEquipped Armor: " + str(equipped_armor)
                            return equipped_armor
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "silver armor":
                    if "Silver Armor" in inventory:
                        if inventory["Silver Armor"] >= 1:
                            print "Equipped Silver Armor!" 
                            equipped_armor = str(Silver_Armor)
                            inventory.pop("Silver Armor")
                            print "\nEquipped Armor: " + str(equipped_armor)
                            return equipped_armor
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "gold armor":
                    if "Gold Armor" in inventory:
                        if inventory["Gold Armor"] >= 1:
                            print "Equipped Gold Armor!" 
                            equipped_armor = str(Gold_Armor)
                            inventory.pop("Gold Armor")
                            print "\nEquipped Armor: " + str(equipped_armor)
                            return equipped_armor
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "armor of darkness":
                    if "Armor Of Darkness" in inventory:
                        if inventory["Armor Of Darkness"] >= 1:
                            print "Equipped Armor Of Darkness!" 
                            equipped_armor = str(Armor_Of_Darkness)
                            inventory.pop("Armor Of Darkness")
                            print "\nEquipped Armor: " + str(equipped_armor)
                            return equipped_armor
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "holy armor":
                    if "Holy Armor" in inventory:
                        if inventory["Holy Armor"] >= 1:
                            print "Equipped Holy Armor!"
                            print "You are God Like!"
                            equipped_armor = str(Holy_Armor)
                            inventory.pop("Holy Armor")
                            print "\nEquipped Armor: " + str(equipped_armor)
                            return equipped_armor
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "exit":
                    armor_or_weapon = ""
                    return armor_or_weapon
            if armor_or_weapon.lower() == "weapon":
                global equipped_weapon
                
                equip_choice = raw_input("\nWhat would you like to equip?")
                if equip_choice.lower() == "wood sword":
                    if "Wood Sword" in inventory:
                        print "Equipped Wood Sword!" 
                        inventory.pop("Wood Sword")
                        equipped_weapon = str(Wood_Sword)                  
                        print "Equipped Weapon: " + str(equipped_weapon)
                        return equipped_weapon
                if equip_choice.lower() == "silver sword":
                    if "Silver Sword" in inventory:
                        print "Equipped Silver Sword!"                       
                        inventory.pop("Silver Sword")
                        equipped_weapon = str(Silver_Sword)         
                        print "Equipped Weapon: " + str(equipped_weapon)
                        return equipped_weapon
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "gold sword":
                    if "Gold Sword" in inventory:
                        print "Equipped Gold Sword!"                       
                        inventory.pop("Gold Sword")
                        equipped_weapon = str(Gold_Sword)         
                        print "Equipped Weapon: " + str(equipped_weapon)
                        return equipped_weapon
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "excalibur":
                    if "Excalibur" in inventory:
                        print "Equipped Excalibur!"                       
                        inventory.pop("Excalibur")
                        equipped_weapon = str(Excalibur_Sword)         
                        print "Equipped Weapon: " + str(equipped_weapon)
                        return equipped_weapon
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "mythril sword":
                    if "Mythril Sword" in inventory:
                        print "Equipped Mythril Sword!"                       
                        inventory.pop("Mythril Sword")
                        equipped_weapon = str(Mythril_Sword)         
                        print "Equipped Weapon: " + str(equipped_weapon)
                        return equipped_weapon
                    else:
                        print "You don't have that!"
                if equip_choice.lower() == "ultima weapon":
                    if "Ultima Weapon" in inventory:
                        print "Equipped Ultima Weapon!"
                        print "You are God Like!"
                        inventory.pop("Ultima Weapon")
                        equipped_weapon = str(Ultima_Weapon)         
                        print "Equipped Weapon: " + str(equipped_weapon)
                        return equipped_weapon
                    else:
                        print "You don't have that!"
                
                    
                if equip_choice.lower() == "exit":
                    armor_or_weapon = ""
            if armor_or_weapon.lower() == "exit":
                print "Left Equipment" 
                action = Travel
                return action
            else:
                print "Please choose an action!"
                break
                
                        

##SHOP FUNCTION##
def shopping(current_location):
    if current_location == Shop:
        shop_choice = ""
        action = "" 
        while action != Travel:                                        
            if my_stats["Level"] >= 10:
                print "\nYou're ready for some better gear!"
                print "[Hidden Shop]"
                print str(Shop_List_2)
                shop_choice = raw_input("Choice: ")                       
                if shop_choice.lower() == "holy armor" and inventory["Gold"] >= 1000:
                    print "The rarest armor in the land!" + "\n[Purchased Holy Armor]" 
                    shop_choice = str(Holy_Armor)
                    inventory["Gold"] -= 1000
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1                   
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "excalibur" and inventory["Gold"] >= 1200:
                    print "The fallen king's own blade, Exaclibur is yours! 1,200 gold please." + "\n[Purchased Excalibur]" 
                    shop_choice = str(Excalibur_Sword)
                    inventory["Gold"] -= 1200
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "gold sword" and inventory["Gold"] >= 125:
                    print "Pure Gold! 125 gold for me that is!" + "\n[Purchased Gold Sword]" 
                    shop_choice = str(Gold_Sword)
                    inventory["Gold"] -= 125
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "gold armor" and inventory["Gold"] >= 150:
                    print "Royalty, you are! 150 smackaroons to me!" + "\n[Purchased Gold Armor]" 
                    shop_choice = str(Gold_Armor)
                    inventory["Gold"] -= 150
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "exit":
                    print "See you soon!" 
                    action = Travel
                    return action
                else:
                    print "Ask for something you can afford!"


            elif my_stats["Level"] < 10:
                print "\nWhat would you like? \n" + "Available: " + str(Shop_List)
                shop_choice = raw_input("Choice: ")                       
                if shop_choice.lower() == "potion" and inventory["Gold"] >= 5:
                    print "That will be 5 gold please!" + "\n[Purchased Potion]" 
                    shop_choice = str(Potion)
                    inventory["Gold"] -= 5
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1                   
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "wood sword" and inventory["Gold"] >= 10:
                    print "10 gold should do the trick!" + "\n[Purchased Wooden Sword]" 
                    shop_choice = str(Wood_Sword)
                    inventory["Gold"] -= 10
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "wood armor" and inventory["Gold"] >= 15:
                    print "15 gold this way!" + "\n[Purchased Wood Armor]" 
                    shop_choice = str(Wood_Armor)
                    inventory["Gold"] -= 15
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "silver sword" and inventory["Gold"] >= 50:
                    print "Ooh a fine item! 50 gold please!" + "\n[Purchased Silver Sword]" 
                    shop_choice = str(Silver_Sword)
                    inventory["Gold"] -= 50
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "gold sword" and inventory["Gold"] >= 125:
                    print "Pure Gold! 125 gold for me that is!" + "\n[Purchased Gold Sword]" 
                    shop_choice = str(Gold_Sword)
                    inventory["Gold"] -= 125
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "silver armor" and inventory["Gold"] >= 60:
                    print "You'll look super cool! 60 gold this way!" + "\n[Purchased Silver Armor]" 
                    shop_choice = str(Silver_Armor)
                    inventory["Gold"] -= 60
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "gold armor" and inventory["Gold"] >= 150:
                    print "Royalty, you are! 150 smackaroons to me!" + "\n[Purchased Gold Armor]" 
                    shop_choice = str(Gold_Armor)
                    inventory["Gold"] -= 150
                    inventory[shop_choice] = inventory.setdefault(shop_choice, 0) + 1
                    print "Inventory: " + str(inventory)
                    return shop_choice
                elif shop_choice.lower() == "exit":
                    print "See you soon!" 
                    action = Travel
                    return action           
                else:
                    print "Ask for something you can afford!"
##In Quest Forest(Define actions, and based on location, actions are changed##
def in_quest_forest(Current_loc):
    if Current_loc == Forest:
        action = ""
        while action.lower() != "explore" or "travel" or "exit":
            print "\nThe forest is thick and the trees bend in the wind. What would you like to do?"
            print "[Explore][Travel]"
            action = raw_input("\nChoice: ")
            if action.lower() == "explore": ##EXPLORE##
                print "You explore the dark forest!"
                action = Explore
                return action
                break
            elif action.lower() == "travel": ##TRAVEL / LEAVE##
                print "You have decided to leave the forest."
                action = Travel
                return action
                break
            else:
                print "\nPlease choose an action!"
##IN Quest Dungeon##
def in_quest_dungeon(Current_loc):
    if Current_loc == Dungeon:
        action = ""
        while action.lower() != "explore" or "travel" or "exit":
            print "\nThe darkness surrounds you, and noises come from unseen places. What would you like to do?"
            print "[Explore][Travel]"
            action = raw_input("\nChoice: ")
            if action.lower() == "explore": ##EXPLORE##
                print "You have descended into the stench filled dungeon!"
                action = Explore
                return action
                break
            elif action.lower() == "travel": ##TRAVEL / LEAVE##
                print "You have decided to leave the dungeon."
                action = Travel
                return action
                break
            else:
                print "\nPlease choose an action!"
##In Quest Mountains
def in_quest_mountains(Current_loc):
    if Current_loc == Mountains:
        action = ""
        while action.lower() != "explore" or "travel" or "exit":
            print "\nThe mountains tower over you and the air is frosty. You've heard rumors that Svelenor resides at it's peaks. What would you like to do?"
            print "WARNING : High Level Monsters!"
            print "\n[Explore][Travel]"
            action = raw_input("\nChoice: ")
            if action.lower() == "explore": ##EXPLORE##
                print "You have begun to climb the snow capped mountains!"
                action = Explore
                return action
                break
            elif action.lower() == "travel": ##TRAVEL / LEAVE##
                print "You have decided to descend from the mountains."
                action = Travel
                return action
                break
            else:
                print "\nPlease choose an action!"
##TEST creating dictionary items##
def create_in_inventory(item):
    my_dict[key] = my_dict.setdefault(key, 0) + 1
##TRAVEL FUNCTION (UNUSED)##
def travel(action):
        begin_quest(player_status)

##EXPLORE FUNCTION##
def explore(action):
    if action == Explore:
        explore_result = random.choice(Random_Explore)
        return explore_result
##FIND TREASURE##    
def treasure(explore_result):
    if explore_result == "Treasure!":
        treasure_found = str(random.choice(Treasure_List_1))
        print "You have discovered " + str(treasure_found) + "!"
        random_gold = random.randrange(1,50)
        inventory[treasure_found] = inventory.setdefault(treasure_found, 0) + random_gold
        print inventory
        return treasure_found
##FIGHT!##
    ##FOREST FIGHT##
        ##FIGHT GOBLIN##
def fight(explore_result):
    if explore_result == "Fight!" and current_location == Forest:
        global my_health
        global player_status
        fight_begin = random.choice(Monster_List_1)
        print "You have encountered a " + str(fight_begin) + "!"
        if fight_begin is Monster_List_1[0]:
            battle_choice = ""
            goblin_health = 175
            goblin_power = 15
            goblin_exp = 30
            
            print "The Goblin approaches you, a bloody knife in his hand."
            print "Health: " + str(goblin_health)
            print "\n[Attack][Defend][Run]"
            while goblin_health >= 1 and my_health >= 1:
                battle_choice = raw_input("\nWhat do you do?")
                if battle_choice.lower() == "attack":
                    print "You Attack!"
                    hit_miss = random.randrange(1,10)
                    if hit_miss >= 3:
                        print str(my_damage) + " Damage!"
                        goblin_health -= my_damage
                        print "Goblin Health: " + str(goblin_health)
                        if goblin_health >= 1:
                            print "\nThe Goblin Attacks!"
                            print str(goblin_power) + " Damage!"
                            my_health -= goblin_power
                            print "Your Health: " + str(my_health)
                            
                    else:
                        print "Your attack misses!"
                        print "\nThe Goblin Attacks!"
                        print str(goblin_power) + " Damage!"
                        my_health -= goblin_power
                        print "Your Health: " + str(my_health)
                        
                        
                        
                elif battle_choice.lower() == "defend":
                    print "The Goblin attacks! He does 0 damage!"
                elif battle_choice.lower() == "run":
                    escape_or_no = random.randrange(1,10)
                    if escape_or_no >= 4:
                        print "You escape!"
                        return battle_choice
                    else:
                        print "You cannot escape!"
                        print "\nThe Goblin Attacks!"
                        print str(goblin_power) + " Damage!"
                        my_health -= goblin_power
                        print "Your Health: " + str(my_health)
            if goblin_health <=0:
                print "\nYou have defeated the Goblin!"
                random_drop = random.randrange(1,10)
                if random_drop >= 7:                        
                    random_drop = str(random.choice(Drop_List_1))
                    random_amount = random.randrange(1,8)
                    print "You have discovered: " + str(random_drop)
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + random_amount
                elif random_drop == 1:
                    random_drop = str("Silver Sword")
                    print "You have found a Silver Sword!"
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + 1
                my_stats["EXP"] += goblin_exp
                print "EXP Gained: " + str(goblin_exp)
                print "Your EXP: " + str(my_stats["EXP"])
                print random.choice(Random_Taunt_List)
                return battle_choice
            elif my_health <= 0:
                print "You have died."
                print "\n GAME OVER"
                player_status = complete
                return player_status
                exit      
##FOREST FIGHT##
    ##FIGHT BAT##
        elif fight_begin is Monster_List_1[1]:
            battle_choice = ""
            bat_health = 75
            bat_power = 20
            bat_exp = 15
            
            print "A Bat with large fangs flutters down from the trees and lands in front of you, hunger in its eyes."
            print "Health: " + str(bat_health)
            print "\n[Attack][Defend][Run]"
            while bat_health >= 1 and my_health >= 1:
                battle_choice = raw_input("\nWhat do you do?")
                if battle_choice.lower() == "attack":
                    print "You Attack!"
                    hit_miss = random.randrange(1,10)
                    if hit_miss >= 3:
                        print str(my_stats["Power"]) + " Damage!"
                        bat_health -= my_damage
                        print "Bat Health: " + str(bat_health)
                        if bat_health >=1:
                            print "\nThe Bat Attacks!"
                            print str(bat_power) + " Damage!"
                            my_health -= bat_power
                            print "Your Health: " + str(my_health)
                    else:
                        print "Your attack misses!"
                        print "\nThe Bat Attacks!"
                        print str(bat_power) + " Damage!"
                        my_health -= bat_power
                        print "Your Health: " + str(my_health)
                elif battle_choice.lower() == "defend":
                    print "The Bat attacks! It does 0 damage!"
                elif battle_choice.lower() == "run":
                    escape_or_no = random.randrange(1,10)
                    if escape_or_no >= 4:
                        print "You escape!"
                        return battle_choice
                    else:
                        print "You cannot escape!"
                        print "\nThe Bat Attacks!"
                        print str(bat_power) + " Damage!"
                        my_health -= bat_power
                        print "Your Health: " + str(my_health)
            if bat_health <= 0:
                print "\nYou have slain the Bat!"
                random_drop = random.randrange(1,10)
                if random_drop >= 7:                        
                    random_drop = str(random.choice(Drop_List_1))
                    random_amount = random.randrange(1,5)
                    print "You have discovered: " + str(random_drop)
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + random_amount
                my_stats["EXP"] += bat_exp
                print "EXP Gained: " + str(bat_exp)
                print "Your EXP: " + str(my_stats["EXP"])
                print random.choice(Random_Taunt_List)
                return battle_choice
            elif my_health <= 0:
                print "You have died."
                print "\n GAME OVER"
                player_status = complete
                return player_status
                exit      
##DUNGEON FIGHT##
    ##FIGHT TROLL##
    elif explore_result == "Fight!" and current_location == Dungeon:
        fight_begin = random.choice(Monster_List_2)
        print "You have encountered a " + str(fight_begin) + "!"
        if fight_begin is Monster_List_2[0]:
            battle_choice = ""
            troll_health = 300
            troll_power = 65
            troll_exp = 85
            
            print "The ground rumbles and a massive Troll rounds the corner."
            print "Health: " + str(troll_health)
            print "\n[Attack][Defend][Run]"
            while troll_health >= 1 and my_health >= 1:
                battle_choice = raw_input("\nWhat do you do?")
                if battle_choice.lower() == "attack":
                    print "You Attack!"
                    hit_miss = random.randrange(1,10)
                    if hit_miss >= 3:
                        print str(my_damage) + " Damage!"
                        troll_health -= my_damage
                        print "Troll Health: " + str(troll_health)
                        if troll_health >= 1:
                            print "\nThe Troll Swings his mighty club!"
                            print str(troll_power) + " Damage!"
                            my_health -= troll_power
                            print "Your Health: " + str(my_health)
                    else:
                        print "Your attack misses!"
                        print "\nThe Troll Attacks!"
                        print str(troll_power) + " Damage!"
                        my_health -= troll_power
                        print "Your Health: " + str(my_health)
                    
                elif battle_choice.lower() == "defend":
                    print "The Troll attacks! He does 0 damage!"
                elif battle_choice.lower() == "run":
                    escape_or_no = random.randrange(1,10)
                    if escape_or_no >= 4:
                        print "You escape!"
                        return battle_choice
                    else:
                        print "You cannot escape!"
                        print "\nThe Troll Attacks!"
                        print str(troll_power) + " Damage!"
                        my_health -= troll_power
                        print "Your Health: " + str(my_health)
            if troll_health <=0:
                print "\nYou have conquered the troll!"
                random_drop = random.randrange(1,10)
                if random_drop >= 7:                        
                    random_drop = str(random.choice(Drop_List_2))
                    random_amount = random.randrange(30,60)
                    print "You have discovered: " + str(random_drop)
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + random_amount
                elif random_drop == 1:
                    random_drop = str("Mythril Sword")
                    print "You have discovered a Mythril Sword!"
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + 1
                my_stats["EXP"] += troll_exp
                print "EXP Gained: " + str(troll_exp)
                print "Your EXP: " + str(my_stats["EXP"])
                print random.choice(Random_Taunt_List)
                return battle_choice
            elif my_health <= 0:
                print "You have died."
                print "\n GAME OVER"
                player_status = complete
                return player_status
                exit      
##DUNGEON FIGHT##
    ##FIGHT SKELETON##
        elif fight_begin is Monster_List_2[1]:
            battle_choice = ""
            skeleton_health = 275
            skeleton_power = 40
            skeleton_exp = 60
            
            print "Bones creak and dust scatters as a Skeleton corpse stands."
            print "Health: " + str(skeleton_health)
            print "\n[Attack][Defend][Run]"
            while skeleton_health >= 1 and my_health >= 1:
                battle_choice = raw_input("\nWhat do you do?")
                if battle_choice.lower() == "attack":
                    print "You Attack!"
                    hit_miss = random.randrange(1,10)
                    if hit_miss >= 3:
                        print str(my_damage) + " Damage!"
                        skeleton_health -= my_damage
                        print "Skeleton Health: " + str(skeleton_health)
                        if skeleton_health >= 1:
                            print "\nThe Skeleton's rusted axes come flying at you!"
                            print str(skeleton_power) + " Damage!"
                            my_health -= skeleton_power
                            print "Your Health: " + str(my_health)
                    else:
                        print "Your attack misses!"
                        print "\nThe Skeleton Attacks!"
                        print str(skeleton_power) + " Damage!"
                        my_health -= skeleton_power
                        print "Your Health: " + str(my_health)
                    
                elif battle_choice.lower() == "defend":
                    print "The Skeleton attacks! He does 0 damage!"
                elif battle_choice.lower() == "run":
                    escape_or_no = random.randrange(25,50)
                    if escape_or_no >= 4:
                        print "You escape!"
                        return battle_choice
                    else:
                        print "Your cannot escape!"
                        print "\nThe Skeleton Attacks!"
                        print str(skeleton_power) + " Damage!"
                        my_health -= skeleton_power
                        print "Your Health: " + str(my_health)
            if skeleton_health <=0:
                print "\nYou have conquered the troll!"
                random_drop = random.randrange(1,10)
                if random_drop >= 7:                        
                    random_drop = str(random.choice(Drop_List_2))
                    random_amount = random.randrange(5,15)
                    print "You have discovered: " + str(random_drop)
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + random_amount
                elif random_drop == 1:
                    random_drop = str("Armor Of Darkness")
                    print "You feel the darkness eminating from the suit of black armor" 
                    print "You have discovered Armor Of Darkness!"
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + 1
                    
                my_stats["EXP"] += skeleton_exp
                print "EXP Gained: " + str(skeleton_exp)
                print "Your EXP: " + str(my_stats["EXP"])
                print random.choice(Random_Taunt_List)
                return battle_choice
            elif my_health <= 0:
                print "You have died."
                print "\n GAME OVER"
                player_status = complete
                return player_status
                exit      
##Mountain FIGHT##
    ##FIGHT Barbarian##
    elif explore_result == "Fight!" and current_location == Mountains:
        fight_begin = random.choice(Monster_List_3)
        print "You have encountered a " + str(fight_begin) + "!"
        if fight_begin is Monster_List_3[0]:
            battle_choice = ""
            barb_health = 1500
            barb_power = 250
            barb_exp = 200
            
            print "Warcries break the silence and a Barbarian, weilding two axes steps out from behind a rock to challenge you."
            print "Health: " + str(barb_health)
            print "\n[Attack][Defend][Run]"
            while barb_health >= 1 and my_health >= 1:
                battle_choice = raw_input("\nWhat do you do?")
                if battle_choice.lower() == "attack":
                    print "You Attack!"
                    hit_miss = random.randrange(1,10)
                    if hit_miss >= 3:
                        print str(my_damage) + " Damage!"
                        barb_health -= my_damage
                        print "Barbarian Health: " + str(barb_health)
                        if barb_health >= 1:
                            print "\nThe Barbarian pounds his chest and lunges at you!"
                            print str(barb_power) + " Damage!"
                            my_health -= barb_power
                            print "Your Health: " + str(my_health)
                    else:
                        print "Your attack misses!"
                        print "\nThe Barbarian Attacks!"
                        print str(barb_power) + " Damage!"
                        my_health -= barb_power
                        print "Your Health: " + str(my_health)
                    
                elif battle_choice.lower() == "defend":
                    print "The Barbarian attacks! He does 0 damage!"
                elif battle_choice.lower() == "run":
                    escape_or_no = random.randrange(1,10)
                    if escape_or_no >= 5:
                        print "You escape!"
                        return battle_choice
                    else:
                        print "Your cannot escape!"
                        print "\nThe Barbarian Attacks!"
                        print str(barb_power) + " Damage!"
                        my_health -= barb_power
                        print "Your Health: " + str(my_health)
            if barb_health <=0:
                print "\nYou have claimed victory over the Barbarian!"
                random_drop = random.randrange(1,100)
                if random_drop >= 10:                        
                    random_drop = str(random.choice(Drop_List_3))
                    random_amount = random.randrange(100,200)
                    print "You have discovered: " + str(random_drop)
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + random_amount
                elif random_drop == 1:
                    random_drop = str("Ultima Weapon")
                    print "You have discovered the legendary " + str(random_drop)
                    print "This will help you defeat Svelenor!"
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + 1
                        
                my_stats["EXP"] += barb_exp
                print "EXP Gained: " + str(barb_exp)
                print "Your EXP: " + str(my_stats["EXP"])
                print random.choice(Random_Taunt_List)
                return battle_choice
            elif my_health <= 0:
                print "You have died."
                print "\n GAME OVER"
                player_status = complete
                return player_status
                exit      
##Mountain Fight##
    ##SVELENOR, BOSS##
        elif fight_begin is Monster_List_3[1]:
            battle_choice = ""
            dragon_health = 15000
            dragon_power = 750
            dragon_exp = 1000
            global equipped_armor
            print "You hear a loud gust of wind, followed by an ear piercing screech. You turn your head as a massive shadow envelops you. Flying above you is the one you've been seeking. Svelenor! Emerald Dragon!"
            print "Health: " + str(dragon_health)
            if inventory["Emerald"] >= 1000:
                print "You have collected over 1000 Emeralds!"
                print "Emerald Armor Equipped!"
                equipped_armor = str(Emerald_Armor)
            print "\n[Attack][Defend][Run]"
            while dragon_health >= 1 and my_health >= 1:
                battle_choice = raw_input("\nWhat do you do?")
                if battle_choice.lower() == "attack":
                    print "You Attack!"
                    hit_miss = random.randrange(1,10)
                    if hit_miss >= 3:
                        print str(my_damage) + " Damage!"
                        dragon_health -= my_damage
                        print "Svelenor, Emerald Dragon Health: " + str(dragon_health)
                        if dragon_health >=1:
                            print "\nThe Dragon's breath erupts in scorching flame!"
                            if equipped_armor == str(Emerald_Armor):
                                print "The Emerald Armor blocks half of Svelenors damage!"
                                emerald_damage = dragon_power / 2
                                print str(emerald_damage) + " Damage!" 
                                my_health -= emerald_damage
                                print "Your Health: " + str(my_health)
                            else:
                                print str(dragon_power) + " Damage!"
                                my_health -= dragon_power
                                print "Your Health: " + str(my_health)
                    else:
                        print "Your attack misses!"
                        print "\nSvelenor Counter Attacks!"
                        print str(dragon_power) + " Damage!"
                        my_health -= dragon_power
                        print "Your Health: " + str(my_health)
                if battle_choice.lower() == "defend":
                    print "The Dragon attacks! It does 0 damage!"
                elif battle_choice.lower() == "run":
                    escape_or_no = random.randrange(1,10)
                    if escape_or_no >= 6:
                        print "You escape!"
                        return battle_choice
                    else:
                        print "Your cannot escape!"
                        print "\nSvelenor Attacks!"
                        print str(dragon_power) + " Damage!"
                        my_health -= dragon_power
                        print "Your Health: " + str(my_health)
            if dragon_health <= 0:
                print "\nIt's finally done! Svelenor has been slain! The world is free once more!"
                random_drop = random.randrange(1,10)
                if random_drop >= 7:                        
                    random_drop = str(random.choice(Drop_List_3))
                    print "You have discovered: " + str(random_drop)
                    inventory[random_drop] = inventory.setdefault(random_drop, 0) + 1
                my_stats["EXP"] += dragon_exp
                print "EXP Gained: " + str(dragon_exp)
                print "Your EXP: " + str(my_stats["EXP"])
                print random.choice(Random_Taunt_List)
                player_status = complete
                return player_status
            elif my_health <= 0:
                print "You have died."
                print "\n GAME OVER"
                player_status = complete
                return player_status
                exit                
                
        
   


    



                             ##GLOBAL CODE##
Class_Choice = ""
while Class_Choice.lower() != "warrior" or "hunter" or "mage" or "dev" or "upgrade":
    print "\n[Warrior][Hunter][Mage]"
    Class_Choice = raw_input("Please choose a class: ")
    if Class_Choice.lower() == "warrior":
        print "\nYou have chosen the mighty Warrior!"
        Class_Choice = Warrior
        break
    elif Class_Choice.lower() == "hunter":
        print "\nYou have chosen the skillful Hunter!"
        Class_Choice = Hunter
        break
    elif Class_Choice.lower() == "mage":
        print "\nYou have chosen the wise Mage!"
        Class_Choice = Mage
        break
    elif Class_Choice.lower() == "dev":
        print "\nYou better be a developer!"
        Class_Choice = Dev
        break
    elif Class_Choice.lower() == "upgrade":
        print "\ntime to test upgrade!"
        Class_Choice = Upgrade
        break
    elif Class_Choice.lower() == "info":
        print "Warrior - [Power: 75][Health: 100]"
        print "Hunter - [Power: 85][Health: 85]"
        print "Mage - [Power: 100][Health: 75]"
    else:
        print "\nYou didn't select an available class!"

##Sets name variable to your name##
name = name_character(Class_Choice)
##Assign Player to Class Choice and Name##
player = Character(Class_Choice, name)
player_level = 1
print "\nYou have named your character! \n" + str(player)

my_stats = {"Level" : 1, \
            "Power" : 0, \
            "Health" : 0, \
            "EXP" : 0 \
            }

##IFCLASSCHOICE##
if Class_Choice == Warrior:
    my_stats = Warrior_Stats_1
if Class_Choice == Hunter:
    my_stats = Hunter_Stats_1
if Class_Choice == Mage:
    my_stats = Mage_Stats_1
if Class_Choice == Dev:
    my_stats = Dev_Stats_1
if Class_Choice == Upgrade:
    my_stats = Mage_Stats_14
    my_stats["EXP"] = 2400
    
complete = ""
player_exp = 0
player_status = 1
monster_kill_count = 0
action = ""
explore_result = ""

##Weapons##
WoodSword = {"Power" : 35}
SilverSword = {"Power" : 75}
MythrilSword = {"Power" : 150}
GoldSword = {"Power" : 300}
ExcaliburSword = {"Power" : 750}
UltimaWeapon = {"Power" : 2000}
HolyBlade = {"Power" : 1500}
HadesStaff = {"Power" : 1500}
AthenasBow = {"Power" : 1500}
##Armor##
WoodArmor = {"Health" : 35}
SilverArmor = {"Health" : 80}
GoldArmor = {"Health" : 200}
ArmorOfDarkness = {"Health" : 400}
HolyArmor = {"Health" : 600}
EmeraldArmor = {"Health" : 1000}
##INVENTORY LIST##
inventory = {"Gold" : 0, "Emerald" : 0}
equipped_weapon = ["none"]
equipped_armor = ["none"]
my_damage = my_stats["Power"]
my_health = my_stats["Health"]
##MYEQUIPPEDWEAPON##
my_equipped_weapon = {}
##MYEQUIPPEDARMOR##
my_equipped_armor = {}




if player_status == 1:
        current_location = begin_quest(player_status)

                             ### MAIN LOOP ###
while player_status != complete:
## Moves to Action ##
    if current_location == Forest:
        player_status = 2
        action = in_quest_forest(current_location)
    if current_location == Dungeon:
        player_status = 2
        action = in_quest_dungeon(current_location)
    if current_location == Mountains:
        player_status = 2
        action = in_quest_mountains(current_location)
    if current_location == Shop:
        player_status = 2
        action = shopping(current_location)
    if current_location == Equipment:
        player_status = 2
        action = equip(current_location)
##Travels based on their action and starts quest again##       
    if action == Travel and player_status == 2:
        player_status = 1
        explore_result = 0
        current_location = begin_quest(player_status)
    if action == Explore and player_status == 2:
        player_status = 3
        explore_result = explore(action)
    if explore_result == "Treasure!":
        player_status = 4
        treasure_found = treasure(explore_result)
    if explore_result == "Fight!":
        player_status = 5
        battle_choice = fight(explore_result)
##LEVELS UP FROM 1 to 2##
    if my_stats["EXP"] >= 100 and my_stats["Level"] == 1:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_2
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_2
        if Class_Choice == Mage:
            my_stats = Mage_Stats_2 
        print my_stats
    if my_stats["EXP"] >= 200 and my_stats["Level"] == 2:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_3
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_3
        if Class_Choice == Mage:
            my_stats = Mage_Stats_3 
        print my_stats
    if my_stats["EXP"] >= 300 and my_stats["Level"] == 3:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_4
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_4
        if Class_Choice == Mage:
            my_stats = Mage_Stats_4 
        print my_stats
    if my_stats["EXP"] >= 400 and my_stats["Level"] == 4:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_5
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_5
        if Class_Choice == Mage:
            my_stats = Mage_Stats_5 
        print my_stats
    if my_stats["EXP"] >= 500 and my_stats["Level"] == 5:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_6
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_6
        if Class_Choice == Mage:
            my_stats = Mage_Stats_6 
        print my_stats
    if my_stats["EXP"] >= 600 and my_stats["Level"] == 6:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_7
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_7
        if Class_Choice == Mage:
            my_stats = Mage_Stats_7 
        print my_stats
    if my_stats["EXP"] >= 700 and my_stats["Level"] == 7:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_8
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_8
        if Class_Choice == Mage:
            my_stats = Mage_Stats_8 
        print my_stats
    if my_stats["EXP"] >= 800 and my_stats["Level"] == 8:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_9
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_9
        if Class_Choice == Mage:
            my_stats = Mage_Stats_9 
        print my_stats
    if my_stats["EXP"] >= 1000 and my_stats["Level"] == 9:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_10
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_10
        if Class_Choice == Mage:
            my_stats = Mage_Stats_10 
        print my_stats
    if my_stats["EXP"] >= 1200 and my_stats["Level"] == 10:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_11
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_11
        if Class_Choice == Mage:
            my_stats = Mage_Stats_11 
        print my_stats
    if my_stats["EXP"] >= 1500 and my_stats["Level"] == 11:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_12
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_12
        if Class_Choice == Mage:
            my_stats = Mage_Stats_12 
        print my_stats
    if my_stats["EXP"] >= 1750 and my_stats["Level"] == 12:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_13
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_13
        if Class_Choice == Mage:
            my_stats = Mage_Stats_13 
        print my_stats
    if my_stats["EXP"] >= 2000 and my_stats["Level"] == 13:
        print "You have leveled up! Congratulations."
        if Class_Choice == Warrior:
            my_stats = Warrior_Stats_14
        if Class_Choice == Hunter:
           my_stats = Hunter_Stats_14
        if Class_Choice == Mage:
            my_stats = Mage_Stats_14 
        print my_stats
    if my_stats["EXP"] >= 2500 and my_stats["Level"] == 14:
        print "You have reached level 15! Your class has now evolved!"
        if Class_Choice == Warrior:
            my_stats = Holy_Knight_Stats_1
            print "Your Warrior is now a Holy Knight!"
            upgraded_class = Holy_Knight
            print "You gain the Holy Blade!"
            equipped_weapon = str(Holy_Blade)
        if Class_Choice == Hunter:
            my_stats = Ranger_Stats_1
            print "Your Hunter is now a Ranger!"
            upgraded_class = Ranger
            print "You gain Athena's Bow!"
            equipped_weapon = str(Athenas_Bow)
        if Class_Choice == Mage:
            my_stats = Warlock_Stats_1
            print "Your Mage has become a Warlock!"
            upgraded_class = Warlock
            print "You gain Hade's Staff!"
            equipped_weapon = str(Hades_Staff)
        if Class_Choice == Upgrade:
            my_stats = Warlock_Stats_1
            print "Your Upgrade has become a Warlock!"
            upgraded_class = Warlock
            print "You gain Hade's Staff!"
            equipped_weapon = str(Hades_Staff)
        print my_stats
        
    if equipped_weapon == ["none"]:
        my_damage = my_stats["Power"]
    if equipped_weapon == str(Wood_Sword):
        my_damage = my_stats["Power"] + WoodSword["Power"]
    if equipped_weapon == str(Silver_Sword):
        my_damage = my_stats["Power"] + SilverSword["Power"]
    if equipped_weapon == str(Gold_Sword):
        my_damage = my_stats["Power"] + GoldSword["Power"]
    if equipped_weapon == str(Excalibur_Sword):
        my_damage = my_stats["Power"] + ExcaliburSword["Power"]
    if equipped_weapon == str(Ultima_Weapon):
       my_damage = my_stats["Power"] + UltimaWeapon["Power"]
    if equipped_weapon == str(Mythril_Sword):
       my_damage = my_stats["Power"] + MythrilSword["Power"]
    if equipped_weapon == str(Athenas_Bow):
       my_damage = my_stats["Power"] + AthenasBow["Power"]
    if equipped_weapon == str(Holy_Blade):
       my_damage = my_stats["Power"] + HolyBlade["Power"]
    if equipped_weapon == str(Hades_Staff):
       my_damage = my_stats["Power"] + HadesStaff["Power"]
    if equipped_armor == ["none"]:
        my_health = my_stats["Health"]
    if equipped_armor == str(Wood_Armor):
        my_health = my_stats["Health"] + WoodArmor["Health"]
    if equipped_armor == str(Silver_Armor):
        my_health = my_stats["Health"] + SilverArmor["Health"]
    if equipped_armor == str(Gold_Armor):
        my_health = my_stats["Health"] + GoldArmor["Health"]
    if equipped_armor == str(Armor_Of_Darkness):
        my_health = my_stats["Health"] + ArmorOfDarkness["Health"]
    if equipped_armor == str(Holy_Armor):
        my_health = my_stats["Health"] + HolyArmor["Health"]
    if equipped_armor == str(Emerald_Armor):
        my_health = my_stats["Health"] + EmeraldArmor["Health"]
    
    
        
    
       
        
        




 



##Player Statuses!!##
        # Status 1 = Ready to Begin
        # Status 2 = In location, Ready for Action
        # Status 3 = Chosen to Explore
        # Status 4 = Found Treasure
        # Status 5 = Fight begun
    
## TO DO ##
        # Iventory screen / location where you can use your items. OR in battle.
        #randomize hit/miss on monster attack, defend, player attack
        #different monsters for Mountain (BOSS)
        #different treasure for different areas
        #weapons + stats = weapon_stats
        ##Currently stats of weapon  = 0 so when adding to my_stats = my_stats only. FIX
