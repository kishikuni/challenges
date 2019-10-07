# http://tinyurl.com/j9qjnep

class Square:
    square_list = []
    
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1*4

def is_same(obj1, obj2):
    return obj1 is obj2

sq = Square(10)
same_sq = sq

print(is_same(sq,same_sq))

another_sq = Square(10)
print(is_same(sq,another_sq))
