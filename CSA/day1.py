from math import *

# class Person:
#     name = ""
#     age = 0
#     sex = ""
#
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def print(self):
#         print(self.name, self.age, self.sex)
#
#     def levelUp(self):
#         self.age += 1
#
#
# Me = Person("Duy", 23, "M")
# Me.print()
# Me.levelUp()
# Me.print()

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def tick(self):
#         self.count += 1
#
#     def doubleTick(self):
#         self.tick()
#         self.tick()
#
#     def reset(self):
#         self.count = 0
#
#     # def print(self):
#     #     print(self.count)
#
#
# time = Counter()
#
# time.tick()
# print(time.count)
# time.reset()
# print(time.count)
# Counter.tick(time)


class HinhChuNhat:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width + self.height) * 2

    def getDiagonal(self):
        return sqrt(self.width ** 2 + self.height ** 2)

    def getAreaRectangle(self):
        return self.getArea() / 2

    def getPerimeterRectangle(self):
        return self.width + self.height + self.getDiagonal()

    def getAreaCircle(self):
        if self.width < self.height:
            return (self.width / 2) ** 2 * pi
        else:
            return (self.height / 2) ** 2 * pi

    def getPerimeterCircle(self):
        if self.width < self.height:
            return self.width * pi
        else:
            return self.height * pi


test = HinhChuNhat(6, 8)
print(test.getArea())
print(test.getPerimeter())
print(test.getDiagonal())
print(test.getAreaRectangle())
print(test.getPerimeterRectangle())
print(test.getAreaCircle())
print(test.getPerimeterCircle())
