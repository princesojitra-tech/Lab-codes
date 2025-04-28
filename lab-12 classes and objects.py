#1
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def display(self):
        if self.imag >= 0:
            print(f"{self.real} + {self.imag}i")
        else:
            print(f"{self.real} - {-self.imag}i")

    def add(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

    def subtract(self, other):
        real_part = self.real - other.real
        imag_part = self.imag - other.imag
        return ComplexNumber(real_part, imag_part)

    def multiply(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def divide(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

c1 = ComplexNumber(4, 5)
c2 = ComplexNumber(2, -3)

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("\nAddition:")
result = c1.add(c2)
result.display()

print("\nSubtraction:")
result = c1.subtract(c2)
result.display()

print("\nMultiplication:")
result = c1.multiply(c2)
result.display()

print("\nDivision:")
result = c1.divide(c2)
result.display()

#2
class Matrix:
    def __init__(self, m):
        self.m = m

    def show(self):
        for r in self.m:
            print(r)

    def add(self, other):
        return Matrix([[self.m[i][j] + other.m[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        return Matrix([[sum(self.m[i][k] * other.m[k][j] for k in range(3)) for j in range(3)] for i in range(3)])

    def transpose(self):
        return Matrix([[self.m[j][i] for j in range(3)] for i in range(3)])

m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print("Matrix 1:"); m1.show()
print("\nMatrix 2:"); m2.show()

print("\nAddition:"); m1.add(m2).show()
print("\nMultiplication:"); m1.multiply(m2).show()
print("\nTranspose of Matrix 1:"); m1.transpose().show()
print("\nTranspose of Matrix 2:"); m2.transpose().show()

#3
import math

class Solid:
    def __init__(self):
        self.shape = input("Enter shape (cube/cylinder): ").lower()
        if self.shape == "cube":
            self.side = float(input("Enter side length of cube: "))
        elif self.shape == "cylinder":
            self.radius = float(input("Enter radius of cylinder: "))
            self.height = float(input("Enter height of cylinder: "))
        else:
            print("Invalid shape")

    def surface_area(self):
        if self.shape == "cube":
            return 6 * self.side ** 2
        elif self.shape == "cylinder":
            return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        if self.shape == "cube":
            return self.side ** 3
        elif self.shape == "cylinder":
            return math.pi * self.radius ** 2 * self.height

s = Solid()
print("Surface Area:", s.surface_area())
print("Volume:", s.volume())

#4
import math

class Shape:
    def __init__(self):
        self.shape = input("Enter shape (square/rectangle/circle): ").lower()
        if self.shape == "square":
            self.side = float(input("Enter side of square: "))
        elif self.shape == "rectangle":
            self.length = float(input("Enter length: "))
            self.breadth = float(input("Enter breadth: "))
        elif self.shape == "circle":
            self.radius = float(input("Enter radius: "))
        else:
            print("Invalid shape")

    def area(self):
        if self.shape == "square":
            return self.side ** 2
        elif self.shape == "rectangle":
            return self.length * self.breadth
        elif self.shape == "circle":
            return math.pi * self.radius ** 2

    def perimeter(self):
        if self.shape == "square":
            return 4 * self.side
        elif self.shape == "rectangle":
            return 2 * (self.length + self.breadth)
        elif self.shape == "circle":
            return 2 * math.pi * self.radius

s = Shape()
print("Area:", s.area())
print("Perimeter/Circumference:", s.perimeter())


#5
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def display(self):
        print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def add(self, other):
        total_sec = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total_sec)

    def subtract(self, other):
        total_sec = abs(self.to_seconds() - other.to_seconds())
        return Time.from_seconds(total_sec)

    @staticmethod
    def from_seconds(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return Time(h, m, s)

t1 = Time(2, 45, 50)
t2 = Time(1, 20, 15)

print("Time 1:")
t1.display()

print("Time 2:")
t2.display()

print("\nAddition of Time:")
t3 = t1.add(t2)
t3.display()

print("\nSubtraction of Time:")
t4 = t1.subtract(t2)
t4.display()

print("\nTime 1 in seconds:", t1.to_seconds())
print("Time 2 in seconds:", t2.to_seconds())


#6
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def display(self):
        print(f"{self.date[0]:02d}-{self.date[1]:02d}-{self.date[2]}")

    def __eq__(self, other):
        return self.date == other.date

d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
d3 = Date(23, 4, 2025)

print("Date 1:")
d1.display()

print("Date 2:")
d2.display()

print("Date 3:")
d3.display()

print("\nIs Date 1 equal to Date 2?", d1 == d2)
print("Is Date 1 equal to Date 3?", d1 == d3)

#7
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

w = Weather(["temperature", "humidity", "pressure", "wind", "rainfall"])

print("temperature" in w)
print("snowfall" in w)


#8
class String:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        self.text += other.text
        return self

    def toLower(self):
        self.text = self.text.lower()

    def toUpper(self):
        self.text = self.text.upper()

    def show(self):
        print(self.text)

s1 = String("Hello")
s2 = String(" World")

s1 += s2
print("After concatenation:")
s1.show()

s1.toLower()
print("To lowercase:")
s1.show()

s1.toUpper()
print("To uppercase:")
s1.show()
