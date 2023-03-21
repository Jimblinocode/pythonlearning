class room:
    def __init__(self, id: int, doors: dict, items: list, monster: list):
        self.id = id
        self.desc: list = open("text adventure game project/Roomdesc.txt").readlines()
        self.directions= doors
        self.items = items
        self.monster = monster
    
        

