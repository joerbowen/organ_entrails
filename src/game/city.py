import random

class City():
    """Class to keep track of City"""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.zombies = random.randrange(10,50)
        self.house = random.randrange(10,30)
        self.active = False

    def update_zombies(self,killed):
        self.zombies -= killed

    def update_house(self):
        self.house -= 1

    
        

        
        
