# http://tinyurl.com/hz9qdh3

class Horse:
    def __init__(self, breed, age, rider):
        self.breed = breed
        self.age = age
        self.rider = rider

class Rider:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rider = Rider("星 豊",48)
horse = Horse("赤毛",4,rider)

print("騎手:{} {}歳".format(horse.rider.name,horse.rider.age))
