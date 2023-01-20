from random import randint

print("Wellcome to Magic 8-ball 2.0! this is a much better version of the previous one i made, because it will actually allow you to ask any question.\nAsk away! \n --------------------------------------------------------------------------------------------------------------------------------------------------------- \n")



def eightball(com):
    num = randint(0,7)
    if num == 0:
        print("Stop talking, be quiet")
    elif num == 1:
        print("no, fuck you")
    elif num == 2:
        print("sure, i guess")
    elif num == 3:
        print("Keep talking, you've earned it")
    elif num == 4:
        print("yes, keep telling yourself that")
    elif num == 5:
        print("no, you are delusional")
    else:
        print("yes, i'm sure you're right")
    return


running = True
while running:
    com = input()
    if com == "exit":
        running = False
    else:
        eightball(com)
    