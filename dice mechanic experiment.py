from random import randint
print("hello and welcome to the stat dispencer!, select a class and roll a series of dice to see what your default stats will be!\nSelect a class.")

classlist = ["1. Brute", "2. Knight", "3. bandit", "4. Pyromancer", "5. Mage", "6. Clergy" ]

for item in classlist:
    print("     ", item)

running = True
# classes
brute = False
knight = False
bandit = False
Pyromancer = False
Mage = False
clergy = False

stats = {
    "HP: ": " ",
    "MP: ": " ",
    "Strength: ": " ",
    "Health: ": " ",
    "Dexterity: ": " ",
    "Passion: ": " ",
    "Intellect: ": " ",
    "Empathy: ": " "
}

def HPdecider():
    if stats["Health: "] <= 5:
        stats["HP: "] = 10
    elif stats["Health: "] >= 6 and stats["Health: "] <= 10:
        stats["HP: "] = 20
    elif stats["Health: "] >= 11 and stats["Health: "] <= 15:
        stats["HP: "] = 30
    elif stats["Health: "] >= 16 and stats["Health: "] <= 19:
        stats["HP: "] = 40
    elif stats["Health: "] == 20:
        stats["HP: "] = 50

def MPdecider():
    if stats["Intellect: "] <= 5:
        stats["MP: "] = 5
    elif stats["Intellect: "] >= 6 and stats["Intellect: "] <= 10:
        stats["MP: "] = 10
    elif stats["Intellect: "] >= 11 and stats["Intellect: "] <= 15:
        stats["MP: "] = 15
    elif stats["Intellect: "] >= 16 and stats["Intellect: "] <= 19:
        stats["MP: "] = 20
    elif stats["Intellect: "] == 20:
        stats["MP: "] = 25

def statchooser():
    statlist = []

    i = 0
    while i < 6:
        statlist.append(randint(1,20))
        i += 1
    if brute == True:
        focus = "Strength: "
        stats["Strength: "] = max(statlist)
        statlist.remove(max(statlist))
    elif knight == True:
        focus = "Health: "
        stats["Health: "] = max(statlist)
        statlist.remove(max(statlist))
    elif bandit == True:
        focus = "Dexterity: "
        stats["Dexterity: "] = max(statlist)
        statlist.remove(max(statlist))
    elif Pyromancer == True:
        focus = "Passion: "
        stats["Passion: "] = max(statlist)
        statlist.remove(max(statlist))
    elif Mage == True:
        focus = "Intellect: "
        stats["Intellect: "] = max(statlist)
        statlist.remove(max(statlist))
    elif clergy == True:
        focus = "Empathy: "
        stats["Empathy: "] = max(statlist)
        statlist.remove(max(statlist))
    base = 4
    for key in stats:
        if key == "HP: " or key == "MP: ":
            continue
        if key == focus:
            continue
        elif base == 0:
            rest = statlist[0]
            stats[key] = rest
            statlist.remove(rest)
        else:
            rest = statlist[randint(0,base)]
            stats[key] = rest
            statlist.remove(rest)
            base -= 1
    HPdecider()
    MPdecider()
    for key in stats:
        print("     ", key, stats[key])

while running:
    com = input()
   
    if com == "Brute":
        brute = True
        statchooser()
    elif com == "Knight":
        knight = True
        statchooser()
    elif com == "Bandit":
        bandit = True
        statchooser()
    elif com == "Pyromancer":
        Pyromancer = True
        statchooser()
    elif com == "Mage":
        Mage = True
        statchooser()
    elif com == "Clergy":
        clergy = True
        statchooser()
    elif com == "Exit":
        running = False
    else: 
        print("NO")


