import random

weapon = {"Crowbar": 1, "Pistol": 2, "Shovel": 3, "Crossbow": 4, "Shotgun": 5, "Bazooka": 7}

def calculateDamage (power,zombies, attack, house=False):
    """Calculate damage using hitMultiplier and number of Zombies.  Different damage depending on attacking or fleeing or if in a house"""
    hitMultiplier = [0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4]
    if attack :
        if house:#Zombies are not as effective in a house
            damage = hitMultiplier[random.randrange(len(hitMultiplier)-3)]*zombies - hitMultiplier[random.randrange(0,len(hitMultiplier))] * power
        else:
            damage = hitMultiplier[random.randrange(len(hitMultiplier))]*zombies - hitMultiplier[random.randrange(0,len(hitMultiplier))]* power
    else :
        damage = hitMultiplier[random.randrange(len(hitMultiplier)-3)]*zombies - power  #zombies are not as strong, but neither is the weapon power multiplied.

    if damage > 0 :
        return damage
    else:
        return 0

def getItem(item_dict):
    """get a random item from a dict"""
    list_items=sorted(item_dict.keys())  #create a list of sorted keys
    return list_items[random.randrange(len(list_items))]
    

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
            player.zombies_killed += zombies
            city.update_zombies(zombies)
            if hit >0 :
                player.update_life(hit)
                print (str(zombies) + " attack you.  They did " + str(hit) + " damage \nLife health is now " + str(player.life))
            else:
                print("You took no damage!  Your life is still " + str(player.life))
            if player.life > 0 :
                lootBodies(player)
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
        foundItem = random.randrange(len(player.inventory))
        foundWeapon=getItem(weapon)
        zombies = random.randrange(4)
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
            takeItem = input("You found a " + player.inventory[foundItem].name + "\nEquip? (Y/N)")
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
        if (random.randrange(9)==8):  
            print("A zombie was not yet dead!\n")
            hit = calculateDamage(3,1,True)# for this fight a destructive power of 3 is assumed no matter what weapon is used.
            player.update_life(hit)
            print("Zombie did " + str(hit) + " damage to you.\nYour life is " + str(player.life))
        else:
            foundItem = random.randrange(len(player.inventory))
            print("You found a " + player.inventory[foundItem].name)
            equip = input("Equip? (Y/N)")
            if (str.upper(equip) == "Y"):
                player.update_inventory(foundItem)
                player.printInventory()

def checkInventory(player):
    """List current inventory and allow user to use an item"""
    print ("Current weapon: " + str(player.weapons[0]))
    print ("Destruction power: " + str(weapon[player.weapons[0]]))
    print("Inventory:\n==========")
    i = 1
    inventoryList =[]
    for item in player.inventory:
        if(item.qty > 0):
            print (str(i) + ") " + item.name + ": " + str(item.qty))
            i = i + 1
            inventoryList.append(item.name)  #Array of all inventory items with qty greater than 0
    print (str(i) + ") Exit Inventory")
    inventoryIndex = int(input("Select the item from the list.\n"))-1
    if inventoryIndex != len(inventoryList):  #if index = len then exit was selected
        player.use_inventory(inventoryList[inventoryIndex])





                   
            
