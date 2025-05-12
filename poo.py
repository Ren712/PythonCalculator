import math 

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calulate_circle_area(self):
        return math.pi * self.radius**2

    def calulate_circle_perimeter(self):
        return math.pi * self.radius *2

radius= (float(input("Input the radius of the circle: ")))
circle= Circle(radius)
area=circle.calulate_circle_area()
print("Area:" , area)
perimeter=circle.calulate_circle_perimeter()
print("Perimeter" , perimeter)