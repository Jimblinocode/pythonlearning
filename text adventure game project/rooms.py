from items import item
from enemies import enemy

class room:
    def __init__(self, id: int, doors: dict, items: list[item], monster: list[enemy]):
        self.id = id
        self.desc: list = open("text adventure game project/Roomdesc.txt").readlines()
        self.directions= doors
        self.itemslist = items
        self.monster = monster
    
        

