import math
ACCEL_GRAVITY = 9.8
dist = float(input('Введите дистанцию, м: '))
print('Скорость при соприкосновении обекта с землей %.2f м/с' % (math.sqrt(2 * ACCEL_GRAVITY * dist)))