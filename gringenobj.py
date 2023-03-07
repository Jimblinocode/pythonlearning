import random

class worldbiome:
    def __init__(self, tree, grass, soil):
        self.T = tree
        self.G = grass
        self.S = soil
    

desert = worldbiome("P", "#", "S")
grassland = worldbiome("O","|", "D")

truth = False

truelist = [[truth for item in range(6)] for item in range(6)]
world = [["B" for item in range(6)] for item in range(6)]

def gridprint(list):
    for row in list:
        for item in row:
            print(item, end="")
        print("")

def boolevaluator():
        try:
            i = 0
            condition = random.randint(0,36)
            while i < condition:
                n1,n2 = (random.randint(0,5), random.randint(0,5))
                if truelist[n1][n2] == True:
                    continue
                else:
                    truelist[n1][n2] = True
                    i += 1
        except:
            print("UH OH YOU MADE A STINKY!")

def grasslandgenerator():
    coordinates = False
    for row in truelist:
        for item in row:
            if item == True:
                coordinates = True


