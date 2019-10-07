# http://tinyurl.com/j9qjnep

class Square:
    square_list = []
    
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1*4


s1 = Square(10)
print(Square.square_list)

s2 = Square(20)
s3 = Square(30)

print(Square.square_list)
