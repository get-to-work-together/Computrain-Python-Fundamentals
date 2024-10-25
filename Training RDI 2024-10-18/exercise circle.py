import math

radius = float(input('Geef de straal: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f'radius        : {radius:8.3f}')
print(f'area          : {area:8.3f}')
print(f'circumference : {circumference:8.3f}')
