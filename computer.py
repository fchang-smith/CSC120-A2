class Computer:
    item_ID: int = 0
    description:str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    def __init__(self, 
                 item_ID: int = 0,
                 description:str = "", 
                 processor_type: str = "", 
                 hard_drive_capacity: int = 0, 
                 memory: int = 0, 
                 operating_system: str = "", 
                 year_made: int = 0, 
                 price: int = 0) -> None:
       self.item_ID = item_ID
       self.description = description
       self.processor_type = processor_type
       self.hard_drive_capacity = hard_drive_capacity
       self.memory = memory
       self.operating_system = operating_system
       self.year_made = year_made
       self.price = price

    def updatePrice(self, newPrice: int):
        self.price = newPrice

    def updateOS(self, newOS):
        self.operating_system = newOS

    def createComputer(self, computer: dict):
        self.description = computer["description"]
        self.processor_type = computer["processor_type"]
        self.hard_drive_capacity = computer["hard_drive_capacity"]
        self.memory = computer["memory"]
        self.operating_system = computer["operating_system"]
        self.year_made = computer["year_made"]
        self.price = computer["price"]

    def __str__(self):
        return f'Item_ID: {self.item_ID} \n    Description: {self.description} ({self.year_made}, {self.price})'

        


    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    #def __init__():
    #    pass # You'll remove this when you fill out your constructor

    # What methods will you need?