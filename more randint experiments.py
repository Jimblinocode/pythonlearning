from random import randint



print("choose your target:")

targets = ["1. short bald man", "2. blonde woman in suit", "3. older man smoking cigar"]

for item in targets:
    print(item, "\n -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n")

running = True
com = input()

def escapechance():
    eschance = randint(0,100)
    if eschance <= 50:
        print("you managed to escape the authorities, for now...")
        print("SUCCESS", sep=" ")
        running = False
    elif eschance > 50:
        print("you were arrested and sent to prison before you could get away")
        print("GAME OVER", sep=" ")
        running = False
    

def killmove():
    killchance = randint(0,100)
    if killchance < 49:
        print("you point the gun over your dying target, readying yourself to enact the killing blow. suddenly, an assailant comes from behind and tackles you before you get the chance.\n the resulting scuffle causes you and the assailant to fall out of a 6 story window, killing you and the assailant instantly.")
        print("GAME OVER", sep=" ")
        running = False
    elif killchance > 49 and killchance < 90:
        print("you point the gun over your dying target, readying yourself to enact the killing blow. you manage to shoot 2-3 more rounds at the target brfore you hear police sirens.\n your target is definately dead, but the authorities are after you now.")
        escapechance()
    elif killchance > 90:
        print("you point the gun over your dying target, readying yourself to enact the killing blow. you completely empty your clip into the target, ensuring their death.\n you manage to somehow do this without alerting anyone in the building, giving you ample time to escape and ensuring you get away scot free.")
        print("SUCCESS", sep=" ")
        running = False


def aim():
    chance = randint(0,100)
    oplist = ["1. shoot them multiple times while they're on the ground, ensuring the targets death", "2. try to escape before the authorities are contacted"]
    
    if chance <= 3:
        print("critical hit, the targets head and torso explode into gore. everyone inside the building is panicking, the authorities are quickly notified and you try to leave before they catch you")
        escapechance()
    elif chance > 4 and chance < 20:
        print("you fire at the target, but the gun jams to the point of exploding, blowing your arm off and causing you to bleed to death in the process.")
        print("GAME OVER", sep=" ")
        running = False
    elif chance > 20 and chance < 40:
        print("you shoot at the target, but the bullet meerly skims their arm, allowing the target to find cover and contact the authorities. you try to leave before the authorities catch you")
        escapechance()
    elif chance > 40 and chance < 60:
        print("you hit the target in the torso, causing them to double over and fall to the ground. the target is still alive but cannot fight back against you nor contact the authorities. you have two options.")
        for item in oplist:
            print(item, "\n -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- \n")
        if com == "1":
            killmove()
        elif com == "2":
            escapechance()
    elif chance > 60 and chance < 80:
        print("your bullet misses the target completely and ricochets off a metal surface within the building and hits you in the head, killing you instantly.")
        print("GAME OVER", sep=" ")
        running = False
    elif chance > 80 and chance < 90:
        print("you shoot the target in the head, killing them instantly. this alerts everyone in the building, leading to the authorities being contacted. you try to escape before they find you.")
        escapechance()
    elif chance > 90:
        print("you shoot the target in the head, killing them instantly. you somehow do this without alerting anyone in the building. this allows you to escape unnoticed and get away scot free")
        print("SUCCESS", sep=" ")
        running = False

while running:
    com = input
    if com == "short bald man":
        aim()
    if com == "blonde woman in suit":
        aim()
    if com == "older man smoking cigar":
        aim()