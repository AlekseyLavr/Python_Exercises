import math

hign = float(input('Введите высоту цилиндра, м: '))
radius = float(input('Ведите радиус, м: '))
print('Объём цилиндра %.1f м2' % (math.pi * radius ** 2 * hign))