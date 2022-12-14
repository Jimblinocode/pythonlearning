# Self Practice: fake menu screen

print("Welcome to the Game!")

mylist = ["Start", "Options", "Credits", "Exit"]

running = True

for item in mylist:
    print(item)


while running:
    com = input()
    if com == "Start" or com == "start":
        print("haha theres no actual game, gottem")
    elif com == "Options" or com == "options":
        oplist = ["vol - 1", "graphics - 4", "anti-aliasing - yes", "bitches - none"]
        for item in oplist:
            print(item)
    elif com == "Credits" or com == "credits":
        print("Made by: Isaac Dority")
    elif com == "Exit" or com == "exit":
        running = False
    else:
        print("INVALID COMMAND")
