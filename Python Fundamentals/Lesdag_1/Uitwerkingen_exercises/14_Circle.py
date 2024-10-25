import math

radiusString = input("What is the radius of the circle? ")
print("radiusString:", type(radiusString))
r = float(radiusString)
print("r:", type(r))

area = math.pi * r**2

circumference = 2 * math.pi * r

print("The circle has a radius:", r)
print("The area of the circle is", area)
print("area:", type(area))
print("The circumference of the circle is:", circumference)
print("circumference:", type(circumference))