import rooms
import items
import enemies

class Game:
    def __init__(self):
        self.gamerun = True  
        self.map = [
            rooms.room(0,{ #room 1
            "EAST": 2,
            "SOUTH": 1,
            "WEST": 0
            },
            [items.item("GLOCK 18"), items.item("ORB")], # items
            [] ), # enemies
            rooms.room(1,{ #room 2
            "EAST": 3,
            "SOUTH": 4,
            "WEST": 2
            },
            [],
            [enemies.enemy("GIGAREDDITOR")] ),
            rooms.room(2, { #room 3
            "WEST": 3
            },
            [items.item("THE SHIRT OF ETERNAL VIRGINITY")],
            [] ),
            rooms.room(3, { #room 4
            "NORTH": 1
            },
            [items.item("THE MAJESTIC LEAN OF THE GODS")],
            [] ),
            rooms.room(4, { #room 5
            "EAST": 5,
            "NORTH": 4,
            "SOUTH": 6
            },
            [],
            [enemies.enemy("FIRE WIZARD")] ),
            rooms.room(5, { #room 6
            "WEST": 5,
            "SOUTH": 8
            },
            [],
            [enemies.enemy("TREE WIZARD")] ),
            rooms.room(6, { #room 7
            "EAST": 7
            },
            [items.item("THE MAGNUM DONG DILDO SWORD")],
            [] ),
            rooms.room(7, { #room 8
            "WEST": 7,
            "NORTH": 6
            },
            [items.item("THE VAPOREON COPYPASTA")],
            [] ),
            rooms.room(8, { #room 9
            "NORTH": 8
            },
            [items.item("THE MYTHICAL ZA")],
            [] )
        ]
        self.bag: list[items.item] = []
        self.l = 0
        self.loc = self.map[self.l]
        self.bag_empty = True
        self.room_empty = True
        
    def move(self, inp):
        try:
            #prints the description of the room your moving to based on the door numbers of the room your currently in
            if inp == "EAST":
                match self.loc.directions["EAST"]:
                    case 2:
                        if self.map[1].monster[0].dead == False:
                            print(self.loc.desc[1])
                            print("the greasy, pimple-ridden GIGAREDDITOR is across the room from you.")
                        else:
                            print(self.loc.desc[1])
                    case 3:
                        if self.map[1].monster[0].dead == False:
                            print("you must defeat the GIGAREDDITOR before proceeding\n")
                            print(self.loc.desc[1])
                        else:    
                            print(self.loc.desc[2])
                    case 5:
                        if self.map[5].monster[0].dead == False:
                            print(self.loc.desc[5])
                            print("ahead of you stands the TREE WIZARD. with the fragrant smell of weed and the insurmountable swag radiating off of him, hes hard not to notice. \n(Type TWIZARD after the ATTACK command to attack)")
                        else:
                            print(self.loc.desc[5])
                    case 7:
                        print(self.loc.desc[7])
            elif inp == "WEST":
                match self.loc.directions["WEST"]:
                    case 0:
                        print(open("text adventure game project/endlose.txt").read())
                        self.gamerun = False
                    case 2:
                        print(self.loc.desc[0])
                    case 3:
                        print(self.loc.desc[1])
                    case 5:
                        print(self.loc.desc[4])
                    case 7:
                        print(self.loc.desc[6])
            elif inp == "SOUTH":
                match self.loc.directions["SOUTH"]:
                    case 1:
                        print(self.loc.desc[3])
                    case 4:
                        if self.map[4].monster[0].dead == False:
                            print(self.loc.desc[4])
                            print("the FIRE WIZARD sits at the center of the room, preparing to cast his SPELLS at you (sponsored by the shadow government). \n(Type FWIZARD after the ATTACK command to attack)")
                        else:
                            print(self.loc.desc[4])
                    case 6:
                        if self.map[4].monster[0].dead == False:
                            print("you must defeat the FIRE WIZARD before proceeding")
                            print(self.loc.desc[4])
                        else:
                            print(self.loc.desc[7])
                    case 8:
                        if self.map[5].monster[0].dead == False:
                            print("you must defeat the TREE WIZARD before proceeding")
                            print(self.loc.desc[5])
                        else:
                            print(self.loc.desc[8])
            elif inp == "NORTH": 
                match self.loc.directions["NORTH"]:
                    case 1:
                        print(self.loc.desc[0])
                    case 4:
                        print(self.loc.desc[1])
                    case 6:
                        print(self.loc.desc[4])
                    case 8:
                        print(self.loc.desc[5])
            
            # actual location change process
            if inp == "EAST": 
                if self.loc == self.map[1] and self.map[1].monster[0].dead == False:
                    self.l = 1
                else:            
                    self.l += 1  
                
                if self.l == 3:
                    self.l -= 1

            elif inp == "WEST":
                self.l -= 1
                if self.l < 0:
                    self.l += 1
            elif inp == "SOUTH":
                if self.loc == self.map[4] and self.map[4].monster[0].dead == False:
                    self.l = 4
                elif self.loc == self.map[5] and self.map[5].monster[0].dead == False:
                    self.l = 5
                else:
                    self.l += 3
            elif inp == "NORTH":
                self.l -= 3
                if self.l < 0: # might get rid of later
                    self.l += 1 
                elif self.l == 6 and self.loc == self.map[0]:
                    self.l -= 6
                elif self.l == 3 and self.loc == self.map[0]:
                    self.l -= 3 
            self.loc = self.map[self.l]
            

                        
        except:
            match inp:
                case "SOUTH":
                    print("You ran into a wall.")
                    print(self.loc.desc[self.l])
                case "NORTH":
                    if self.l == 6:
                        self.loc = self.map[0]
                        print(self.loc.desc[0])
                    else:
                        print("You ran into a wall.")
                        print(self.loc.desc[self.l])
                case "EAST":
                    if self.l == 3:
                        self.loc = self.map[2]
                        print(self.loc.desc[2])
                    else:
                        print("You ran into a wall.")
                        print(self.loc.desc[self.l])
                case "WEST":
                    if self.l == 5:
                        self.loc = self.map[6]
                        print(self.loc.desc[6])
                    else:
                        print("You ran into a wall.")
                        print(self.loc.desc[self.l])

    def process_pick(self, object):
        self.exist = False
        self.shorthand = ["GLOCK18", "SHIRT", "LEAN", "SWORD", "COPYPASTA"]
        if self.loc == self.map[0]:
            match object:
                case "GLOCK18":
                    for item in self.loc.itemslist:
                        if item.name == "GLOCK 18":
                            self.exist = True
                    if self.exist == True:
                        if self.loc.itemslist[0].name == "GLOCK 18":
                            self.bag.append(self.loc.itemslist[0])
                            print(f"\n{self.loc.itemslist[0].name} has been added to your inventory\n")
                            self.bag_empty = False
                            self.loc.itemslist.remove(self.loc.itemslist[0])
                            self.bag_empty_check()
                            self.room_empty_check()
                        else:
                            self.bag.append(self.loc.itemslist[1])
                            self.bag_empty = False
                            self.loc.itemslist.remove(self.loc.itemslist[1])
                            print(f"\n{object} has been added to your inventory\n")
                            self.bag_empty_check()
                            self.room_empty_check()
                case "ORB":
                    for item in self.loc.itemslist:
                        if item.name == "ORB":
                            self.exist = True
                    if self.exist == True:
                        if self.loc.itemslist[0].name == "ORB":
                            self.bag.append(self.loc.itemslist[0])
                            self.loc.itemslist.remove(self.loc.itemslist[0])
                            print(f"\n{object} has been added to your inventory\n")
                            self.bag_empty_check()
                            self.room_empty_check()
                        else:
                            self.bag.append(self.loc.itemslist[1])
                            self.bag_empty = False
                            self.loc.itemslist.remove(self.loc.itemslist[1])
                            print(f"\n{object} has been added to your inventory\n")
                            self.bag_empty_check()
                            self.room_empty_check()
                case _:  
                    print(f"{object} does not exist and connot be picked up")
        elif self.loc == self.map[2]:
            match object:
                case "SHIRT":
                    for item in self.loc.itemslist:
                        if item.name == "THE SHIRT OF ETERNAL VIRGINITY":
                            self.exist = True
                    if self.exist == True:
                        self.bag.append(self.loc.itemslist[0])
                        self.bag_empty = False
                        print(f"\n{self.loc.itemslist[0].name} has been added to your inventory\n")
                        self.loc.itemslist.remove(self.loc.itemslist[0])
                        self.bag_empty_check()
                        self.room_empty_check()
                case _:  
                    print(f"{object} does not exist and connot be picked up")
        elif self.loc == self.map[3]:
            match object:
                case "LEAN":
                    for item in self.loc.itemslist:
                        if item.name == "THE MAJESTIC LEAN OF THE GODS":
                            self.exist = True
                    if self.exist == True:
                        self.bag.append(self.loc.itemslist[0])
                        self.bag_empty = False
                        print(f"\n{self.loc.itemslist[0].name} has been added to your inventory\n")
                        self.loc.itemslist.remove(self.loc.itemslist[0])
                        self.bag_empty_check()
                        self.room_empty_check()
                case _:  
                    print(f"{object} does not exist and connot be picked up")
        elif self.loc == self.map[6]:
            match object:
                case "SWORD":
                    for item in self.loc.itemslist:
                        if item.name == "THE MAGNUM DONG DILDO SWORD":
                            self.exist = True
                    if self.exist == True:
                        self.bag.append(self.loc.itemslist[0])
                        self.bag_empty = False
                        print(f"\n{self.loc.itemslist[0].name} has been added to your inventory\n")
                        self.loc.itemslist.remove(self.loc.itemslist[0])
                        self.bag_empty_check()                              
                        self.room_empty_check()
                case _:  
                    print(f"{object} does not exist and connot be picked up")
        elif self.loc == self.map[7]:
            match object:
                case "COPYPASTA":
                    for item in self.loc.itemslist:
                        if item.name == "THE VAPOREON COPYPASTA":
                            self.exist = True
                    if self.exist == True:
                        self.bag.append(self.loc.itemslist[0])
                        print(f"\n{self.loc.itemslist[0].name} has been added to your inventory\n")
                        self.bag_empty = False
                        self.loc.itemslist.remove(self.loc.itemslist[0])
                        self.bag_empty_check()
                        self.room_empty_check()
                case _:  
                    print(f"{object} does not exist and connot be picked up")
        elif self.loc == self.map[8]:
            match object:
                case "ZA":
                    for item in self.loc.itemslist:
                        if item.name == "THE MYTHICAL ZA":
                            self.exist = True
                    if self.exist == True:
                        self.bag.append(self.loc.itemslist[0])
                        self.bag_empty = False
                        self.loc.itemslist.remove(self.loc.itemslist[0])
                        print(open("text adventure game project/endwin.txt").read())
                        self.gamerun = False
        else:
            itemexist = False
            if len(self.loc.itemslist) >= 1:
                itemexist = True
            if itemexist == True:
                for item in self.shorthand:
                    if item  == object:
                        for item in self.loc.itemslist:
                            if len(item.name.split(" ")) > 1:
                                object = item
                                self.bag.append(object)
                                self.loc.itemslist.remove(object)
                                print(f"{object.name} has been added to your inventory")
                                self.bag_empty_check()

    def process_drop(self, object):
        for item in self.shorthand:
            if item == object:
                for item in self.bag:
                    if len(item.name.split(" ")) > 1:
                        object = item
                        self.loc.itemslist.append(object)
                        self.bag.remove(object)
                        print(f"{object.name} has been romoved from your inventory", "\nYour inventory:\n")
                        self.bag_empty_check()
                    else:
                        self.loc.itemslist.append(item.name)
                        self.bag.remove(item.name)
                        print(f"{item.name} has been removed from your inventory", "\nYour inventory:\n")
                        self.bag_empty_check()

    def bag_empty_check(self):
        if len(self.bag) == 0:
                self.bag_empty = True
        else:
                self.bag_empty = False
        
        print("\nYour inventory:")
        if self.bag_empty == True:
            print("inventory empty.\n")
        else:
            for item in self.bag:
                print(item.name, "\n----------------------------------------------------------------\n")

    def room_empty_check(self):
        if len(self.loc.itemslist) == 0:
            self.room_empty = True
        else:
            self.room_empty = False
        
        if self.room_empty == True:
            print("There are no items in this room")
        else:
            print("items in this room:")
            for item in self.loc.itemslist:
                print("|", item.name,"|", end="")
            print(" ")
            if self.loc == self.map[0]:
                print(open("text adventure game project/shorthandhelp.txt").readlines()[0])
            elif self.loc == self.map[2]:
                print(open("text adventure game project/shorthandhelp.txt").readlines()[1])
            elif self.loc == self.map[3]:
                print(open("text adventure game project/shorthandhelp.txt").readlines()[2])
            elif self.loc == self.map[6]:
                print(open("text adventure game project/shorthandhelp.txt").readlines()[3])
            elif self.loc == self.map[7]:
                print(open("text adventure game project/shorthandhelp.txt").readlines()[4])
            elif self.loc == self.map[8]:
                print(open("text adventure game project/shorthandhelp.txt").readlines()[5])

    def process_attack(self, inp):
        if inp == "GIGAREDDITOR" and self.loc == self.map[1]:
            for item in self.bag:
                if item.name == "ORB" and self.map[1].monster[0].dead == False:
                    print("\n",open("text adventure game project/attack.txt").readlines()[0],end="\n\n")
                    self.map[1].monster[0].dead = True
                    print("a path has been opened to the EAST.")
                else:
                    if len(self.bag) > 1:
                        continue
                    else:
                        print(f"you attempt to attack with item {item.name}, however the GIGAREDDITOR's 500D chess intellect sees your move coming from a mile away. he teleports behind you and impales you with his katana, you lay on the floor bleeding to death.")
                        print(open("text adventure game project/enddead.txt").read())
                        self.gamerun = False
        elif inp == "FWIZARD" and self.loc == self.map[4]:
                for item in self.bag:
                    if item.name == "THE SHIRT OF ETERNAL VIRGINITY" and self.map[4].monster[0].dead == False:
                        print("\n",open("text adventure game project/attack.txt").readlines()[1],end="\n\n")
                        self.map[4].monster[0].dead = True
                        print("a path has been opened to the SOUTH")
                    elif item.name == "GLOCK 18" and self.map[4].monster[0].dead == False:
                        print("\n",open("text adventure game project/attack.txt").readlines()[2],end="\n\n")
                        self.map[4].monster[0].dead = True
                        print("a path has been opened to the SOUTH")
                    else:
                        if self.bag[1].name == "THE SHIRT OF ETERNAL VIRGINITY" or self.bag[2].name == "THE SHIRT OF ETERNAL VIRGINITY" or self.bag[3].name == "THE SHIRT OF ETERNAL VIRGINITY":
                            continue
                        else:
                            print(f"you attempt to attack with item {item.name}, the items power is deflected by the wizards ward. the wizard, with his immense swag, then casts a powerful stream of fire (sponsored by the shadow government) burning you to a crisp.")
                            print(open("text adventure game project/enddead.txt").read())
                            self.gamerun = False
        elif inp == "TWIZARD" and self.loc == self.map[5]:
            for item in self.bag:
                if item.name == "THE MAGNUM DONG DILDO SWORD" and self.map[5].monster[0].dead == False:
                    print("\n",open("text adventure game project/attack.txt").readlines()[3],end="\n\n")
                    self.map[5].monster[0].dead = True
                    print("a path has been opened to the SOUTH")
                else:
                    if (self.bag[2].name == "THE MAGNUM DONG DILDO SWORD" or self.bag[3].name == "THE MAGNUM DONG DILDO SWORD") or (self.bag[4].name == "THE MAGNUM DONG DILDO SWORD" or self.bag[5].name == "THE MAGNUM DONG DILDO SWORD"):
                        continue
                    else:
                        print(f"you attempt to attack with item {item.name}, the items power is deflected by the wizards ward. the wizard then uses his spells (sponsored by the shadow governement) to wrap all four of your limbs in giant weed vines and then pull you appart, killing you instantly")
                        print(open("text adventure game project/enddead.txt").read())
                        self.gamerun = False

    

    def run(self):
        print("what is your name?")
        name = input()
        print(f"\nHello, {name}!\n")
        print(open("text adventure game project/start.txt").read(), end="\n\n")
        self.bag_empty_check()
        print(self.map[0].desc[0])
        while self.gamerun:
            rcom = input()
            com = rcom.split(" ")
            if com[0] == "MOVE":
                if self.l >= 10:
                    self.l -= 3
                self.move(com[1])
            elif com[0] == "PICK":
                self.process_pick(com[1])
            elif com[0] == "DROP":
                self.process_drop(com[1])
            elif com[0] == "ATTACK":
                self.process_attack(com[1])
            elif com[0] == "LOOK":
                self.room_empty_check() 
            elif com[0] == "EXIT":
                self.gamerun = False      
Game().run()





