# http://tinyurl.com/gpqe62e

class Triangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def area(self):
        return 1/2 * self.width * self.height

tri = Triangle(2,1)
print(tri.area())
