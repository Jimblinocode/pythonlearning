# Challenge 5: building a text adventure shop

print("you have 200G.")
print("There is Nothing in your inventory")

shop = {
"the Grass Sword of Thesophelese": 50, 
"Spell: Finger Gun": 75, 
"Medium Health Potion": 25,
"The Magnum Dong Dildo Sword": 200,
}
running = True
inventory = []
pgold = 200



print("Welcome to the fantasy battle imporium! your one stop shop for everything legendary swords, powerful spells, thaumically powered appliances and Potions!")
print("we have...")


while running:
    for key in shop:
        print(key + "     " + str(shop[key]) + "G")
    com = input()
    
    for key in shop:
        if com == key:
            if pgold < shop[key]:
                print("Sorry, you can't afford this item.")
            else:
                pgold-= shop[key]
                print("-" + str(shop[key]) + "G")
                inventory.append(key)
                print(key + " has been added to inventory")
                print("you have " + str(pgold)+ "G" + " left")
                
            
    for item in inventory:
        print("inventory:")
        print(item)
        print("------------")
    
     