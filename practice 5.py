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
        com = input()
    elif com == "Options" or com == "options":
        print("vol - 4")
        print("graphics - 1")
        print("anti-aliasing - yes")
        print("bitches - none")
        com = input()
    elif com == "Credits" or com == "credits":
        print("Made by: Isaac Dority")
        com = input()
    elif com == "Exit" or com == "exit":
        running = False
