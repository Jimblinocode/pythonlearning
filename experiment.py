
from random import randint

questionslist = ["--can i keep talking?", "--will i get a girlfriend?", "--should i eat this?", "--how many bitches do i have?", "--can i exit?", "--exit"]

print("welcome to the magic 8-ball! normally magic 8-balls will answer any question, but because this is an experiment, you will only get a set number. \nask away!\n")

for item in questionslist:
    print(item, end="\n----------------------------\n")


running = True

while running:
    com = input()
    num = randint(0,101)
    if com == "can i keep talking?":
        if num < 50:
            print("Stop talking, be quiet")
        elif num > 50:
            print("Keep talking, you've earned it")
    elif com == "will i get a girlfriend?":
        if num < 50:
            print("No, you will be alone forever")
        elif num == 50:
            print("Maybe, who knows?")
        elif num > 50:
            print("Yes, all your problems are solved and you'll never be sad again")
    elif com == "should i eat this?":
        if num < 45:
            print("No, you will die of every disease tomorrow if you do")
        elif num > 46 and num < 52:
            print("Maybe, it never hurts to roll the dice")
        elif num > 53:
            print("yes, not only is it healthy but you'll gain super powers and be able to talk to women")
    elif com == "how many bitches do i have?":
        print(f"you have {num} bitches")
    elif com == "can i exit?":
        if num < 10:
            running = False
        elif num > 10:
            print("No, your stuck here forever >:)")
    elif com == "exit":
        print("okay fine :(")
        running = False
    