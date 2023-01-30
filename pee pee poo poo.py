

def curse(var:str):
    curse = ""
    for item in var:
        curse = item + curse
    return(curse)







running = True
stinkoptions = ["1. yes", "2. no"]
print("art thou stinky?")

for item in stinkoptions:
    print("\n -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n",  item, "\n -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n")


while running:
    var = input()


    if var == "yes":
       print("back off, this is holy ground")
    elif var == "no":
       print("come sit in the sacred gamer chair")
    elif var =="*hisss*":
       print(curse("you've cursed me, you foul stink creature! leave this sacred gaming ground and never come back"))
    else:
        print("speaking jibberish i see, just as a stinky cat would. back off, this is holy ground")


