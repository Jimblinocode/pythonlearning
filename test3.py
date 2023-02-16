
from random import randint
from os import system

bool = False




boollist = [[bool for row in range(6)] for column in range(6)]
symbol = [["#" for row in range(6)] for column in range(6)]

def gridclear():
    while True:
        penis, penis2 = (randint(0,5), randint(0,5))
        try:
            system("cls")
            boollist[penis][penis2] = True
            for row in boollist:
                for column in row:
                    if column == True:
                        coordinates = True
            if coordinates == True:
                print(f"{penis},{penis2} TRUE")
                symbol[penis][penis2] = " "
                for row in symbol:
                    for column in row:
                        print(column, end="")
                    print("")
            end = True
            for row in boollist:
                for column in row:
                    if column == False:
                        end = False
            if end == True:
                print("CLEAR")
                break
        except:
            print("done")


def randomgridconfig():
    
    i = 0
    condition = randint(0,36)
    while i < condition:
        system("cls")
        num, num2 = (randint(0,5), randint(0,5))
        boollist[num][num2] = False
        for row in boollist:
            for item in row:
                if item == False:
                    coordinates = True
        if coordinates == True:
            print(f"GENERATED {condition} TIMES")
            if symbol[num][num2] == "#":
                continue
            else:
                symbol[num][num2] = "#"
            for row in symbol:
                for item in row:
                    print(item, end="")
                print("")
            i += 1


gridclear()
while True:
    com = input()
    try:
        if com == "Random":
            randomgridconfig()
        elif com == "Clear":
            gridclear()
    except:
        print("NO")