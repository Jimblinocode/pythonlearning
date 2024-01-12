class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)