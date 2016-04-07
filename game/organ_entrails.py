#!/usr/bin python

from player import Player
from inventory import Inventory
import game_functions as gf
import random
from city import City

__author__ = 'andrewjohnson'


#Zombie game similar to Oregon Trail
#CC 2015 Non-Commercial use Attribution license

welcome = "Welcome to Organ Entrails!\nYou must make it from city to city, killing zombies along the way.\nCareful, they bite!"

# create an list of inventory objects       
inventory =[]
toiletPaper = Inventory ("Toilet Paper", "The soft conttonelle does wonders for your chapped skin It's the little things to be thankful for.", 5)
inventory.append(toiletPaper)
ductTape= Inventory("Duct Tape", "Pretty much good for everything-- wrap a steak in it and it will keep idefinitely.",1)
inventory.append(ductTape)
paracord = Inventory ("Paracord" , "Your braided bracelet makes you look cool and if you get lost you'll have like 7 feet of rope.", 1)
inventory.append(paracord)
gum= Inventory("Pack of Gum", "The flavor only last for a moment.  Alas, this is cheap gum, and the good stuff is hard to come by.", 1)
inventory.append(gum)
hose = Inventory("Garden Hose", "Hooking up the hose to the spigot provides adqequate water for your beautiful petunias." ,0)
inventory.append(hose)
axeSpray = Inventory("Half Empty Can of Axe Body Spray", "The awkward smell of middle school envelopes your body, reminding you of the futility of life.", 0)
inventory.append(axeSpray)
petunia = Inventory("Petunia" , "It neve hurts to make an Apocalypse beautiful." ,0)
inventory.append(petunia)
candybar = Inventory("Candy Bar", "Slightly sweet, slightly sour with rich tones of military surplus rations.  Still, it ain't bad.", 0)
inventory.append(candybar)

player = Player(inventory)

#create an list of city objects
cities = []
Zombietown = City("Zombietown", "Ground zero of the outbreak")
cities.append(Zombietown)
Wastelands = City("The Wastelands" , "There is not much here but zombies")
cities.append(Wastelands)
Detroit = City("Detroit", "Detroit has always been rough, but now it is deadly")
cities.append(Detroit)
Brainsville= City ("Brainsville" , "These zombies have devoloped a taste for brains")
cities.append(Brainsville)

# Game Starts here:
print (welcome)
print ("You start in " + Zombietown.name + " " + Zombietown.description + " good luck!")
print ("\nLook, a small horde of zombies approaches! Take this crowbar and go bash some heads!")

ready = input("Ready to fight? (Y/N)\n")

if (str.upper(ready) != "Y"):
    print ("Too bad, this is Zombietown. You better get ready.\n")
else:
    print ("Lock and load!\n")

gf.fightZombies(player, cities[player.city_index],3)


print("Now let's go loot a house")
gf.lootHouse(player, cities[player.city_index])

print("You seem to be getting this on your own. Here's a candy bar to restore your health, and one for the road. \n")
item = player.getInventoryIndex("Candy Bar")
player.update_inventory(item)
player.life = 20

while (player.life > 0):
    print("\nLife: " + str(player.life))
    print ("Zombies left in " + cities[player.city_index].name + ": " + str(cities[player.city_index].zombies))
    print ("House left to loot in " + cities[player.city_index].name + ": " + str(cities[player.city_index].house))
    action = input("What would you like to do now?\n1)Find more zombies\n2)Loot more houses\n3)Leave the city\n4)Check inventory\n5)Change Weapon\n6)Exit Game\n\n")
    if (action == "1"):  #case statement does the same thing.  Which is better for this?
        if cities[player.city_index].zombies > 0 :
            zombies = random.randrange(1,10)
            if zombies < cities[player.city_index].zombies :
                gf.fightZombies(player, cities[player.city_index], zombies)
            else:
                print ("These are the last zombies roaming the city")
                print ("There may be more hiding in houses")
                gf.fightZombies(player, cities[player.city_index], cities[player.city_index].zombies)
        else:
            print ("There are no more zombies in this city.  Try somewhere else")
    elif (action == "2"):
        if cities[player.city_index].house > 0 :
            gf.lootHouse(player,cities[player.city_index])
        else:
            print ("There are no more houses to loot.  Try somewhere else")
    elif (action == "3"):
        player.leaveCity(cities)
    elif (action == "4"):
        gf.checkInventory(player)
    elif (action == "5"):
        player.changeWeapon()
    elif (action =="6"):
        print ("At the first sign of weekness all zombies gang up on you!")
        break
    else:
        print("Invalid input!")

print("You killed a total of " + str(player.zombies_killed) + " zombies.  Then you died.")
