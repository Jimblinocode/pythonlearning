# challenge 3: guessing game

from random import randint

print("Pick a number between 0 and 100")

Num = input()
minimum = 0
maximum = 100
ans = randint(0, 100)
running = True

while running:
    if int(Num) < minimum or int(Num) > maximum:
        print("invalid input: must be a number between 0 and 100")
        Num = input()
    elif int(Num) > ans or int(Num) < ans:
        print("WRONG")
        Num = input()
    elif int(Num) == ans:
        print("CORRECT!!")
        running = False
