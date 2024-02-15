import math

side_length = float(input('Введите длину стороны многоугольника: '))
quantity_side = float(input('Введите количество сторон мнгогоугольника: '))
area = (quantity_side * side_length ** 2) / (4 * math.tan(math.pi / quantity_side))
print('Площадь многоугольника: %.2f' % area)