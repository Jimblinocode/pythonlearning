from random import randint
from os import system
phraselist = ["The problem with", "the vaushification of", "in defense of"]
phraselist2 = ["pedophillia", "chris chan", "vaush"]
 
i = 0
i2 = 0
p1, p2 = (phraselist[i], phraselist2[i2])
print(p1, p2)
while True:
    com = input()
    if com == "w":
        system("cls")
        i += 1
        if i > 2:
            i -= 1
        p1 = phraselist[i%3]
        print(p1, p2)
    elif com == "s":
        system("cls")
        i -= 1
        if i < 0:
            i += 1
        p1 = phraselist[i%3]
        print(p1, p2)
    elif com == "d":
        system("cls")
        i2 += 1
        if i2 > 2:
            i2 -= 1
        p2 = phraselist2[i2%3]
        print(p1, p2)
    elif com == "a":
        pass
   
        











#class phrasecustomiser:
    #def __init__(self, x):
        #self.x = 0

    #def moveup():
        #if com == "w":

