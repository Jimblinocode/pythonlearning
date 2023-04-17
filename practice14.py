class animal:
    def __init__(self, legnum: int, sound: int):
        self.legnum = legnum
        self.sound = sound
    
class snake(animal):
    def __init__(self, legnum, sound):
        super().__init__(legnum, sound)
        self.legnum = 0
        self.sound = "HIIISSSSSSSSS"

class cat(animal):
    def __init__(self, legnum, sound):
        super().__init__(legnum, sound)
        self.legnum = 4
        self.sound = "MROW"

class dog(animal):
    def __init__(self, legnum, sound):
        super().__init__(legnum, sound)
        self.legnum = 4
        self.sound = "BARK BARK"

class offspring(animal):
    def init(self, legnum, sound):
        super().__init__(legnum, sound)

class kitten(cat, offspring):
    def __init__(self, legnum, sound):
        super().__init__(legnum, sound)

class puppy(dog, offspring):
    def __init__(self, legnum, sound):
        super().__init__(legnum, sound)





