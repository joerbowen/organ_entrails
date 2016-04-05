class Player():
    """Class to keep track of player related stuff"""
    def __init__(self):
        self.inventory = {"Toilet Paper": 5,
                          "Duct Tape": 1,
                          "Paracord": 1,
                          "Pack of Gum": 1,
                          "Garden Hose": 0,
                          "Half Empty Can of Axe Body Spray": 0,
                          "Petunia": 0,
                          "Candy Bar" : 0
                          }
    

        self.life = 20
        self.weapons = ["Crowbar"]
        self.zombies_killed = 0

    def update_life(self,hit):
        self.life -=hit

    def update_inventory(self, item):
        self.inventory[item] +=1

    def update_weapon(self, weapon):
        self.weapons.insert(0, weapon)

    def use_inventory(self, item):
        self.inventory[item] -=1
        if item == "Candy Bar":
            self.life += 5

    def printInventory(self):
        print ("Inventory:\n==========")
        for item in self.inventory:
            if self.inventory[item] > 0:
                print (item + ": " + str(self.inventory[item]))
        print ("\n")
        
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
    
    
        

        
