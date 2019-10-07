# http://tinyurl.com/j9qjnep

class Square:
    square_list = []
    
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1*4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1)


s1 = Square(10)
print(s1)
