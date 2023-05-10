class Biome:
    def __init__(self):
        self.soil: str = "D"
        self.fauna = "Sh"
        self.hasgrass = True

    def grasschecker(self):
        if self.hasgrass == True:
            self.soil += "G"

class Forest(Biome):
    def __init__(self):
        super().__init__()
        self.fauna = "T"

class Desert(Biome):
    def __init__(self):
        super().__init__()
        self.soil = "S"
        self.hasgrass = False
        

