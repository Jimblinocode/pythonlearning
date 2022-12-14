# challenge 3: guessing game

from random import randint

print("Pick a number between 0 and 100")


minimum = 0
maximum = 100
ans = randint(0, 100)
running = True

while running:
    Num = int(input())
    if Num < minimum or Num > maximum:
        print("invalid input: must be a number between 0 and 100")
    elif Num > ans:
        print("LOWER")
    elif Num < ans:
        print("HIGHER")
    else:
        print("CORRECT!!")
        running = False
