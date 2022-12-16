# Challenge 5: building a text adventure shop

print("you have 200G.")
print("There is Nothing in your inventory")

shop = ["the Grass Sword of Thesophelese 50G", "Spell: Finger Gun              75G", "Medium Health Potion           25G", "The Magnum Dong Dildo Sword   200G", "Exit Shop" ]
running = True
inventory = []
pgold = 200

print("Welcome to the fantasy battle imporium! your one stop shop for everything legendary swords, powerful spells, thaumically powered appliances and Potions!")
print("we have...")

for item in shop:
    print(item)

while running:
    com = input()
    
    if pgold == 0:
        print("sorry, you can't afford that")
    
    elif com == "The Grass Sword of Thesophelese" or com == "Grass Sword of Thesophelese" or com == "Grass Sword":
        pgold-= 50
        inventory.append("Grass Sword of Thesophelese")
        print("The Grass sword of Thesophelese has been moved to your inventory -50G.")
        print("you have " + str(pgold),"Gold")
        print("Inventory:")
        for item in inventory:
            print(item)
    
    elif com == "Spell: Finger Gun" or com == "Finger Gun":
        pgold-= 75
        inventory.append("Spell: Finger Gun")
        print("a Finger Gun spell has been moved to your inventory -75G.")
        print("you have " + str(pgold),"Gold")
        print("Inventory:")
        for item in inventory:
            print(item)
    
    elif com == "Medium Health Potion" or com == "Health Potion":
        pgold-= 25
        inventory.append("Medium Health Potion")
        print("a Medium Health Potion has been moved to your inventory -25G")
        print("you have " + str(pgold), "Gold")
        print("Inventory:")
        for item in inventory:
            print(item)
    
    elif com == "The Magnum Dong Dildo Sword" or com == "Magnum Dong Dildo Sword" or com == "Dildo Sword":
        pgold-= 200
        inventory.append("Magnum Dong Dildo Sword")
        print("The Magnum Dong Dildo Sword has been Moved to your inventory -200G")
        print("you have " + str(pgold), "Gold")
        print("Inventory:")
        for item in inventory:
            print(item)
    
    elif com == "Exit Shop" or com == "exit shop":
        running = False

    else:
        print("INVALID COMMAND")