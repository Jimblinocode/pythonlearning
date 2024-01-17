from random import randint



row = 26
column = 59

rowpos = randint(0, row)

columnpos = randint(0, column)


position = (columnpos,rowpos)

running = True



def mapprint():
    for item in range(row):
        for item in range(column):
            print("|", end="")
        print("")
    return

def loc():
    for item1 in range(row):
        for item2 in range(column):
            if position[0] == item2 and position[1] == item1:
                print("a", end="")
            print("|", end="")
        print("")
    return



while running:
    com = input()
    if com == "m":
        mapprint()     
    elif com == "spawn point":
        loc()
    




