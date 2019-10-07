# http://tinyurl.com/gpqe62e

import math

class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return (self.radius**2) * math.pi

cir = Circle(1)

print(cir.area())
