import rooms
import items

class Game:
    def __init__(self):
        self.gamerun = True  
        self.map = [
            rooms.room(1,{
            "EAST": 2,
            "SOUTH": 1,
            "WEST": 0
            },
            [],
            [] ),
            rooms.room(2,{
            "EAST": 3,
            "SOUTH": 4,
            "WEST": 2
            },
            [],
            [] ),
            rooms.room(3, {
            "WEST": 3
            },
            [],
            [] ),
            rooms.room(4, {
            "NORTH": 1
            },
            [],
            [] ),
            rooms.room(5, {
            "EAST": 5,
            "NORTH": 4,
            "SOUTH": 6
            },
            [],
            [] ),
            rooms.room(6, {
            "WEST": 5,
            "SOUTH": 8
            },
            [],
            [] ),
            rooms.room(7, {
            "EAST": 7
            },
            [],
            [] ),
            rooms.room(8, {
            "WEST": 7,
            "NORTH": 6
            },
            [],
            [] ),
            rooms.room(9, {
            "NORTH": 8
            },
            [],
            [] )
        ]
    
    def move(self, inp, num: int):
        loc = self.map[num]
        try:
            if inp == "EAST":
                match loc.directions["EAST"]:
                    case 2:
                        print(loc.desc[1])
                    case 3:
                        print(loc.desc[2])
                    case 5:
                        print(loc.desc[5])
                    case 7:
                        print(loc.desc[7])
            elif inp == "WEST":
                match loc.directions["WEST"]:
                    case 0:
                        self.gamerun = False
                        print("PLACEHOLDER")
                    case 2:
                        print(loc.desc[0])
                    case 3:
                        print(loc.desc[1])
                    case 5:
                        print(loc.desc[4])
                    case 7:
                        print(loc.desc[6])
            elif inp == "SOUTH":
                match loc.directions["SOUTH"]:
                    case 1:
                        print(loc.desc[3])
                    case 4:
                        print(loc.desc[4])
                    case 6:
                        print(loc.desc[7])
                    case 8:
                        print(loc.desc[8])

                        
        except:
            if inp == "WEST":
                print(loc.desc[2])
            if inp == "NORTH" and loc == self.map[0]:
                print(open("text adventure game project/bonustext").readlines[1]) # bonus text that appears when you try to go north on room 1.
                print("you run into a wall.")
            
        
    
    def process_command(self):
        pass

    def run(self):
        print("what is your name?")
        name = input()
        print(f"Hello {name}")
        print(open("text adventure game project/start.txt").read(), end="\n\n")
        print(self.map[0].desc[0])
        l = 0
        while self.gamerun:
            rcom = input()
            com = rcom.split(" ")
            if com[0] == "MOVE":
                self.move(com[1], l)
                if com[1] == "EAST":               
                    l += 1
                elif com[1] == "WEST":
                    l -= 1
                    if l == 0:
                        continue
                elif com[1] == "SOUTH":
                    l += 3
                elif com[1] == "NORTH":
                    l -= 3
                    if l == 0: # might get rid of later
                        continue 
                
                
                

            
Game().run()



