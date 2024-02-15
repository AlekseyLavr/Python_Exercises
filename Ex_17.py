WATER_HEAT_CAPACITY = 4.186
PRICE = 8.9
J_KWH = 2.7778e-7
mass = float(input('Введите массу воды, в граммах: '))
diff_temp = float(input('Введите разницу температур, в градусах Цельсия: '))
q = mass * WATER_HEAT_CAPACITY * diff_temp
print('Количество энергии %d Дж' % q)
cost = J_KWH * PRICE * q
print('Стоимость энергии: %.2f кВт/ч в центах' % cost)
