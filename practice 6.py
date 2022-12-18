# Challenge 5: building a text adventure shop

print("you have 200G.")
print("There is Nothing in your inventory")

shop = {
"The Grass Sword of Thesophelese": 50, 
"Spell: Finger Gun": 75, 
"Medium Health Potion": 25,
"The Magnum Dong Dildo Sword": 200,
}
running = True
inventory = []
pgold = 200



while running:
    print("Welcome to the fantasy battle imporium! your one stop shop for everything legendary swords, powerful spells, thaumically powered appliances and Potions!")
    print("we have...")

    for key in shop:
        print(key + "     " + str(shop[key]) + "G")
    com = input()
    
    if com != key:
        print("Sorry, we don't have that")
    if com == "exit":
        run_exit = True
        while run_exit:
            print("you have " + str(pgold) + "G")
            print("inventory:")
            for item in inventory:
                print(item)
                print("------------")
            print("Are you sure you want to leave the shop? (Y/N)")
            com = input()      
            if com == "yes":
                running = False
                run_exit = False
            elif com == "no":
                run_exit = False
    
    else:
        for key in shop:
            if com == key:
                if pgold < shop[key]:
                    print("Sorry, you can't afford this item.")
                    print("----------------------------------")
                else:
                    pgold-= shop[key]
                    print("-" + str(shop[key]) + "G")
                    inventory.append(key)
                    print(key + " has been added to inventory")
                    print("you have " + str(pgold)+ "G" + " left")
                    print("inventory:")
                    for item in inventory:
                        print(item)
                        print("------------")


    
     