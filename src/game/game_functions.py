import random

weapon = {"Crowbar": 1, "Pistol": 2, "Shovel": 3, "Crossbow": 4, "Shotgun": 5, "Bazooka": 7}

def calculateDamage (power,zombies, attack, house=False):
    """Calculate damage using hitMultiplier and number of Zombies.  Different damage depending on attacking or fleeing or if in a house"""
    hitMultiplier = [0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4]
    if attack :
        if house:#Zombies are not as effective in a house
            damage = hitMultiplier[random.randrange(0,len(hitMultiplier)-3)]*zombies - hitMultiplier[random.randrange(0,len(hitMultiplier))] * power
        else:
            damage = hitMultiplier[random.randrange(0,len(hitMultiplier))]*zombies - hitMultiplier[random.randrange(0,len(hitMultiplier))]* power
    else :
        damage = hitMultiplier[random.randrange(0,len(hitMultiplier)-3)]*zombies - power  #zombies are not as strong, but neither is the weapon power multiplied.

    if damage > 0 :
        return damage
    else:
        return 0

def getItem(item_dict):
    list_items=[]  #create a list of keys
    for item in item_dict:
        list_items.append(item)
    return list_items[random.randrange (0, len(list_items))]
    

def fightZombies(player,city, zombies):
    """Calculates the amount of damage a zombie does.  If you run your weapon is not as effective"""
    current_weapon = player.weapons[0]
    destructive_power = weapon[current_weapon]
    if zombies != 0:
        print(str(zombies) + " zombies stagger towards you. Ready your " + str.lower(current_weapon) + "!\n")
        attack = input("Attack, or Run? (A for attack, R for run)\n")
        if (str.upper(attack) != "A"):
            hit = calculateDamage(destructive_power,zombies,False)  
            if hit > 0:
                player.update_life(hit)
                print (str(zombies) + " attack you.  They did " + str(hit) + " damage \nLife health is now " + str(player.life))
            if (hit == 0):
                print("That was a lucky miss. Next time you should attack!")
        else:
            hit = calculateDamage(destructive_power,zombies,True)
            if hit >0 :
                player.update_life(hit)
                print (str(zombies) + " attack you.  They did " + str(hit) + " damage \nLife health is now " + str(player.life))
            else:
                print("You took no damage!  Your life is still " + str(player.life))
        player.zombies_killed += zombies
        city.update_zombies(zombies)
    elif zombies == 0:
         print ("But Nobody Came!")

def lootHouse(player,city):
    """Allows you to fight zombies and collect one random object and one random weapon.
    if user runs away they don't get any equiptment"""
    current_weapon = player.weapons[0]
    destructive_power = weapon[current_weapon]
    
    runAway = False
    loot = input("Loot house? (Y/N)\n")
    if(str.upper(loot) == "Y"):
        foundItem = getItem(player.inventory)
        foundWeapon=getItem(weapon)
        zombies = random.randrange(0, 4)
        print(str(zombies) + " zombies found in house.")
        if zombies != 0:
            attack = input("Attack or Run? (A/R)\n")
            if str.upper(attack) == "A":
                hit = calculateDamage(destructive_power,zombies,True,True) 
                player.update_life(hit)
                print (str(zombies) + " attack you. They did "+ str(hit) + " damage \nLife health is now " + str(player.life))
                player.zombies_killed += zombies
            else:
                runAway = True
                print("You run away quietly, with no cool stuff.")
        else:
            print ("The house is empty of zombies, but full of cool stuff...")
        if (runAway != True):
            city.update_house()
            takeItem = input("You found a " + foundItem + "\nEquip? (Y/N)")
            takeWeapon = input("Cool! You found a " + foundWeapon + "\nEquip? (Y/N)")
            if str.upper(takeWeapon) == "Y": player.update_weapon(foundWeapon)
            if str.upper(takeItem) == "Y": player.update_inventory(foundItem)
            print ("Current weapon: " + player.weapons[0])
            print ("Destruction power: " + str(weapon[player.weapons[0]]))
            player.printInventory()

def lootBodies(player):
    """Allows user to get random inventory item.  No weapons like in loot house"""
    loot = input("Would you like to loot the bodies? (Y/N)\n")
    if (str.upper(loot) == "Y"):
        if (random.randrange(0,9)>8):
            print("A zombie was not yet dead!\n")
            hit = calculateDamage(3,1,True)# for this fight a destructive power of 3 is assumed no matter what weapon is used.
            player.update_life(hit)
            print("Zombie did " + str(hit) + " damage to you.\nYour life is " + str(player.life))
        else:
            foundItem = getItem(player.inventory)
            print("You found a " + foundItem)
            equip = input("Equip? (Y/N)")
            if (str.upper(equip) == "Y"):
                player.update_inventory(foundItem)
                player.printInventory()

def checkInventory(player):
    """List current inventory and allow user to use an item"""
    flavorText = {"Toilet Paper": "The soft cottonelle does wonders for your chapped skin. It's the little things to be thankful for.",
              "Duct Tape": "Pretty much good for everything-- wrap a steak in it and it will keep indefinitely.",
              "Paracord": "Your braided bracelet makes you look cool and if you get lost you'll have like 7 feet of rope.",
              "Pack of Gum": "The flavor only lasts for a moment. Alas, this is cheap gum, and the good stuff is hard to come by.",
              "Garden Hose": "Hooking up the hose to the spigot provides adequate water for your beautiful petunias.",
              "Half Empty Can of Axe Body Spray": "The awkward smell of middle school envelopes your body, reminding you of the futility of life.",
              "Petunia": "It never hurts to make an Apocalypse beautiful.",
              "Candy Bar" : "Slightly sweet, slightly sour with rich tones of military surplus rations. Still, it ain't bad."
            }
    
    print ("Current weapon: " + str(player.weapons[0]))
    print ("Destruction power: " + str(weapon[player.weapons[0]]))
    print("Inventory:\n==========")
    i = 1
    invArray = []
    for item in player.inventory:
        if(player.inventory[item] > 0):
            print (str(i) + ") " + item + ": " + str(player.inventory[item]))
            invArray.append(item)  #create a list of keys  index = i-1
            i = i + 1
    print (str(i) + ") Exit Inventory")
    inventoryIndex = int(input("Select the item from the list.\n"))-1
    if inventoryIndex != len(invArray):  #if index = len then exit was selected
        myItem = invArray[inventoryIndex]
        print (flavorText[myItem])
        player.use_inventory(myItem)

        


                   
            
