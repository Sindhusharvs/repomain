import math

class Circle:
    def __init__(self,r):
        self.area=math.pi*r*r
        self.perimeter=2*math.pi*r
    def area(self):
        print('Area:',self.area)
    def perimeter(self):
        print('Perimeter',self.perimeter)

Radius=float(input('Enter Radius:'))
obj=Circle(Radius)
obj.area()
obj.perimeter()
