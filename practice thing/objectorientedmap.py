import random
import biomes

class map():
    def __init__(self):
        self.world_size = (input("long:"), input("tall:"))
        self.world = [["#" for row in range(int(self.world_size[0]))] for column in range(int(self.world_size[1]))]
        self.i = 0

    def world_print(self):
        for row in self.world:
            for column in row:
                print(column, end="")
            print("")

    
        


    def world_generation(self):
            self.biolist = [biomes.Desert(), biomes.Forest()]
            self.select_biome = self.biolist[random.randint(0, 1)]
            try:
                self.maxgen = int(self.world_size[0])*int(self.world_size[1])
                self.cond = random.randint(0, self.maxgen)
                while self.i < self.cond:
                    self.coordinates = (random.randint(0, int(self.world_size[0])-1), random.randint(0, int(self.world_size[1])-1))
                    if self.world[self.coordinates[0]][self.coordinates[1]] == self.select_biome.soil:
                        self.world[self.coordinates[0]][self.coordinates[1]] = self.select_biome.fauna
                    elif self.world[self.coordinates[0]][self.coordinates[1]] == self.select_biome.fauna:
                        continue
                    else:
                        self.world[self.coordinates[0]][self.coordinates[1]] = self.select_biome.soil
                    self.i += 1
                print(f"generated {self.cond} times!")
                self.world_print()
            except:
                print("uh oh you gotta restart the program again oopsie uwu")


    def run(self):
        pass

map().world_generation()