import math

class Circle:
    def area(self, r):
        return math.pi * r * r

class Rectangle:
    def area(self, l, w):
        return l * w

class Triangle:
    def area(self, b, h):
        return 0.5 * b * h

shapes = [Circle(), Rectangle(), Triangle()]

print(shapes[0].area(5))
print(shapes[1].area(4, 6))
print(shapes[2].area(3, 7))
