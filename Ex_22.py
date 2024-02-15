import math
side_1 = float(input('Введите первую сторону треугольника, см: '))
side_2 = float(input('Введите вторую сторону треугольника, см: '))
side_3 = float(input('Введите третью сторону треугольника, см: '))
s = float(side_1 + side_2 + side_3) / 2
if side_1 + side_2 < side_3 or side_2 + side_3 < side_1 or side_1 + side_3 < side_2:
    print('Это не треугольник')
else:
    print('Площадь треугольника %.2f см2' % (math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))))