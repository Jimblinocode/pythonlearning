from os import *

first = []
last = []




def yourname():
    i = 0
    while i < 3:
        print("Enter a first name")
        com = input()
        first.append(com)
        system("cls")
        print("Enter a Last name")
        com2 = input()
        last.append(com2)
        system("cls")
        i += 1
    print("first names:")
    print("-------------",)
    for item in first:
        print(item)
    print("-------------\n",)
    print("\nlast names:")
    print("-------------",)
    for item in last:
        print(item)
    print("-------------\n",)
def gamestart():
    pass


yourname()
    
        