import random
print("roll a D20!")
while True:
    i = 0
    com = input()
    if com == "roll" or com == "ROLL":
        while i < 2:
            thingy = random.randint(0,20)
            print(thingy)
            if thingy == 20:
                break
            else:
                i += 2

            
