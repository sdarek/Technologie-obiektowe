# vector.py

import math

class IVector:
    def abs(self):
        pass

    def cdot(self, param):
        pass

    def getComponents(self):
        pass

class Vector2D(IVector):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def abs(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def cdot(self, param):
        return self.x * param.x + self.y * param.y

    def getComponents(self):
        return [self.x, self.y]
