class Shape:
    def __init__(self, shape):
        self.shape = shape

    def shapeName(self):
        print(self.shape)

class Rectangle(Shape):                         # Rectangle class inherits Shape

    count = 0                                   # static variable

    def __init__(self, name):
        Shape.__init__(self, name)
        print('In Rectangle')
        Rectangle.count = Rectangle.count + 1


rec1 = Rectangle('Rectangle')
rec2 = Rectangle('Rectangle')

rec1.shapeName()
rec2.shapeName()

print( Rectangle.count )
