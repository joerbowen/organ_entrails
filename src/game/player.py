class Player():
    """Class to keep track of player related stuff"""
    def __init__(self, inventory):
        """Create a play with an inventory array, life and weapons"""
        self.inventory = inventory
        self.life = 20
        self.weapons = ["Crowbar"]
        self.zombies_killed = 0
        self.city_index = 0

    def update_life(self,hit):
        """subtract hit points from life"""
        self.life -=hit

    def update_inventory(self, index):
        """Decrease quantity of item in inventory"""
        self.inventory[index].qty +=1

    def update_weapon(self, weapon):
        """Insert a new weapon in the weapon array"""
        if weapon not in self.weapons:
            self.weapons.insert(0, weapon)
        elif weapon == self.weapons[0]:
            print( weapon + " is currently equipted")
        else:
            print("You already have a " + weapon)
            print ("Your current weapon is " + self.weapons[0])
            use = input ("Would you like to switch to "+ weapon + "? (Y/N)").upper()
            if use =="Y" :
                index = self.weapons.index(weapon)
                w=self.weapons.pop(index)
                self.weapons.insert(0,w)
                         

    def use_inventory(self, item):
        """Decrease the quanity of the item in inventory"""
        index=self.getInventoryIndex(item)
        self.inventory[index].qty -=1
        print (self.inventory[index].description)
        if self.inventory[index].name == "Candy Bar":
            self.life += 5

    def printInventory(self):
        """Print a formated list of all items with quanity > 0"""
        print ("Inventory:\n==========")
        for item in self.inventory:
            if item.qty > 0:
                print (item.name + ": " + str(item.qty))
        print ("\n")

    def getInventoryIndex(self, name):
        """For a given inventory name return the array index.
           used to insert item by name"""
        for i in range(0, len(self.inventory)):
            if self.inventory[i].name == name:
                return i

    
    def changeWeapon(self):
        """Allow user to equip a different weapon from inventory"""
        print("Current weapon equipped: " + self.weapons[0])
        print ("Select weapon to equip from the list.")
        i = 1
        for weapon in self.weapons:
            print (str(i) + ") " + weapon)
            i += 1
        equip = int(input("Equip:\n"))-1
        w = self.weapons.pop(equip)
        self.update_weapon(w)

        print (self.weapons[0] + " is equipped.\n")

    
    def leaveCity(self,cities):
        """Change to a different city"""
    
        print("Where would you like to go? You are currently in " + cities[self.city_index].name)
        whereTo = ""
        i = 1
        for city in cities:
            if city != cities[self.city_index]:
                whereTo = whereTo + "   " + str(i) + ") " + city.name + "\n"
                i = i + 1
        cityIndex =  int(input("I want to go to: " + "\n" + whereTo))
        if self.city_index >= cityIndex: # for loop creates incorrect index. for all cities less than current city
            self.city_index = cityIndex -1
        else:
            self.city_index = cityIndex
        print("Welcome to " + cities[self.city_index].name)
        print (cities[self.city_index].description)

        
