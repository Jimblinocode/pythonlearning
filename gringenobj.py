import random
import os

class worldbiome:
    def __init__(self, tree, grass, soil):
        self.T = tree
        self.G = grass
        self.S = soil
    

desert = worldbiome("P", "#", "S")
grassland = worldbiome("O","|", "D")




world = [["B" for item in range(12)] for item in range(12)]

objlist =[desert, grassland]
biome = objlist[random.randint(0,1)]

def gridprint(list):
    for row in list:
        for item in row:
            print(item, end="")
        print("")

def worldgen():
        try:
            i = 0
            condition = random.randint(0,144)
            while i < condition:
                n1,n2 = (random.randint(0,11), random.randint(0,11))
                if world[n1][n2] == biome.S:
                    world[n1][n2] = biome.G
                elif world[n1][n2] == biome.G:
                    world[n1][n2] == biome.T
                elif world[n1][n2] == biome.T:
                    continue
                else:
                    world[n1][n2] = biome.S
                    i += 1
            gridprint(world)
        except:
            print("UH OH YOU MADE A STINKY!")
 
os.system("cls")
worldgen()   