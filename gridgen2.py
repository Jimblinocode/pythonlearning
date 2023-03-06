import random
import os

thing = True

bools = [[thing for item in range(6)] for item in range(6)]
gen = [["B" for item in range(6)] for item in range(6)]


def gridprint(G:list):
    for row in G:
        for item in row:
            print(item, end="")
        print("")

def boolchange():
    try:
        i = 0
        while i < 36:
            rnum1, rnum2 = (random.randint(0,5), random.randint(0,5))
            bools[rnum1][rnum2] = False
            i += 1
    except:
        print("SEX")

def generation():
    coordinates = False
    while True:
        rnum1, rnum2 = (random.randint(0,5), random.randint(0,5))
        for row in bools:
            for item in row:
                if item == False:
                    coordinates = True
        if coordinates == True:
            if gen[rnum1][rnum2] == "S":
                continue
            else:
                gen[rnum1][rnum2] = "S"
        end = True
        for row in gen:
            for item in row:
                if item == "B":
                    end = False
        os.system("cls")
        gridprint(gen)
        if end == True:
            print("good job, it's all filled with sand")
            break
        

           


while True:
    com = input()
    boolchange()
    if com == "generate":
        generation()
    
