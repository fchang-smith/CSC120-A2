import computer as cp
class ResaleShop:
    inventory: list = []
    def __init__(self, inventory: list = []) -> None:
        self.inventory = inventory
    
    def buy(self, newComputer: object):
        listLen = len(self.inventory)
        item_ID = listLen + 1
        newComputer.item_ID = item_ID
        self.inventory.append(newComputer)
        return newComputer.item_ID
    
        

    
    def update_price(self, item_ID: int, newPrice: int):
        idx = item_ID - 1
        self.inventory[idx].updatePrice(newPrice)

    def sell(self, item_ID:str):
        idx = item_ID - 1
        listLen = len(self.inventory)
        if idx >= 0 and idx < listLen:
            del self.inventory[idx]
        else:
            print ("No such computer found")

    def print_inventory(self):
        listLen = len(self.inventory)
        if listLen != 0:
            print("Inventory:")
            for i in range(0, listLen):
                computer = self.inventory[i]
                print(computer)
        else:
            print("The inventory is empty")

    def refurbish(self, item_ID: int, new_os: str = None):
        idx = item_ID - 1
        if idx >= 0 and idx < len(self.inventory):
            computer = self.inventory[idx]
            if computer.year_made < 2000:
                computer.price = 0 
            elif computer.year_made < 2012:
                computer.price = 250 
            elif computer.year_made < 2018:
                computer.price = 550 
            else:
                computer.price = 1000 
        else:
            print("Item", item_ID, "not found. Please select another item to refurbish.")

        if new_os is not None:
            computer.operating_system = new_os
        
    




        

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
        
         # You'll remove this when you fill out your constructor

    # What methods will you need?