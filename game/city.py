import random

class City():
    """Class to keep track of City"""

    def __init__(self, name, description):
        """create a city with a name and a random number of zombies and houses"""
        self.name = name
        self.description = description
        self.zombies = random.randrange(10,25)
        self.house = random.randrange(10,20)

    def update_zombies(self,killed):
        """subtract killed zombies from total"""
        self.zombies -= killed

    def update_house(self):
        """subtract looted house from house total"""
        self.house -= 1

    
        

        
        
