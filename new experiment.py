
from random import randint

com = input()

location = randint(0,59)

location2 = randint(1,25)
map = [
        ["-----------------------------------------------------------"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"],
        ["-----------------------------------------------------------"],
    ]


    


if com == "m":
    for item in map:
        for item in item:
            print(item)
if com == "where am i?":
    for item in map:
        for item in item:
            loc2 = "a"
            for item in item:
                loc2 += item[location]
