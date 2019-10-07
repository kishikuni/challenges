# http://tinyurl.com/gpqe62e

class Hexagon:
    def __init__(self,h):
        self.height = h

    def calculate_perimeter(self):
        return 1/2 * self.height * 6

hex = Hexagon(2)
print(hex.calculate_perimeter())
