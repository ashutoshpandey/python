class Square:
    def __init__(self, x):              # self  is   'this' here,   __init__ is constructor
        self.x = x

    def area(self):
        return self.x*self.x

    def perimeter(self):
        return 4*self.x

