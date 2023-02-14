from random import randint
from os import system

def randmax():
    numlist = []

    i = 0
    while i < 8:
        numlist.append(randint(0,100))
        i += 1
    j = numlist[0]
    for item in numlist:
        if item > j:
            j = item
    return (j)


i = 0
while True:
    print(i, randmax())
    i += 1
    system("cls")
    if i > 100:
        print(i, randmax())
        break

