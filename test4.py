from random import randint
bool = False
bool2 = False
bool3 = False

itemlist = [bool, bool2, bool3]

while True:
    com = input()
    if com == "|":
        itemlist[randint(0,2)] = True
        for item in itemlist:
            if item == True:
                print("8========D")