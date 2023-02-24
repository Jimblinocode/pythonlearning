
from os import system
com = input()

class MoveBoy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

player = MoveBoy(0, 0)
    
coord = (player.y, player.x)

while True:
    com = input()
    print(coord)
    
