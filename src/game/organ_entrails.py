#!/usr/bin python

from player import Player
import game_functions as gf
import random
from city import City

__author__ = 'andrewjohnson'


#Zombie game similar to Oregon Trail
#CC 2015 Non-Commercial use Attribution license

welcome = "Welcome to Organ Entrails!\nYou must make it from city to city, killing zombies along the way.\nCareful, they bite!"
cities = []
youAreHere = 0
        

def leaveCity():
    """Change to a different city"""
    global cities
    global youAreHere
    print("Where would you like to go? You are currently in " + cities[youAreHere].name)
    whereTo = ""
    i = 1
    for city in cities:
        if city != cities[youAreHere]:
            whereTo = whereTo + "   " + str(i) + ") " + city.name + "\n"
            i = i + 1
    cityIndex =  int(input("I want to go to: " + "\n" + whereTo))
    if youAreHere >= cityIndex: # for loop creates incorrect index. for all cities less than current city
        youAreHere = cityIndex -1
    else:
        youAreHere = cityIndex
    print("Welcome to " + cities[youAreHere].name)
    print (cities[youAreHere].description)

player = Player()

Zombietown = City("Zombietown", "Ground zero of the outbreak")
cities.append(Zombietown)
Wastelands = City("The Wastelands" , "There is not much here but zombies")
cities.append(Wastelands)
Detroit = City("Detroit", "Detroit has always been rough, but now it is deadly")
cities.append(Detroit)
Brainsville= City ("Brainsville" , "These zombies have devoloped a taste for brains")
cities.append(Brainsville)
Zombietown.active = True

# Game Starts here:
print (welcome)
print ("You start in " + Zombietown.name + " " + Zombietown.description + " good luck!")
print ("\nLook, a small horde of zombies approaches! Take this crowbar and go bash some heads!")

ready = input("Ready to fight? (Y/N)\n")

if (str.upper(ready) != "Y"):
    print ("Too bad, this is Zombietown. You better get ready.\n")
else:
    print ("Lock and load!\n")

gf.fightZombies(player, cities[youAreHere],3)
gf.lootBodies(player)

print("Now let's go loot a house")
gf.lootHouse(player, cities[youAreHere])

print("You seem to be getting this on your own. Here's a candy bar to restore your health, and one for the road. \n")
player.update_inventory("Candy Bar")
player.life = 20

while (player.life > 0):
    print("Life: " + str(player.life))
    print ("Zombies left in " + cities[youAreHere].name + ": " + str(cities[youAreHere].zombies))
    print ("House left to loot in " + cities[youAreHere].name + ": " + str(cities[youAreHere].house))
    action = input("What would you like to do now?\n1)Find more zombies\n2)Loot more houses\n3)Leave the city\n4)Check inventory\n5)Change Weapon\n6)Exit Game\n\n")
    if (action == "1"):  #case statement does the same thing.  Which is better for this?
        if cities[youAreHere].zombies > 0 :
            zombies = random.randrange(0,10)
            gf.fightZombies(player, cities[youAreHere], zombies)
            if (player.life > 0) and zombies !=0:
                gf.lootBodies(player)
            elif (player.life <= 0):
                break
        else:
            print ("There are no more zombies in this city.  Try somewhere else")
    elif (action == "2"):
        if cities[youAreHere].house > 0 :
            gf.lootHouse(player,cities[youAreHere])
        else:
            print ("There are no more houses to loot.  Try somewhere else")
    elif (action == "3"):
        leaveCity()
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
