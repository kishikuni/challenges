# http://tinyurl.com/hz9qdh3

# classはinitを定義しなくてもできる
class Shape:
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return 2*(self.width + self.len)

class Square(Shape):
    def __init__(self, w):
        self.width = w
    def calculate_perimeter(self):
        return 4*(self.width)
    def change_size(self, add_size):
        self.width +=  add_size

squ1 = Square(20)
print(squ1.calculate_perimeter())

# squ1.change_size(-10)
# print(squ1.calculate_perimeter())

squ1.what_am_i()
