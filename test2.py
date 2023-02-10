
from os import system

playernum = 0
playerchar = ("X", "O", "@")

while True:
    player = playerchar[playernum]
    playernum %= 3
    playernum += 1
    
    
    print(player)
    #system("cls")